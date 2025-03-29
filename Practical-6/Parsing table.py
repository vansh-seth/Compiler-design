class PredictiveParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.first_sets = {}
        self.follow_sets = {}
        self.parse_table = {}
        self.compute_first_sets()
        self.compute_follow_sets()
        self.construct_parse_table()

    def compute_first_sets(self):
        for non_terminal in self.grammar:
            self.first_sets[non_terminal] = self.first(non_terminal)

    def compute_follow_sets(self):
        for non_terminal in self.grammar:
            self.follow_sets[non_terminal] = self.follow(non_terminal)

    def first(self, symbol):
        if symbol in self.first_sets:  
            return self.first_sets[symbol]
        if symbol in self.grammar: 
            first_set = set()
            for production in self.grammar[symbol]:
                if production == 'ε': 
                    first_set.add('ε')
                else:
                    for char in production:
                        first_set |= self.first(char)
                        if 'ε' not in self.first_sets.get(char, set()):
                            break
            self.first_sets[symbol] = first_set
            return first_set
        return {symbol} 

    def follow(self, non_terminal):
        if non_terminal in self.follow_sets:  
            return self.follow_sets[non_terminal]
        follow_set = set()
        if non_terminal == 'S':  
            follow_set.add('$')
        for head, productions in self.grammar.items():
            for production in productions:
                if non_terminal in production:
                    idx = production.index(non_terminal)
                    if idx + 1 < len(production):
                        follow_set |= self.first(production[idx + 1])
                    elif head != non_terminal:
                        follow_set |= self.follow(head)
        self.follow_sets[non_terminal] = follow_set
        return follow_set

    def construct_parse_table(self):
        for non_terminal in self.grammar:
            self.parse_table[non_terminal] = {}
            for terminal in self.first_sets[non_terminal]:
                if terminal != 'ε':
                    for production in self.grammar[non_terminal]:
                        if production.startswith(terminal):
                            self.parse_table[non_terminal][terminal] = production
            if 'ε' in self.first_sets[non_terminal]:
                for terminal in self.follow_sets[non_terminal]:
                    self.parse_table[non_terminal][terminal] = 'ε'

    def display_parse_table(self):
        print("Parsing Table:")
        for non_terminal in self.parse_table:
            for terminal in self.parse_table[non_terminal]:
                print(f"M[{non_terminal}, {terminal}] = {self.parse_table[non_terminal][terminal]}")

grammar = {
    'S': ['Aa', 'b'],
    'A': ['c', 'ε']
}

parser = PredictiveParser(grammar)

parser.display_parse_table()
