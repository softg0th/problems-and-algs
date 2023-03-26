import re
import sys
from collections import deque

dq = deque()


def find_num(s):
    ret = re.findall('[0-9]+', s)
    if '-' in s:
        return int(f'-{ret[0]}')
    return int(ret[0])


def push_front(x):
    dq.appendleft(x)
    print('ok')


def push_back(x):
    dq.append(x)
    print('ok')


def pop_front():
    if len(dq) != 0:
        print(dq.popleft())
    else:
        print('error')


def pop_back():
    if len(dq) != 0:
        print(dq.pop())
    else:
        print('error')


def front():
    if len(dq) != 0:
        print(dq[0])
    else:
        print('error')


def back():
    if len(dq) != 0:
        print(dq[-1])
    else:
        print('error')


def size():
    print(len(dq))


def clear():
    dq.clear()
    print('ok')


def exit():
    print('bye')
    sys.exit()


while True:
    com = input()
    if 'push_back' in com:
        data = find_num(com)
        push_back(int(data))

    if 'push_front' in com:
        data = find_num(com)
        push_front(int(data))

    if com == 'pop_back':
        pop_back()

    if com == 'pop_front':
        pop_front()

    if com == 'front':
        front()

    if com == 'back':
        back()

    if com == 'size':
        size()

    if com == 'clear':
        clear()

    if com == 'exit':
        exit()
