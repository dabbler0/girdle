# Conjunctive Normal Form
class CNF:
    def __init__(self, disjunctions):
        self.disjunctions = set(disjunctions)

    def __hash__(self):
        return hash(self.disjunctions)

    def __eq__(self, other):
        return self.disjunctions == other.disjunctions

    def __str__(self):
        return ' \u2227 '.join(str(x) for x in self.disjunctions)

    def join(self, other):
        return CNF(self.disjunctions | other.disjunctions)

class CNFDisjunction:
    def __init__(self, terms):
        self.terms = frozenset(terms)

    def __hash__(self):
        return hash(self.terms)

    def __eq__(self, other):
        return self.terms == other.terms

    def __str__(self):
        return '(%s)' % ' \u2228 '.join(str(x) for x in self.terms)

    def join(self, other):
        return CNFDisjunction(self.terms | other.terms)

class CNFTerm:
    def __init__(self, expression, sign):
        self.expression = expression
        self.sign = sign

    def __hash__(self):
        return hash((self.expression, self.sign))

    def __eq__(self, other):
        return isinstance(other, CNFTerm) and other.expression == self.expression and other.sign == self.sign

    def __str__(self):
        if self.sign == False:
            return '\u00AC%s' % (str(self.expression),)
        else:
            return str(self.expression)

    def negative(self):
        return CNFTerm(self.expression, not self.sign)

class Expression:
    def __init__(self, children):
        self.children = tuple(children)

    def substitute(self, mapping):
        return Expression(tuple(x.substitute(mapping) for x in self.children))

    def __str__(self):
        return '(%s)' % (' '.join(str(x) for x in self.children))

    def __hash__(self):
        return hash(self.children)

    def __eq__(self, other):
        return isinstance(other, Expression) and other.children == self.children

    def cnf(self, parent = None):
        return CNF({
            CNFDisjunction({
                CNFTerm(self, True)
            })
        })

class Constant:
    _id = 0
    def __init__(self, name):
        Constant._id += 1
        self.id = Constant._id
        self.name = name

    def substitute(self, mapping):
        return self

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return isinstance(other, Constant) and other.id == self.id

class Variable:
    _id = 0
    def __init__(self, name):
        Variable._id += 1
        self.id = Constant._id
        self.name = name

    def substitute(self, mapping):
        if self in mapping:
            return mapping[self]
        return self

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return isinstance(other, Variable) and other.id == self.id

# First order logic that can be turned into cnf
class Implication(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __hash__(self):
        return hash((self.left, self.right))

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __str__(self):
        return '(%s \u21D2 %s)' % (str(self.left), str(self.right))

    def cnf(self, parent = None):
        return Disjunction(Negation(self.left), self.right).cnf(parent)

class Disjunction(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __hash__(self):
        return hash((self.left, self.right))

    def substitute(self, mapping):
        return Disjunction(self.left.substitute(mapping), self.right.substitute(mapping))

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __str__(self):
        return '(%s \u2228 %s)' % (str(self.left), str(self.right))

    def cnf(self, parent = None):
        left_cnf = self.left.cnf(parent)
        right_cnf = self.right.cnf(parent)

        final_set = set()

        # Distributive law
        for x in left_cnf.disjunctions:
            for y in right_cnf.disjunctions:
                final_set.add(x.join(y))

        return CNF(final_set)

class Conjunction(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __hash__(self):
        return hash((self.left, self.right))

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __str__(self):
        return '(%s \u2227 %s)' % (str(self.left), str(self.right))

    def substitute(self, mapping):
        return Conjunction(self.left.substitute(mapping), self.right.substitute(mapping))

    def cnf(self, parent = None):
        left_cnf = self.left.cnf(parent)
        right_cnf = self.right.cnf(parent)

        return left_cnf.join(right_cnf)

class UniversalQuantifier(Expression):
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

    def substitute(self, mapping):
        return UniversalQuantifier(self.variable, self.expression.substitute(mapping))

    def __hash__(self):
        return hash((self.left, self.right))

    def __str__(self):
        return '\u2200%s.%s' % (str(self.variable), str(self.expression))

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def cnf(self, parent = None):
        return self.expression.cnf((self, parent))

class ExistentialQuantifier(Expression):
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

    def substitute(self, mapping):
        return ExistentialQuantifier(self.variable, self.expression.substitute(mapping))

    def __hash__(self):
        return hash((self.variable, self.expression))

    def __eq__(self, other):
        return self.variable == other.variable and self.expression == other.expression

    def __str__(self):
        return '\u2203%s.%s' % (str(self.variable), str(self.expression))

    def cnf(self, parent = None):
        replacement_expression = [
            Constant(self.variable.name + '_')
        ]

        while parent is not None:
            if isinstance(parent[0], UniversalQuantifier):
                replacement_expression.append(parent[0].variable)

            parent = parent[1]

        return self.expression.substitute({self.variable: Expression(replacement_expression)}).cnf()

class Negation(Expression):
    def __init__(self, term):
        self.term = term

    def substitute(self, mapping):
        return Negation(self.term.substitute(mapping))

    def __hash__(self):
        return hash(self.term)

    def __eq__(self, other):
        return self.term == other.term

    def __str__(self):
        return '\u00AC%s' % (str(self.term),)

    def cnf(self, parent = None):
        if isinstance(self.term, Implication):
            return Conjunction(self.term.left, Negation(self.term.right)).cnf(parent)
        elif isinstance(self.term, Disjunction):
            return Conjunction(Negation(self.term.left), Negation(self.term.right)).cnf(parent)
        elif isinstance(self.term, Conjunction):
            return Disjunction(Negation(self.term.left), Negation(self.term.right)).cnf(parent)
        elif isinstance(self.term, Negation):
            return self.term.term.cnf(parent)
        elif isinstance(self.term, ExistentialQuantifier):
            return UniversalQuantifier(self.term.variable, Negation(self.term.expression)).cnf(parent)
        elif isinstance(self.term, UniversalQuantifier):
            return ExistentialQuantifier(self.term.variable, Negation(self.term.expression)).cnf(parent)
        else:
            return CNF({
                CNFDisjunction({
                    CNFTerm(self.term, False)
                })
            })

# A test:
eq = Constant('=')
plus = Constant('+')
a = Variable('a')
b = Variable('b')
expression = UniversalQuantifier(
    a,
    Implication(
        Expression((eq, a, Expression((plus, a, a)))),
        ExistentialQuantifier(
            b,
            Disjunction(
                Expression((eq, a, Expression((plus, b, b)))),
                Expression((eq, b, a))
            )
        )
    )
)

print(str(expression))
print(str(expression.cnf()))
