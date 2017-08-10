from cnf import *

# Unify two EXPRESSIONS.
def unify(a, b):
    mapping = {v: v for v in set(a.get_all_variables()) | set(b.get_all_variables())}

    while True:
        disagreement = disagreement_set(a, b)

        if disagreement is None:
            return None

        elif disagreement == ():
            return mapping

        elif isinstance(disagreement[0], Variable):
            if disagreement[0] in disagreement[1].get_all_variables():
                return None

            insert_into_mapping(mapping, disagreement[0], disagreement[1])
            a = a.substitute({disagreement[0]: disagreement[1]})
            b = b.substitute({disagreement[0]: disagreement[1]})

        elif isinstance(disagreement[1], Variable):
            if disagreement[1] in disagreement[0].get_all_variables():
                return None
            insert_into_mapping(mapping, disagreement[1], disagreement[0])
            a = a.substitute({disagreement[1]: disagreement[0]})
            b = b.substitute({disagreement[1]: disagreement[0]})

        else:
            return None

def disagreement_set(a, b):
    if isinstance(a, Expression) and isinstance(b, Expression):
        if len(a.children) != len(b.children):
            return None
        for i, c in enumerate(a.children):
            disagreement = disagreement_set(c, b.children[i])
            if disagreement != ():
                return disagreement
        return ()
    elif a != b:
        return (a, b)
    else:
        return ()

def insert_into_mapping(mapping, a, b):
    for key in mapping:
        mapping[key] = mapping[key].substitute({a: b})

if __name__ == '__main__':
    a, b, c = Variable('a'), Variable('b'), Variable('c')
    d, e, f = Variable('d'), Variable('e'), Variable('f')
    print(unify(
        Expression((a, Expression((b, c)))),
        Expression((d, Expression((Expression((e, e)), Expression((d, f))))))
    ))
