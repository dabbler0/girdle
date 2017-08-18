from cnf import *

class TokenStream:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def peek(self):
        return self.tokens[self.index]

    def consume(self):
        self.index += 1

class AxiomParser:
    def __init__(self, binary_ops, unary_prefix_ops, unary_postfix_ops, constants, tokens):
        self.binary_ops = binary_ops
        self.unary_prefix_ops = unary_prefix_ops
        self.unary_postfix_ops = unary_postfix_ops

        self.tokens = tokens
        self.constants = constants
        self.variables = {}

    def parse_lexpression(self):
        return self.parse_universal_quantifier()

    def parse_universal_quantifier(self):
        if self.tokens.peek() == 'forall':
            self.tokens.consume()
            vname = self.tokens.peek()

            if vname in self.variables:
                raise Exception('You reused variable name %s in a single expression.' % (vname,))

            variable = Variable(vname)
            self.variables[vname] = variable

            self.tokens.consume()

            return UniversalQuantifier(variable, self.parse_universal_lexpression())

        return self.parse_existential_quantifier()

    def parse_existential_quantifier(self):
        if self.tokens.peek() == 'exists':
            self.tokens.consume()
            vname = self.tokens.peek()

            if vname in self.variables:
                raise Exception('You reused variable name %s in a single expression.' % (vname,))

            variable = Variable(vname)
            self.variables[vname] = variable

            self.tokens.consume()

            return ExistentialQuantifier(variable, self.parse_lexpression())

        return self.parse_implication()

    def parse_implication(self):
        expr = self.parse_lor()

        if self.tokens.peek() == '=>':
            self.tokens.consume()

            result = self.parse_lexpression()

            expr = Implication(expr, result)

        return expr

    def parse_lor(self):
        expr = self.parse_land()

        if self.tokens.peek() == 'or':
            self.tokens.consume()

            result = self.parse_lor()

            expr = Disjunction(expr, result)

        return expr

    def parse_land(self):
        expr = self.parse_lnegation()

        if self.tokens.peek() == 'and':
            self.tokens.consume()

            result = self.parse_land()

            expr = Conjunction(expr, result)

        return expr

    def parse_lnegation(self):
        if self.tokens.peek() == '~':
            self.tokens.consume()

            return Negation(self.parse_lnegation())

        return self.parse_lprimary()

    def parse_lprimary(self):
        if self.tokens.peek() == '(':
            self.tokens.consume()
            expr = self.parse_lexpression()
            self.tokens.consume()

            return expr

        return self.parse_expression()

    def parse_expression(self):
        return self.parse_binary_op(0)

    def parse_binary_op(self, index):
        if index >= len(self.binary_ops):
            return self.parse_unary_prefix_op(0)

        operator_text, is_left_associative = self.binary_ops[index]

        expr = self.parse_binary_op(index + 1)

        if is_left_associative:
            while self.tokens.peek() == operator_text:
                self.tokens.consume()
                next_expr = self.parse_binary_op(index + 1)

                expr = Expression((self.constants[operator_text], expr, next_expr))

        else:
            if self.tokens.peek() == operator_text:
                self.tokens.consume()

                next_expr = self.parse_binary_op(index)

                expr = Expression((self.constants[operator_text], expr, next_expr))

        return expr

    def parse_unary_prefix_op(self):
        if self.tokens.peek() in self.unary_prefix_ops:
            op = self.constants[self.tokens.peek()]
            self.tokens.consume()
            return Expression((op, self.parse_unary_prefix_op(index)))

        return self.parse_functional()

    # Functional also includes postfix ops
    def parse_functional(self):
        expr = self.parse_primary()

        while True:
            if self.tokens.peek() == '(':
                self.tokens.consume()
                args = [self.parse_expression()]
                while self.tokens.peek() == ',':
                    self.tokens.consume()
                    args.append(self.parse_expression())
                self.tokens.consume()
                expr = Expression(tuple([expr] + args))

            elif self.tokens.peek() in self.unary_postfix_ops:
                op = self.constants[self.tokens.peek()]
                self.tokens.consume()
                return Expression((op, expr))

            else:
                break

        return expr

    def parse_primary(self):
        if self.tokens.peek() == '(':
            self.tokens.consume()
            result = self.parse_expression()
            self.tokens.consume()
            return result

        return self.parse_literal()

    def parse_literal(self):
        token = self.tokens.peek()
        self.tokens.consume()

        if token in self.constants:
            return self.constants[token]
        elif token not in self.variables:
            self.variables[token] = Variable(token)

        return self.variables[token]

