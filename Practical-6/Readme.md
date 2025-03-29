Certainly! Here's an updated version of the `README.md` with a handwritten example added for better understanding.

---

# Predictive Parsing Table Construction

This repository provides an implementation of constructing a **Predictive Parsing Table** for **LL(1)** parsers. The **Predictive Parser** uses **FIRST** and **FOLLOW** sets to create a table that helps in parsing a given input string using a context-free grammar (CFG). This technique is commonly used in the design of top-down parsers for compilers.

## Features:
- **FIRST Set Calculation**: Computes the set of terminal symbols that appear at the beginning of any string derived from a given non-terminal.
- **FOLLOW Set Calculation**: Computes the set of terminal symbols that can follow a given non-terminal.
- **Parsing Table Construction**: Based on the **FIRST** and **FOLLOW** sets, constructs a parsing table for LL(1) parsing.
- **Grammar Support**: Supports context-free grammars (CFGs) where the grammar is defined using production rules.

## How It Works:
1. **FIRST Set**: For each non-terminal, the FIRST set is calculated based on the productions. It contains all the terminal symbols that can appear at the beginning of any string derived from the non-terminal.
2. **FOLLOW Set**: The FOLLOW set for a non-terminal is computed using the rules of grammar, which determine the set of terminals that can follow that non-terminal in any valid derivation.
3. **Parsing Table**: The parsing table is constructed by associating non-terminals with terminals and assigning the corresponding production rule from the grammar.

## Grammar Format:
The grammar is defined as a dictionary where the keys are non-terminal symbols and the values are lists of production rules.

### Example:
```python
grammar = {
    'S': ['Aa', 'b'],
    'A': ['c', 'ε']
}
```
Here, the grammar has two non-terminals `S` and `A`. The production rules for `S` are `Aa` and `b`. The production rule for `A` is `c`, or the empty string `ε` (epsilon).

## Example Usage:

### Step 1: Initialize the Parser with Grammar
```python
grammar = {
    'S': ['Aa', 'b'],
    'A': ['c', 'ε']
}

parser = PredictiveParser(grammar)
```

### Step 2: Compute and Display the Parsing Table
```python
parser.display_parse_table()
```

### Output:
The parser computes the **FIRST** and **FOLLOW** sets, and then constructs and displays the predictive parsing table.

```plaintext
Parsing Table:
M[S, c] = Aa
M[S, b] = b
M[A, c] = c
M[A, $] = ε
```

This table can then be used to parse strings and check if they conform to the grammar.

---

## Handwritten Example:

Let’s consider a grammar with two non-terminals `S` and `A`:

### Grammar:
```
S → Aa | b
A → c | ε
```

### Step 1: Compute the **FIRST** Set:
1. **FIRST(S)**: The productions for `S` are:
   - `S → Aa`: `FIRST(S)` will contain `FIRST(A)`.
   - `S → b`: `b` is a terminal, so add `b` to `FIRST(S)`.

   Now, calculate **FIRST(A)**:
   - `A → c`: `FIRST(A)` contains `c`.
   - `A → ε`: `ε` is included in `FIRST(A)`.

   So, we have:
   - **FIRST(S) = {a, b}**
   - **FIRST(A) = {c, ε}**

### Step 2: Compute the **FOLLOW** Set:
1. **FOLLOW(S)**: The start symbol `S` has `$` (end of input) in its FOLLOW set.
   
2. **FOLLOW(A)**: For production `S → Aa`, the terminal after `A` is `a`, so `a` goes into **FOLLOW(A)**. Since `A → ε` is a valid production, we also add **FOLLOW(S)** to **FOLLOW(A)**. Thus, **FOLLOW(A)** contains `$`.

   So, we have:
   - **FOLLOW(S) = {$}**
   - **FOLLOW(A) = {a, $}**

### Step 3: Construct the Predictive Parsing Table:

Now, we can construct the predictive parsing table based on the **FIRST** and **FOLLOW** sets. The table will have rows corresponding to non-terminals and columns corresponding to terminals and `$` (end of input).

| Non-terminal | c    | b    | a    | $    |
|--------------|------|------|------|------|
| S            |      | b    | Aa   |      |
| A            | c    |      |      | ε    |

- **M[S, c]**: Since `c` is in `FIRST(A)`, and `A → c` is a production for `S`, we place `Aa` in the table at `[S, c]`.
- **M[S, b]**: Since `b` is directly in the grammar production `S → b`, we place `b` in the table at `[S, b]`.
- **M[A, c]**: Since `A → c` is a valid production, we place `c` in the table at `[A, c]`.
- **M[A, $]**: Since `A → ε` is valid, and `$` is in **FOLLOW(A)**, we place `ε` in the table at `[A, $]`.

### Final Table:
```
Parsing Table:
M[S, c] = Aa
M[S, b] = b
M[A, c] = c
M[A, $] = ε
```

---

## Functions:

- `compute_first_sets()`: Computes the **FIRST** sets for all non-terminals in the grammar.
- `compute_follow_sets()`: Computes the **FOLLOW** sets for all non-terminals in the grammar.
- `construct_parse_table()`: Constructs the **parsing table** using the **FIRST** and **FOLLOW** sets.
- `display_parse_table()`: Displays the constructed parsing table.

## Requirements:
- Python 3.x

## Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/predictive-parsing-table.git
   cd predictive-parsing-table
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the parser script:
   ```bash
   python predictive_parsing.py
   ```
