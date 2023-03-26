import sys

source = input()
stack = []

table = {'[': ']', '(': ')', '{': '}'}


for bracket in source:
    if bracket in table.keys():
        stack.append(bracket)

    if bracket in table.values():
        if len(stack) == 0:
            print('no')
            sys.exit()
        if table[stack[-1]] != bracket:
            print('no')
            sys.exit()
        else:
            stack.pop()

if len(stack) == 0:
    print('yes')

else:
    print('no')
