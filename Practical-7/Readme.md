
# LR Parsing

This repository provides an implementation of **LR Parsing**, a bottom-up parsing technique for context-free grammars. The LR parser uses **action** and **goto tables** to guide the parsing process, making it suitable for deterministic grammars, specifically those that fall under the **LR(0)** or **SLR(1)** categories.

## Features:
- **Shift and Reduce Actions**: Uses **shift** and **reduce** actions to parse input.
- **Action and Goto Tables**: Constructs action and goto tables based on the grammar.
- **Grammar Support**: Supports context-free grammars (CFGs) in a specific form (LR(0) or SLR(1)).
- **Step-by-Step Parsing**: Provides a detailed, step-by-step output of the parsing process for better debugging and understanding.

## How It Works:
1. **Shift**: If the current symbol on the input can be shifted to the stack (based on the action table), the parser moves it to the stack and transitions to the next state.
2. **Reduce**: If the current configuration matches a reduction rule in the action table, the parser reduces a series of symbols in the stack to the corresponding non-terminal.
3. **Accept**: If the parser reaches the final accepting state, the input is accepted as valid.
4. **Error**: If no valid action is found for the current state and symbol, the parser reports an error.

## Grammar Format:
The grammar must be provided in a dictionary format, where the keys represent non-terminal symbols, and the values represent lists of production rules.

### Example:
```python
grammar = {
    'S': ['AA'],
    'A': ['a']
}
```
This represents the following productions:
```
S → AA
A → a
```

## Example Usage:

### Step 1: Initialize the Parser with Grammar, Action Table, and Goto Table
```python
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
```

### Step 2: Parse the Input String
```python
parser.parse("aa")
```

### Output:
The parser will display the actions as it shifts and reduces symbols and will either accept the string or print an error message.

```plaintext
Shifted to state 1. Stack: [0, 'a', 1]
Shifted to state 2. Stack: [0, 'a', 1, 'a', 2]
Input Accepted!
```

---

## Handwritten Example:

Let’s walk through an example of how the **LR parsing** works with the following grammar:

### Grammar:
```
S → AA
A → a
```

### Step 1: Construct the **Action** and **Goto** Tables:
For this grammar, we need to build the **action** and **goto** tables based on the possible states of the parser.

#### Action Table:
The **action** table defines the actions (shift, reduce, accept) for each state and input symbol.

| State | a      | $    |
|-------|--------|------|
| 0     | shift 1|      |
| 1     | shift 2|      |
| 2     |        | accept|

- **State 0**: When we encounter `a`, we shift to state 1.
- **State 1**: When we encounter `a`, we shift to state 2.
- **State 2**: The parser reaches the accepting state, so it accepts when the input is complete (i.e., when `$` is encountered).

#### Goto Table:
The **goto** table defines the transitions for non-terminal symbols.

| State | A    |
|-------|------|
| 0     | 2    |
| 1     |      |
| 2     | 1    |

- **State 0**: If we encounter `A`, the parser moves to state 2.
- **State 2**: If we encounter `A`, the parser moves to state 1.

### Step 2: Parsing Process:
Let's parse the input string `"aa"` step by step.

#### Step 1: Initial State
- Stack: `[0]`
- Input: `["a", "a", "$"]`

We are in **State 0** and the next symbol is `a`. According to the **action table**, we perform a **shift** to state 1.

#### Step 2: After First Shift
- Stack: `[0, 'a', 1]`
- Input: `["a", "$"]`

We are in **State 1** and the next symbol is `a`. According to the **action table**, we perform a **shift** to state 2.

#### Step 3: After Second Shift
- Stack: `[0, 'a', 1, 'a', 2]`
- Input: `["$"]`

We are in **State 2** and the next symbol is `$`. According to the **action table**, we perform an **accept** since this is the accepting state.

### Final Output:
```plaintext
Shifted to state 1. Stack: [0, 'a', 1]
Shifted to state 2. Stack: [0, 'a', 1, 'a', 2]
Input Accepted!
```

---

## Functions:

- `parse(input_string)`: Initiates the parsing process. Parses the input string using the action and goto tables.
- `shift(state, symbol)`: Executes a shift operation, pushing the symbol and the next state onto the stack.
- `reduce(production)`: Executes a reduce operation based on the provided production.
- `display_parse_step()`: Displays the parsing steps and the current state of the stack and input string.
- `construct_action_table()`: Constructs the **action table** based on the grammar.
- `construct_goto_table()`: Constructs the **goto table** based on the grammar.

## Requirements:
- Python 3.x

## Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lr-parsing.git
   cd lr-parsing
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the parser script:
   ```bash
   python lr_parsing.py
   ```
