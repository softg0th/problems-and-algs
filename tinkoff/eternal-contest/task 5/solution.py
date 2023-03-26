def repdigit(num):
    element = int(str(num)[0])
    while num > 0:
        digit = num % 10
        if int(digit) != element:
            return False
        num = num // 10
    return True


def calculate(lst):
    ans = 0
    for i in range(lst[0], lst[1]+1):
        if i < 10:
            ans += 1
            continue
        if repdigit(i) is True:
            ans += 1
    return ans


def interface():
    data = input()
    data = data.split()
    data = [int(i) for i in data]
    print(calculate(data))


if __name__ == '__main__':
    interface()
