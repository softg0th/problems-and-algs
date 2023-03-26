import re


def calc(op, a, b):
    if op == "*":
        return a * b
    elif op == "/":
        return a / b
    elif op == "+":
        return a + b
    else:
        return a - b


stdin = input()
stack = []
regex = '^\d{1,}$'
digits = []
operands = ['+', '-', '*', '/']

for sign in stdin:
    if re.match(regex, sign):
        stack.append(int(sign))

    if sign in operands:
        a = stack.pop()
        b = stack.pop()
        numb = calc(sign, b, a)
        stack.append(numb)

print(stack[0])
