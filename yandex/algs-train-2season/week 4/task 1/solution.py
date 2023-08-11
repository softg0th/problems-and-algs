def calcs(data):
    output = {}
    for element in data:
        if element[0] not in output.keys():
            output[element[0]] = element[1]
        else:
            output[element[0]] += element[1]
    for element in sorted(output):
        print(element, output[element])


def interface():
    count = int(input())
    datas = []

    for i in range(count):
        dt = input()
        dt = dt.split()
        key, value = int(dt[0]), int(dt[1])
        datas.append([key, value])

    calcs(datas)


if __name__ == '__main__':
    interface()
