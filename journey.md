Automated Theorem Proving in Four Steps
=======================================
*A Novice's Journey To Writing an Automated Theorem Prover*

Automated theorem provers have a super fancy name but are, fundamentally, really simple systems. Most modern therorem provers follow this design pattern, except 

Step One: Conjunctive Normal Form (CNF)
---------------------------------------

First: there are a lot of different logical symbols, and a lot of different reduction and rewrite rules for propositional expressions. Their complexity and composability makes them difficult to work with, so we're here going to present a simple canonical form to which we can reduce all logical expressions. This form is called **conjunctive normal form** (CNF), and takes the following form:

```
forall a,b,c,d... (A or B or C or D ..) and (E or F or G or H ..) and ..
```

Where each A, B, C, etc. are expressions that contain no propositional operators except for possibly `~` (not).

The rules for reducion are as follows.

First, turn all implications into "or" expressions like so:
```
a => b ---> ~a or b

The expression should now consist only of `or`s and `and`s, with nots and quantifiers spread between. Bubble up the `and`s to the top by the distributive law:
```
(a and b) or c --> (a or c) and (b or c)
```

Move quantifiers to the outside:
```
((forall a. a) and b) --> forall a. (a and b)
((forall a. a) or b) --> forall a. (a or b)
((exists a. a) and b) --> forall a. (a and b)
((exists a. a) or b) --> forall a. (a or b)
~(forall a. a) --> exists a. ~a
~(exists a. a) --> forall a. ~a
```
Note that quantifiers change sign whenever they bubble through a `~`.

Now **skolemize** all of the existential quantifiers. `forall b. exists a. b(a)` means "for all b, there is at least one a such that b(a)." We can rewrite this using a new function `q` and saying `forall a. b(q(a))`. This implies the existential statement, since obviously if `b(q(a))` then `q(a)` is the element that satisfies the existence proposition. The existential statement also implies that such a function `q` exists, as we can construct `q` by just taking one such `b` for each input `a`. Thus the statements are equivalent.

Now our entire theory can be expressed in a form with finite depth and lots of structure. Every theory is:
  - a conjunction
  - of disjunctions
  - of negations or non-negations
  - of literals

With only universal quantifiers.

Step Two: Unification
---------------------

We will frequently have a statement like:

`x + y = y + x`

And we want to combine this with a statement like, say:

`a = b => b = a`

(or in cnf, we would have `~(a = b) or (b = a)`) and produce:

`y + x = x + y`

This requires knowing that we can substitute `x + y` in for `a` and `y + x` in for `b`. The process of detecting this substitution is called **unification**. In general, unification is taking two statements `a` and `b` and determining a substitution `u(a, b)` such that `u(a, b)(a) = u(a, b)(b)` (where we consider a substitution to be a function). There are many such substitutions, obviously; we want the **most general unifier** (**mgu**), meaning every other substitution factors through it: `forall u. u(a, b)(a) = u(a, b)(b) => forall x. exists w. u(a, b)(x) = w(mgu(a, b)(x))`.

There are some linear-time algorithms to compute the most general unifier, but usually these are not used, because they have large constant terms and are slow for the small expressions and easy substitutions we usually see in proofs. Instead, we use the more general, but exponential-time, algorithm that follows:

```
to compute the mgu of a and b:
    initialize an identity mapping
    compute the disagreement set (x, y) of a and b (see below)
    if it is empty return mapping
    if x is just a variable and y doesn't contain x
        add to the mapping: x -> y
    otherwise
        return failure
    apply the mapping to a and b

to compute the disagreement set of a and b:
    if a and b are equal return the empty set
    if a and b are different lengths return failure
    find the first child index i of a and b at which they aren't equal
    if a[i] or b[i] is an atom then return {a[i], b[i]}
    return the disagreement set of a[i] and b[i]
```

You are welcome to try one of the other mgu algorithms but it generally does not improve performance.

Step Three: Binary Reduction
----------------------------

It can be shown, though we won't do so here, that all logical inference rules in intuitionistic logic can be reduced to combinations of the following rule:

```
    (x or a or b or c ..) and (~x or p or q or j ..)
