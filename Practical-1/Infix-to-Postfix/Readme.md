# Infix to Postfix Conversion with Right-to-Left Associativity for Exponentiation
## Theory
Infix expressions, such as `a + b * c ^ d ^ e`, are the common way of writing mathematical formulas. However, computers prefer working with **postfix notation** (Reverse Polish Notation, RPN), where the operator follows the operands (e.g., `a b c d e ^ ^ * +`). This eliminates the need for parentheses and operator precedence rules when evaluating expressions.

This program converts an **infix expression** (with operators `+`, `-`, `*`, `/`, and `^` for exponentiation) to **postfix notation**, ensuring:
1. **Operator precedence**: The program correctly handles operator precedence such that higher precedence operators (like `*`, `/`, `^`) are evaluated before lower precedence ones (like `+`, `-`).
2. **Associativity**: The program correctly handles the **right-to-left associativity** of the `^` operator, which means `a^b^c` is interpreted as `a^(b^c)`.
### Key Concepts:
1. **Operator Precedence**: Operators with higher precedence (e.g., `^`, `*`, `/`) are evaluated before operators with lower precedence (e.g., `+`, `-`).
2. **Associativity**: Operators like `^` are **right-associative**, meaning in expressions like `a^b^c`, the evaluation starts from the right (`b^c` before `a^(b^c)`).
3. **Postfix Notation**: In postfix, operators come after their operands, eliminating the need for parentheses. This makes it easier for machines to evaluate the expression.
---

## Steps

The program follows these steps to convert an infix expression to postfix notation:

1. **Initialize a Stack**: A stack is used to temporarily hold operators and parentheses as we process the expression.
2. **Iterate through the Expression**: Each character in the infix expression is processed one at a time.
   - **Operands (Numbers/Variables)**: If the character is an operand (a number or variable), it is immediately added to the output.
   - **Left Parenthesis `(`**: If the character is `(`, it is pushed onto the stack to indicate that a subexpression begins.
   - **Right Parenthesis `)`**: If the character is `)`, the stack is popped until a left parenthesis `(` is encountered, printing the operators in between.
   - **Operators (`+`, `-`, `*`, `/`, `^`)**: Operators are handled based on their precedence and associativity:
     - If the operator has a higher precedence than the top of the stack, it is pushed onto the stack.
     - If the operator has lower or equal precedence, operators are popped from the stack until an operator with lower precedence is found, respecting the associativity of the operators.
3. **Pop Remaining Operators**: Once the entire expression has been processed, any remaining operators in the stack are popped to the output.

### Functions:
- `push(char x)`: Adds an operator or parenthesis to the stack.
- `pop()`: Removes and returns the top element from the stack.
- `priority(char x)`: Returns the precedence of an operator.
- `isRightAssociative(char x)`: Checks if the operator has right-to-left associativity (e.g., `^`).

---

## Example Walkthrough

**Input**:
```
a+b*c^d^e
```

### Step-by-Step Conversion:

1. **Operands**: `a`, `b`, `c`, `d`, and `e` are added directly to the output.
2. **Operators**:
   - First, `+` is pushed onto the stack.
   - Then `*` is pushed, as it has higher precedence than `+`.
   - `^` is then pushed twice, as it has higher precedence than `*` and right-to-left associativity.
3. **Parentheses**: No parentheses are in the input, so this step is skipped.
4. **Final Output**: After processing all characters, the remaining operators in the stack are popped, resulting in the postfix notation:  
   `a b c d e ^ ^ * +`

### Output:
```
a b c d e ^ ^ * + 
```

---

## Code Explanation

```c
#include <stdio.h>
#include <ctype.h>

char stack[100];
int top = -1;

// Push operation to stack
void push(char x)
{
    stack[++top] = x;
}

// Pop operation from stack
char pop()
{
    if (top == -1)
        return -1;  // Return -1 if stack is empty
    else
        return stack[top--];
}

// Function to return priority of operators
int priority(char x)
{
    if (x == '(')
        return 0;
    if (x == '+' || x == '-')
        return 1;
    if (x == '*' || x == '/')
        return 2;
    if (x == '^')  // Exponentiation has the highest precedence
        return 3;
    return 0;
}

// Function to handle associativity of operators
int isRightAssociative(char x)
{
    if (x == '^')  // '^' is right associative
        return 1;
    return 0;  // Other operators are left associative
}

int main()
{
    char exp[100];
    char *e, x;
    printf("Enter the expression: ");
    scanf("%s", exp);
    printf("\n");

    e = exp;
    while (*e != '\0')  // Iterate through the expression
    {
        if (isalnum(*e))  // If the character is a number or letter, print it (operand)
            printf("%c ", *e);
        else if (*e == '(')  // If it's '(', push to stack
            push(*e);
        else if (*e == ')')  // If it's ')', pop till '(' is encountered
        {
            while ((x = pop()) != '(')
                printf("%c ", x);
        }
        else  // For operators
        {
            // Check the precedence and associativity
            while (top != -1 && 
                   ((priority(stack[top]) > priority(*e)) || 
                   (priority(stack[top]) == priority(*e) && !isRightAssociative(*e))))
            {
                printf("%c ", pop());
            }
            push(*e);  // Push the current operator to the stack
        }
        e++;
    }

    // Pop remaining operators from the stack
    while (top != -1)
    {
        printf("%c ", pop());
    }

    return 0;
}
```

---

## Conclusion

This program efficiently converts infix expressions to postfix notation, handling operator precedence and associativity correctly. Specifically, it ensures that the `^` operator is treated as right-associative, which is crucial for expressions involving exponentiation (e.g., `a^b^c` is evaluated as `a^(b^c)`). This approach simplifies expression evaluation and is useful for applications like calculators and compilers.
