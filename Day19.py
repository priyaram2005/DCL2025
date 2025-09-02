import math

def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(math.trunc(a / b))
            elif token == '^':
                stack.append(a ** b)
    return stack[0]

expr = input().strip()
print(evaluate_postfix(expr))
