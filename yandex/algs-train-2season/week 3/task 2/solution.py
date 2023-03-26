def check(data):
    storage = set()
    for i in data:
        if i not in storage:
            storage.add(i)
            print('NO')
        else:
            print('YES')


def interface():
    data = [int(s) for s in input().split()]
    check(data)


if __name__ == '__main__':
    interface()