class ProgramParser:
    def __init__(self, tokens):
        self.tokens = tokens

        self.binary_ops = []
        self.prefix_ops = []
        self.postfix_ops = []
        self.constants = {}

        self.axioms = []
        self.theorems = {}

    def parse_block(self):
        if self.tokens.peek() == 'constants':
            self.tokens.consume()
            self.parse_constants_block()

        if self.tokens.peek() == 'axioms':
            self.tokens.consume()
            self.parse_axioms_block()

        if self.tokens.peek() == 'theorem':
            self.tokens.consume()

            # Theorem name
            theorem_name = self.tokens.peek()
            self.tokens.consume()

            # Arguments
            arguments = []
            if self.tokens.peek() == '(':
                self.tokens.consume()
                arguments.append(self.tokens.peek())
                self.tokens.consume()

                while self.tokens.peek() == ',':
                    self.tokens.consume()
                    arguments.append(self.tokens.peek())
                    self.tokens.consume()

                self.tokens.consume()

            parser = TheoremParser(self, arguments)

            theorem_object = parser.parse_theorem()

            self.theorems[theorem_name] = theorem_object

    def parse_constants_block(self):
        if self.tokens.peek() == '~INDENT~':
            self.tokens.consume()
            self.parse_constants_line()
            while self.tokens.peek() == '~NEWLINE~':
                self.tokens.consume()
                self.parse_constants_line()
            self.tokens.consume()
        else:
            pass

    def parse_constants_line(self):
        constant_name = self.tokens.peek()

        if constant_name in self.constants:
            raise Exception('You defined the constant %s twice.' % (constant_name,))

        self.constants[constant_name] = Constant(constant_name)

        if self.tokens.peek() == 'binary':
            self.tokens.consume()

            if self.tokens.peek() == 'left':
                self.tokens.consume()
                self.binary_ops.append((constant_name, True))
            elif self.tokens.peek() == 'right':
                self.tokens.consume()
                self.binary_ops.append((constant_name, False))
            else:
                self.binary_ops.append((constant_name, False))

        elif self.tokens.peek() == 'prefix':
            self.tokens.consume()
            self.prefix_ops.append(constant_name)

        elif self.tokens.peek() == 'postfix':
            self.tokens.consume()
            self.postfix_ops.append(constant_name)

    def parse_axioms_block(self):
        if self.tokens.peek() == '~INDENT~':
            self.tokens.consume()
            self.parse_constants_line()
            while self.tokens.peek() == '~NEWLINE~':
                self.tokens.consume()
                self.axioms.append(self.parse_axiom_line())
            self.tokens.consume()
        else:
            pass

    def parse_axiom_line(self):
        parser = AxiomParser(self.binary_ops, self.prefix_ops, self.postfix_ops, self.constants, self.tokens)
        return parser.parse_lexpression()

class TheoremParser:
    def __init__(self, context, arguments):
        self.constants = {**context.constants}
        for argument in arguments:
            self.constants[argument] = Constant(argument)

        self.tokens = context.tokens

    def parse_theorem_line(self):
        '''
        There are three kinds of lines that can occur in a theorem.

        A statement: this is a simple axiom line which is proved by the prover.
        A theorem application: begins with the word 'apply', and applies a previous theorem explicitly
        A choose statement: begins with the word 'choose', and expand an exists statement.
        '''

        # Test for 'choose' statement
        if self.tokens.peek() == 'choose':
            return self.parse_choose_line()

        if self.tokens.peek() == 'apply':
            return self.parse_apply_line()

        return self.parse_statement_line()