--> (a or b or c or p or q or j ..)
```

In other words, we take two statements, one which says "X or A", the other of which says "Not-X or B", and conclude that either something in A or something in B must be true, since if they were both false then we would have both X and not-X, which doesn't work.

This is not the only rule that can generate all of logic, but it is convenient because in many common cases it is exactly the modus ponens:

```
        (a => b) and a
cnf --> (~a or b) and a
red --> b
```

We need to extend this rule, however, to account for our quantified variables and unification. In the binary reduction rule, it is unlikley we will have `x` and `~x` exactly; more likely, we will have some `x1` and `x2` that **unify** to `x` and `~x`. The binary reduction rule, then, would be:
```
    (x1 or a or b or c ..) and (x2 or p or q or j ..)
--> mgu(x1, x2)(a or b or c or p or q or j ..)
```
Whenever that mgu exists.

Step Four: Graph Search
-----------------------

Finally, the fun part. Suppose we have some axioms (where each axiom is a **disjunction** of literals) and a goal `g`. We prove the goal `g` by contradiction. To do so, we add `~g` to the axiom set. Then we take several steps. At every step, we select some pair of axioms in the axiom list, do binary reduction, and add the result as an axiom. If we produce the empty set, we have reached a contradiction (the empty set an only be produced by the binary reduction of `a` and `~a`), and the goal is proven.

If the goal is false, then it can be disproven by adding `g` to the axiom list and trying to reach a contradiction. If we are trying to prove-or-disprove we can simply do this in parallel.

Godel's completeness and incompleteness theorems tell us about the properties of this algorithm. Godel's completeness theorem says that if our selection process is *fair*, then we will, given infinite time, prove any provable theorem. A selection process is *fair* if it has the property any pair of axioms in the axiom list will eventually be chosen for reduction. "Always choose the last two axioms," for instance, is not fair, whereas "choose the two axioms we haven't reduced yet that required in total the least number of reductions to produce" is fair. Intuitively, we are searching for a proof on an countably infinite graph. If your graph search algorithm is bfs-like, then any point in this graph will eventually be reached given enough time. But if it is dfs-like, then because the graph is infinite you might go off into infinity and never return.

Godels' incompletness theorem says that some statements can be neither proven nor disproven. That is to say, there are some statements whose truth value is *independent* of the axioms given. For these statements, the proof process will not terminate.

There are many different fair selection algorithms. For instance, the following algorithm, with any suitable metric function, is fair:
  - Assign each axiom a cost
  - When creating a new axiom `c` as the reduction of `a` and `b`, use some metric function `f` to assign a cost `cost(c) = f(a, b, c)`. To preserve fairness, the function should have the following property:
        `exists min > 0. f(a, b) - max(cost(a), cost(b)) >= min`
  - At each step, choose the pairing that generates the axiom with lowest cost.

This is essentially a modified Dijkstra's algorithm. Accordingly, it can be made more effective by using a frontier and adding axioms to the axiom list from the frontier, rather than adding the immediately. This algorithm can easily be shown to be fair because there are a finite number of axioms with each cost, so the waiting time for an axiom to be added to the axiom set is at most the number of axioms with lesser or equal cost, which is finite. To see that there are a finite number of axioms at each cost, note that if an axiom's cost is `x` then it can only have required at most `x / min` reductions to get to that axiom. That there are a finite number of axioms that take at most `x / min` reductions to reach is obvious -- each corresponds to a sequence of `x / min` pairs of indices less than `x / min` specifying which axioms to reduce.

You can use this fact to create a proof system that finds proofs for most "seen-in-the-wild" statements much faster than naive bfs. Common metric function heuristics include:
  - Penalize statements with lots of clauses, i.e. prefer `(a or b)` to `(a or b or c or d)`
  - Penalize statements with large expression trees
  - Favor the goal expression

To speed up the algorithm, it is also usually useful to make sure you're not adding redundant statements to the knowledge base. Obviously all new statements are redunant in the logical sense, but some statements are redundant for the purposes of our graph search; `a or b` is redudant if we already have `a`, because in order to get to the empty clause we have to eliminate both `b` and `a` anyway, so the second will strictly get there faster. This process technically makes the graph search not "fair," but we can still prove that we will eventually reach the empty clause if it is reacahble, even though we might not reach every reachable clause (which is what the completeness theorem was saying). The process of eliminating redundant clauses is called **subsumption**. A fast way to determine subsumption is to blah blah blah #TODO
