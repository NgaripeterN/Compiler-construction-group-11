import re

# Token specification as (token type, regex pattern)
token_specification = [
    ('KEYWORD', r'\b(if|else|do|while|for|int|float|string)\b'),  # Keywords
    ('NUMBER', r'\b\d+(\.\d*)?\b'),  # Integer or float literals
    ('STRING', r'"[^"]*"'),  # String literals
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'),  # Identifiers
    ('OPERATOR', r'[=+\-*/><]'),  # Operators
    ('LPAREN', r'\('),  # Left parenthesis
    ('RPAREN', r'\)'),  # Right parenthesis
    ('LBRACE', r'\{'),  # Left brace
    ('RBRACE', r'\}'),  # Right brace
    ('SEMICOLON', r';'),  # Semicolon
    ('WHITESPACE', r'\s+'),  # Whitespace (ignored)
    ('MISMATCH', r'.'),  # Any other character (error)
]

# Example Zara code to tokenize
zara_code = '''
int x = 10;
float y = 20.5;
if (x > y) {
    x = x * 2;
} else {
    y = y / 2;
}
'''

# Create a master regex by combining all token patterns
master_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})'
                        for pair in token_specification)

# Compile the regex
token_regex = re.compile(master_regex)


# Tokenizer function
def tokenize(code):
    tokens = []
    for match in token_regex.finditer(code):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type == 'WHITESPACE':
            continue  # Ignore whitespace
        elif token_type == 'MISMATCH':
            raise SyntaxError(f"Unexpected character: {token_value}")
        tokens.append((token_type, token_value))
    return tokens


# Tokenize Zara code
tokens = tokenize(zara_code)

# Output the tokens
for token in tokens:
    print(token)
