from cnf import *
from unify import *
from heapq import heappush, heappop

# Graph search to reach contradictions from a given set of axioms

# f is the heuristic, which takes f(a, b) where a and b are axioms
# axioms is the disjunction set (not the actual CNF object).
def reach_contradiction(axioms, f, initial_cost = (lambda x: 0), max_cost = 10):
    # Frontier of statements we could reach
    frontier = []
    visited = {}
    costs = {}

    # Shallow copy
    axioms = set(axioms)

    for a in axioms:
        costs[a] = initial_cost(a)
        visited[a] = None

    # Initial frontier
    used = set()
    for a in axioms:
        used.add(a)
        for b in axioms:
            if b not in used:
                reduction = a.reduce(b)
                for candidate in reduction:
                    if candidate not in visited:
                        visited[candidate] = (a, b)
                        costs[candidate] = f(a, b, candidate, costs)
                        heappush(frontier, (costs[candidate], candidate))

    # Frontier-expansion loop
    while True:
        cost, adding = heappop(frontier)

        #print('Popping (%d) (%s from %s, %s): %s' % (cost, hash(adding), hash(visited[adding][0]), hash(visited[adding][1]), str(adding)))

        if cost > max_cost:
            return None

        for a in axioms:
            reduction = a.reduce(adding)

            for candidate in reduction:
                # Return the history!
                if len(candidate.terms) == 0:
                    filtered_visited = {}

                    visited[candidate] = (a, adding)

                    def add_to_history(x):
                        if x not in filtered_visited:
                            filtered_visited[x] = visited[x]
                            if visited[x] is not None:
                                add_to_history(filtered_visited[x][0])
                                add_to_history(filtered_visited[x][1])

                    add_to_history(candidate)

                    return filtered_visited, candidate

                # Add to the frontier
                if candidate not in visited:
                    visited[candidate] = (a, adding)
                    costs[candidate] = f(a, adding, candidate, costs)
                    heappush(frontier, (costs[candidate], candidate))

def get_reasoning(filtered_visited, goal):
    visited_nodes = set()
    ordering = []

    # Topological sort
    def dfs(x):
        if x not in visited_nodes:
            visited_nodes.add(x)

            if filtered_visited[x] is not None:
                dfs(filtered_visited[x][0])
                dfs(filtered_visited[x][1])

            ordering.append(x)

    dfs(goal)

    return filtered_visited, ordering

def print_reasoning(reason_map, ordering):
    print('Suppose otherwise.')
    inverse_map = {}
    for i, statement in enumerate(ordering):
        inverse_map[statement] = i + 1

    for i, statement in enumerate(ordering):
        if reason_map[statement] is None:
            print('It is given that we have:')
            print('  %s [%d]' % (str(statement), i + 1))
        else:
            a, b = reason_map[statement]
            print('From [%d] and [%d] we have:' % (inverse_map[a], inverse_map[b]))
            print('  %s [%d]' % (str(statement), i + 1))

def check_proof(program):
    axioms, lines = program

    axioms = {x.canonicalize() for x in axioms.disjunctions}

    for line in lines:
        '''
        print('BEGIN. AXIOMS ARE:')
        for axiom in axioms:
            print(str(axiom), hash(axiom))

        print('AND MY NULL HYPOTHESES ARE:')
        for axiom in Negation(line).cnf().disjunctions:
            print(str(axiom.canonicalize()), hash(axiom.canonicalize()))
        '''

        reasoning, contradiction = reach_contradiction(
            axioms | {x.canonicalize() for x in Negation(line).cnf().disjunctions},
            (lambda a, b, r, c: c[a] + c[b] + 1 if (a in axioms) != (b in axioms) else c[a] + c[b] + 2),
            lambda x: 0#(lambda x: 0 if x in axioms else -10),
        )
        reasoning, order = get_reasoning(reasoning, contradiction)
        print_reasoning(reasoning, order)

        axioms |= {x.canonicalize() for x in line.cnf().disjunctions}

    return True

if __name__ == '__main__':
    from parse import *

    program = parse_program(open('test_program.txt', 'r').read())
    check_proof(program)
