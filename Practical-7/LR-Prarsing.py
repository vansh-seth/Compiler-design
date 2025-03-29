class LRParser:
    def __init__(self, grammar, action_table, goto_table):
        self.grammar = grammar
        self.action_table = action_table
        self.goto_table = goto_table
        self.stack = []
        self.input = []

    def parse(self, input_string):
        self.input = list(input_string) + ['$']
        self.stack = [0]

        while True:
            state = self.stack[-1]
            current_symbol = self.input[0]
            if current_symbol in self.action_table[state]:
                action = self.action_table[state][current_symbol]

                if action == 'accept':
                    print("Input Accepted!")
                    return True

                elif action.startswith('shift'):
                    next_state = int(action.split()[1])
                    self.stack.append(current_symbol)
                    self.stack.append(next_state)
                    self.input.pop(0)
                    print(f"Shifted to state {next_state}. Stack: {self.stack}")
                
                elif action.startswith('reduce'):
                    production = action.split()[1]
                    non_terminal = production.split('→')[0]
                    length = len(self.grammar[non_terminal][0])
                    self.stack = self.stack[:-length * 2]
                    goto_state = self.goto_table[self.stack[-1]][non_terminal]
                    self.stack.append(non_terminal)
                    self.stack.append(goto_state)
                    print(f"Reduced using {production}. Stack: {self.stack}")
            
            else:
                print("Error in parsing. No valid action found.")
                return False


grammar = {
    'S': ['AA'],
    'A': ['a']
}

action_table = {
    0: {'a': 'shift 1'},
    1: {'a': 'shift 2'},
    2: {'$': 'accept'},
}

goto_table = {
    0: {'A': 2},
    1: {},
    2: {'A': 1},
}

parser = LRParser(grammar, action_table, goto_table)
parser.parse("aa")
