import sys
from collections import deque
import re

queue = deque()


def find_num(s):
    ret = re.findall('[0-9]+', s)
    if '-' in s:
        return int(f'-{ret[0]}')
    return int(ret[0])


def push(x):
    queue.append(x)
    print('ok')


def pop():
    if len(queue) != 0:
        print(queue[0])
        queue.popleft()
    else:
        print('error')


def front():
    if len(queue) != 0:
        print(queue[0])
    else:
        print('error')


def size():
    print(len(queue))


def clear():
    queue.clear()
    print('ok')


def exit():
    print('bye')
    sys.exit()


while True:
    com = input()

    if 'push' in com:
        data = find_num(com)
        push(int(data))

    if com == 'pop':
        pop()

    if com == 'front':
        front()

    if com == 'size':
        size()

    if com == 'clear':
        clear()

    if com == 'exit':
        exit()
