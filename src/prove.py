from cnf import *
from unify import *
from heapq import heappush, heappop

# Graph search to reach contradictions from a given set of axioms

# f is the heuristic, which takes f(a, b) where a and b are axioms
# axioms is the disjunction set (not the actual CNF object).
def reach_contradiction(axioms, f, initial_cost = (lambda x: 0), max_n = 30000):
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

    max_cost_so_far = 0

    # Frontier-expansion loop
    while True:
        cost, adding = heappop(frontier)

        print('Cost %f, size %d' % (cost, len(visited)), end='\r', flush=True)

        if len(visited) > max_n:
            return None

        #print('Popping (%d) (%s from %s, %s): %s' % (cost, hash(adding), hash(visited[adding][0]), hash(visited[adding][1]), str(adding)))

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

def get_forward_reasoning(filtered_visited, goal, original):
    # Invert the table
    outputs = {}

    for key in filtered_visited:
        if filtered_visited[key] is not None:
            a, b = filtered_visited[key]

            if a not in outputs:
                outputs[a] = []
            outputs[a].append(key)

            if b not in outputs:
                outputs[b] = []
            outputs[b].append(key)

    # Check to see if there is a single thread of reasoning
    # from the beginning to the end
    node = original
    nodes_on_forward_chain = {goal}
    forward_chain = [goal]
    while node != goal:
        if len(outputs[node]) == 1:
            nodes_on_forward_chain.add(node)
            forward_chain.append(node)
            node = outputs[node][0]
        else:
            return None

    # There is!
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

    # Topological sort everything except for the forward chain
    if filtered_visited[goal][0] in nodes_on_forward_chain:
        dfs(filtered_visited[goal][1])
    else:
        dfs(filtered_visited[goal][0])

    return ordering, reversed(forward_chain)

def get_backward_reasoning(filtered_visited, goal):
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

def print_backward_reasoning(reason_map, ordering, axioms, original):
    print('Suppose for the sake of contradiction that:')
    print('  %s' % (str(CNF(original)),))
    inverse_map = {}
    for i, statement in enumerate(ordering):
        inverse_map[statement] = i + 1

    for i, statement in enumerate(ordering):
        if reason_map[statement] is None:
            print('By %s we have:' % (axioms[statement],))
            print('  %s [%d]' % (str(statement), i + 1))
        elif i == len(ordering) - 1:
            a, b = reason_map[statement]
            print('But [%d] and [%d] are contradictory. =><=' % (inverse_map[a], inverse_map[b]))
            print('')
        else:
            a, b = reason_map[statement]
            print('From [%d] and [%d] we have:' % (inverse_map[a], inverse_map[b]))
            print('  %s [%d]' % (str(statement), i + 1))

def check_proof(program):
    axioms, lines = program

    axioms = {x.canonicalize(): axioms[x] for x in axioms}

    for j, line in enumerate(lines):
        '''
        print('BEGIN. AXIOMS ARE:')
        for axiom in axioms:
            print(str(axiom), hash(axiom))

        print('AND MY NULL HYPOTHESES ARE:')
        for axiom in Negation(line).cnf().disjunctions:
            print(str(axiom.canonicalize()), hash(axiom.canonicalize()))
        '''

        disjunctions = {x.canonicalize(): 'our assumption' for x in Negation(line).cnf().disjunctions}

        tmp_axioms = set(axioms.keys())
        print('We now prove %s [result %d]' % (str(line), j + 1))

        ratio = sum(len(x.terms) for x in disjunctions)

        result = reach_contradiction(
            set(axioms.keys()) | set(disjunctions.keys()),
            (lambda a, b, r, c:
                c[a] + c[b] + len(r.terms) * 3.0 / ratio + 1 if (a in tmp_axioms) != (b in tmp_axioms)
                else c[a] + c[b] + len(r.terms) * 3.0 / ratio + 9.0 / ratio
                ),
            (lambda x: 0.0)
        )

        if result is not None:
            reasoning, contradiction = result

            if len(disjunctions) == 1 and False:
                disjunction = next(iter(disjunctions))
                forward_result = get_forward_reasoning(reasoning, contradiction, disjunction)
            else:
                reasoning, order = get_backward_reasoning(reasoning, contradiction)
                print_backward_reasoning(reasoning, order, {**axioms, **disjunctions}, disjunctions)
        else:
            print('')
            print('I do not understand how this follows.')
            print('')

        for x in line.cnf().disjunctions:
            axioms[x.canonicalize()] = 'result %d' % (j + 1,)

    return True

if __name__ == '__main__':
    from parse import *

    program = parse_program(open('test_program.txt', 'r').read())
    check_proof(program)
