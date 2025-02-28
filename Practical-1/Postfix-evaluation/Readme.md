# Postfix Expression Evaluator

## Theory

Postfix notation (also known as Reverse Polish Notation, or RPN) is a mathematical notation in which every operator follows all of its operands. This means that the operator is placed after the operands, unlike infix notation where operators are placed between operands (e.g., `2 + 3`).

For example:
- Infix: `3 + 5`
- Postfix: `3 5 +`

In postfix notation, there is no need for parentheses to define operation order, as the order of operations is determined by the position of the operators in relation to the operands.

This program evaluates postfix expressions using a stack data structure. The general idea is to read the expression from left to right, push operands onto the stack, and for each operator, pop the operands, perform the operation, and push the result back onto the stack.

## Steps

### 1. **Input Parsing:**
   - The program reads the entire postfix expression input from the user, which may include multi-digit numbers.
   - The expression is processed one character at a time.

### 2. **Processing the Expression:**
   - **If the character is a digit:** It is converted to an integer and pushed onto the stack.
   - **If the character is an operator (+, -, *, /):** The two topmost operands are popped from the stack, the operation is performed, and the result is pushed back onto the stack.

### 3. **Evaluating the Result:**
   - Once all characters in the expression are processed, the remaining value in the stack is the final result of the postfix expression.

### 4. **Output:**
   - The program prints the result of the postfix expression evaluation.

### 5. **Handling Multi-Digit Numbers:**
   - The program is designed to handle multi-digit numbers by reading the full number until a non-digit character is encountered.

## Example Walkthrough

### Input:
```
Enter the postfix expression: 10 3 5 * + 2 -
```

**Steps:**
1. Push `10` onto the stack.
2. Push `3` onto the stack.
3. Push `5` onto the stack.
4. Encounter `*`:
   - Pop `5` and `3`, perform `3 * 5 = 15`, push `15`.
5. Encounter `+`:
   - Pop `15` and `10`, perform `10 + 15 = 25`, push `25`.
6. Push `2` onto the stack.
7. Encounter `-`:
   - Pop `2` and `25`, perform `25 - 2 = 23`, push `23`.

### Output:
```
Result = 23
```

---

## Code Explanation

### 1. **Push and Pop Functions:**
   - The `push` function adds an element to the top of the stack.
   - The `pop` function removes the top element from the stack and returns it.

### 2. **Operator Check:**
   - The `is_operator` function checks if a given character is an operator (i.e., `+`, `-`, `*`, `/`).

### 3. **Expression Evaluation:**
   - The `evaluate` function iterates through the postfix expression. It processes numbers by constructing them from digits and applies operators by popping operands from the stack and pushing results.

### 4. **Input Handling:**
   - The `scanf` function with the format specifier `"%[^\n]%*c"` reads the entire line, allowing multi-digit numbers and spaces between operands.

---

## Conclusion

This C program successfully evaluates postfix expressions using a stack. It can handle multi-digit numbers and perform basic arithmetic operations (`+`, `-`, `*`, `/`). The algorithm follows the principle of using a stack to store operands and apply operators in the correct order.

### Possible Improvements:
- Support for more complex operations such as modulus (`%`) or exponentiation (`^`).
- Handling of invalid input (e.g., mismatched operands and operators).
- Support for floating-point numbers.

