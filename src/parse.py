from cnf import *
import antlr4
import grammar.girdleParser
import grammar.girdleLexer
import re

def transform(tree, constants, variables, necessary_quantifiers):
    if variables == None:
        variables = {}

    # Terminals.
    if 'symbol' in dir(tree):
        text = tree.getText()

        if text in constants:
            return constants[text]
        elif text not in variables:
            variables[text] = Variable(text)
            necessary_quantifiers[variables[text]] = True
        return variables[text]

    # Nonterminals.
    else:
        rule_name = tree.parser.ruleNames[tree.getRuleIndex()]

        # Expression: pass-through
        if rule_name in ('line', 'fol_expression'):
            return transform(tree.children[0], constants, variables, necessary_quantifiers)

        elif rule_name == 'primary_fol_expression':
            if len(tree.children) == 1:
                return transform(tree.children[0], constants, variables, necessary_quantifiers)
            else:
                return transform(tree.children[1], constants, variables, necessary_quantifiers)

        # Universal quantifier
        elif rule_name == 'fol_universal_quantifier':
            if len(tree.children) == 1:
                return transform(tree.children[0], constants, variables, necessary_quantifiers)
            else:
                variable = transform(tree.children[1], constants, variables, necessary_quantifiers)
                necessary_quantifiers[variable] = False
                return UniversalQuantifier(variable, transform(tree.children[3], constants, variables, necessary_quantifiers))

        # Existential quantifier
        elif rule_name == 'fol_existential_quantifier':
            if len(tree.children) == 1:
                return transform(tree.children[0], constants, variables, necessary_quantifiers)
            else:
                variable = transform(tree.children[1], constants, variables, necessary_quantifiers)
                necessary_quantifiers[variable] = False
                return ExistentialQuantifier(variable, transform(tree.children[3], constants, variables, necessary_quantifiers))

        elif rule_name == 'fol_implication_or_equivalence':
            return transform(tree.children[0], constants, variables, necessary_quantifiers)

        # Implication
        elif rule_name == 'fol_implication':
            if len(tree.children) == 1:
                return transform(tree.children[0], constants, variables, necessary_quantifiers)
            else:
                return Implication(transform(tree.children[0], constants, variables, necessary_quantifiers), transform(tree.children[2], constants, variables, necessary_quantifiers))

        elif rule_name == 'fol_equivalence':
            if len(tree.children) == 1:
                return transform(tree.children[0], constants, variables, necessary_quantifiers)
            else:
                return Equivalence(transform(tree.children[0], constants, variables, necessary_quantifiers), transform(tree.children[2], constants, variables, necessary_quantifiers))

        # Disjunction
        elif rule_name == 'fol_disjunction':
            if len(tree.children) == 1:
                return transform(tree.children[0], constants, variables, necessary_quantifiers)
            else:
                return Disjunction(transform(tree.children[0], constants, variables, necessary_quantifiers), transform(tree.children[2], constants, variables, necessary_quantifiers))

        # Conjunction
        elif rule_name == 'fol_conjunction':
            if len(tree.children) == 1:
                return transform(tree.children[0], constants, variables, necessary_quantifiers)
            else:
                return Conjunction(transform(tree.children[0], constants, variables, necessary_quantifiers), transform(tree.children[2], constants, variables, necessary_quantifiers))

        # Negation
        elif rule_name == 'fol_negation':
            if len(tree.children) == 1:
                return transform(tree.children[0], constants, variables, necessary_quantifiers)
            else:
                return Negation(transform(tree.children[1], constants, variables, necessary_quantifiers))

        # Literal (expressions)
        elif rule_name == 'expression':
            if len(tree.children) == 1:
                return transform(tree.children[0], constants, variables, necessary_quantifiers)
            else:
                return Expression(transform(x, constants, variables, necessary_quantifiers) for x in tree.children)

        elif rule_name == 'primary_expression':
            if len(tree.children) == 1:
                return transform(tree.children[0], constants, variables, necessary_quantifiers)
            else:
                return transform(tree.children[1], constants, variables, necessary_quantifiers)

        else:
            print('uh what is', rule_name)

def parse(text, constants):
    chars = antlr4.InputStream(text)
    lexer = grammar.girdleLexer.girdleLexer(chars)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = grammar.girdleParser.girdleParser(tokens)
    parser.buildParseTrees = True

    result_variables = {}
    necessary_quantifiers = {}
    result = transform(parser.line(), constants, result_variables, necessary_quantifiers)

    for var in necessary_quantifiers:
        if necessary_quantifiers[var]:
            result = UniversalQuantifier(var, result)

    return result

def parse_program(text):
    # A Girdle program has three sections. GLOBALS, AXIOMS, and a set of THEOREMS.
    # GLOBALS first.

    lines = text.split('\n')

    mode = None
    constants = {}
    axioms = {} # Empty axiom list
    theorem_lines = []
    for i, line in enumerate(lines):
        if re.match('^\s*$', line) is not None:
            continue
        elif line == 'CONSTANTS':
            mode = 'CONSTANTS'
        elif line == 'AXIOMS':
            mode = 'AXIOMS'
        elif line == 'THEOREM':
            mode = 'THEOREM'

        else:
            if mode is None:
                raise Exception('Encountered statement outside of a recognized block (line %d)' % (i,))

            elif mode == 'CONSTANTS':
                constants_here = re.split('\s*,\s*', re.sub('\s*$', '', re.sub('^\s*', '', line)))

                for constant in constants_here:
                    constants[constant] = Constant(constant)

            elif mode == 'AXIOMS':
                split = line.split(';')
                comment = 'a given axiom'
                if len(split) > 1:
                    comment = re.sub('^\s*', '', re.sub('\s*$', '', split[1]))
                line = split[0]

                axioms_here = parse(line, constants).cnf()

                for axiom in axioms_here.disjunctions:
                    axioms[axiom] = comment

            elif mode == 'THEOREM':
                theorem_lines.append(parse(line, constants))

    return axioms, theorem_lines

if __name__ == '__main__':
    print('WELL-FOUNDEDNESS AXIOM TEST')
    tree = parse('forall g. (forall x. (f x) => (g x)) and (exists q. (g q)) => ((g base) or (exists y. ~(g y) and (g (succ y))))', {'succ': Constant('succ'), 'f': Constant('f'), 'base': Constant('base')})
    print(str(tree))

    print('PROGRAM TEST')
    program = parse_program(open('test_program.txt', 'r').read())
    print('AXIOMS:')
    print(str(program[0]))
    print('THEOREM LINES:')
    for line in program[1]:
        print(str(line))
        print('CNF:', str(Negation(line).cnf()))
