def interface():
    n = int(input())
    nums = set(range(1, n + 1))
    while True:
        data = input()
        if data == 'HELP':
            break
        sets = {int(x) for x in data.split()}
        answer = input()
        if answer == 'YES':
            nums &= sets
        else:
            nums -= answer
    print(*nums)


if __name__ == '__main__':
    interface()
