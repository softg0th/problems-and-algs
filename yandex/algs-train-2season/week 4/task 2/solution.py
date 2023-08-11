def calcs(data):
    output = {}
    print(data)
    for element in data:
        if element[0] not in output.keys():
            output[element[0]] = element[1]
        else:
            output[element[0]] += element[1]
    for element in sorted(output):
        print(element, output[element])


def interface():
    dt = []
    while True:
        base = input()
        if base == '':
            break
        data = base.split()
        data = [data[0], int(data[1])]
        dt.append(data)
    calcs(dt)


if __name__ == '__main__':
    interface()
