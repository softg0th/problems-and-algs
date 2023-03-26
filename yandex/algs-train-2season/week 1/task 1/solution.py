def module(a, b, c):

    if b == 0:
        if c > 0:
            return 3
        return c

    if b == 1:
        return c

    if b == 4:
        if a != 0:
            return 3
        return 4

    if b == 6:
        return 0

    if b == 7:
        return 1

    return b


def interface():
    code = int(input())
    intercator = int(input())
    checker = int(input())
    result = module(code, intercator, checker)
    print(result)


if __name__ == '__main__':
    interface()
