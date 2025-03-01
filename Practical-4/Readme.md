# Lexical Analysis

## Aim
To implement a lexical analyzer that tokenizes a given input string or source code and identifies keywords, identifiers, operators, and other tokens.

## Theory
Lexical Analysis is the first phase of a compiler, where the source code is converted into a sequence of tokens. The lexical analyzer reads the input character stream and groups characters into meaningful lexemes, which are then mapped to corresponding token types.

### Key Components of Lexical Analysis:
- **Token:** The smallest unit of meaning, such as keywords, identifiers, literals, operators, and symbols.
- **Lexeme:** A sequence of characters that form a token.
- **Pattern:** A rule defining the structure of lexemes.

### Steps in Lexical Analysis:
1. Read the source code as an input.
2. Identify valid lexemes based on predefined patterns.
3. Assign corresponding tokens to the lexemes.
4. Generate a token stream as output for the next phase (Syntax Analysis).

## Code Implementation (Python)
```python
import re

def tokenize(code):
    tokens = []
    token_specification = [
        ('KEYWORD', r'\b(if|else|while|return|int|float|char)\b'),
        ('IDENTIFIER', r'[a-zA-Z_]\w*'),
        ('NUMBER', r'\b\d+(\.\d+)?\b'),
        ('OPERATOR', r'[+\-*/=<>]'),
        ('DELIMITER', r'[;(),{}]'),
        ('WHITESPACE', r'\s+'),
        ('UNKNOWN', r'.')
    ]
    
    token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    
    for match in re.finditer(token_regex, code):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type != 'WHITESPACE':
            tokens.append((token_type, token_value))
    
    return tokens

# Example Input Code
source_code = "int x = 10; if (x > 5) x = x + 1;"
tokenized_output = tokenize(source_code)

print("Tokenized Output:")
for token in tokenized_output:
    print(token)
```

## Sample Output
```
Tokenized Output:
('KEYWORD', 'int')
('IDENTIFIER', 'x')
('OPERATOR', '=')
('NUMBER', '10')
('DELIMITER', ';')
('KEYWORD', 'if')
('DELIMITER', '(')
('IDENTIFIER', 'x')
('OPERATOR', '>')
('NUMBER', '5')
('DELIMITER', ')')
('IDENTIFIER', 'x')
('OPERATOR', '=')
('IDENTIFIER', 'x')
('OPERATOR', '+')
('NUMBER', '1')
('DELIMITER', ';')
```

## Conclusion
The lexical analyzer successfully tokenized the input code by recognizing keywords, identifiers, operators, numbers, and delimiters. This forms the basis for the next phase of compilation, which is syntax analysis. The implementation demonstrates how regular expressions can be used for pattern matching in lexical analysis.


