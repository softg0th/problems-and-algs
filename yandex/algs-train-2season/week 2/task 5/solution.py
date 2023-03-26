def calc(lst):
    maximum = max(lst)
    count = 0
    for el in lst:
        count += el
    return count-maximum


def interface():
    count = int(input())
    data = input()
    dat = data.split(' ')
    dt = []
    for i in dat:
        dt.append(int(i))
    print(calc(dt))


if __name__ == '__main__':
    interface()
