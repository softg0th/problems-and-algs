import sys


def find_num(s):
    word_list = s.split()
    st = ''
    for word in word_list[1]:
        if word.isnumeric():
            st += str(word)
    if '-' in word_list[1]:
        return f'-{st}'
    return int(st)


class Storage:
    stack = []


s = Storage()


def push(n):
    s.stack.append(n)
    print("ok")


def back():
    if len(s.stack) != 0:
        print(s.stack[-1])
    else:
        print("error")


def pop():
    if len(s.stack) != 0:
        print(s.stack[-1])
        s.stack.pop()
    else:
        print("error")


def size():
    print(len(s.stack))


def clear():
    s.stack = []
    print("ok")


def exit():
    print("bye")
    sys.exit()


while True:
    com = input()

    if 'push' in com:
        data = find_num(com)
        push(data)

    if com == 'pop':
        pop()

    if com == 'back':
        back()

    if com == 'size':
        size()

    if com == 'clear':
        clear()

    if com == 'exit':
        exit()
