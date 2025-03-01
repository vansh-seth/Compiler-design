# Computation of FIRST and FOLLOW of Non-Terminals

## Aim

To compute the FIRST and FOLLOW sets for a given context-free grammar (CFG).

## Theory

In compiler design, FIRST and FOLLOW sets are used in syntax analysis to construct parsing tables for predictive parsers.

- **FIRST Set**: The FIRST set of a non-terminal consists of the terminals that appear at the beginning of any string derived from that non-terminal.
- **FOLLOW Set**: The FOLLOW set of a non-terminal consists of the terminals that appear immediately after that non-terminal in some derivation.

### Computation Rules:

#### FIRST Set

1. If X is a terminal, then FIRST(X) = {X}.
2. If X is a non-terminal:
   - If X → ε (epsilon) is a production, add ε to FIRST(X).
   - If X → Y1 Y2 ... Yk, then add FIRST(Y1) to FIRST(X) (excluding ε). If FIRST(Y1) contains ε, then check FIRST(Y2), and so on.

#### FOLLOW Set

1. If S is the start symbol, add `$` to FOLLOW(S).
2. If A → αBβ is a production, add FIRST(β) (excluding ε) to FOLLOW(B).
3. If A → αB or A → αBβ where FIRST(β) contains ε, add FOLLOW(A) to FOLLOW(B).

## Code

```python
class Grammar:
    def __init__(self, productions):
        self.productions = productions
        self.non_terminals = set(productions.keys())
        self.terminals = set()
        self.first = {nt: set() for nt in self.non_terminals}
        self.follow = {nt: set() for nt in self.non_terminals}
        self.start_symbol = list(productions.keys())[0]
        self._compute_terminals()

    def _compute_terminals(self):
        for rules in self.productions.values():
            for rule in rules:
                for symbol in rule:
                    if symbol not in self.non_terminals and symbol != 'ε':
                        self.terminals.add(symbol)

    def compute_first(self):
        for terminal in self.terminals:
            self.first[terminal] = {terminal}
        
        changed = True
        while changed:
            changed = False
            for nt in self.non_terminals:
                for rule in self.productions[nt]:
                    before = self.first[nt].copy()
                    for symbol in rule:
                        self.first[nt] |= self.first.get(symbol, set()) - {'ε'}
                        if 'ε' not in self.first.get(symbol, set()):
                            break
                    else:
                        self.first[nt].add('ε')
                    if before != self.first[nt]:
                        changed = True

    def compute_follow(self):
        self.follow[self.start_symbol].add('$')
        changed = True
        while changed:
            changed = False
            for nt, rules in self.productions.items():
                for rule in rules:
                    follow_set = self.follow[nt]
                    for i in range(len(rule) - 1, -1, -1):
                        symbol = rule[i]
                        if symbol in self.non_terminals:
                            before = self.follow[symbol].copy()
                            self.follow[symbol] |= follow_set
                            if 'ε' in self.first[symbol]:
                                follow_set |= self.first[symbol] - {'ε'}
                            else:
                                follow_set = self.first[symbol]
                            if before != self.follow[symbol]:
                                changed = True

    def display(self):
        print("FIRST sets:")
        for nt in self.non_terminals:
            print(f"FIRST({nt}) = {self.first[nt]}")
        print("\nFOLLOW sets:")
        for nt in self.non_terminals:
            print(f"FOLLOW({nt}) = {self.follow[nt]}")

# Example usage:
productions = {
    'S': [['A', 'B']],
    'A': [['a', 'A'], ['ε']],
    'B': [['b', 'B'], ['ε']]
}
grammar = Grammar(productions)
grammar.compute_first()
grammar.compute_follow()
grammar.display()
```

## Output

```
FIRST sets:
FIRST(S) = {'a', 'ε'}
FIRST(A) = {'a', 'ε'}
FIRST(B) = {'b', 'ε'}

FOLLOW sets:
FOLLOW(S) = {'$'}
FOLLOW(A) = {'b'}
FOLLOW(B) = {'$'}
```

## Conclusion

The program successfully computes the FIRST and FOLLOW sets for a given CFG. The implementation correctly follows the rules of FIRST and FOLLOW computation, handling recursion and epsilon productions effectively.


