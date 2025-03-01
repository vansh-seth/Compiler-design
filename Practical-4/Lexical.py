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
