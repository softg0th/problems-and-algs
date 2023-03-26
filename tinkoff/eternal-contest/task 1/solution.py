def calculate(lst):
    a, b, c, d = lst[0], lst[1], lst[2], lst[3]
    if d > b:
        plus = d - b
        amount = c * plus
        output = a + amount
        return output
    else:
        return a


def interface():
    data = input()
    data = data.split(' ')
    dt = []
    for i in data:
        if i != '':
            dt.append(i)
    dt = [int(x) for x in dt]
    output = calculate(dt)
    print(output)


if __name__ == '__main__':
    interface()
