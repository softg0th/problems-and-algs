def countingsort(lst):
    minval = min(lst)
    maxval = max(lst)
    largest = maxval[0]-minval[0]+1
    count = [0]*largest
    for now in lst:
        count[now[0]-minval[0]] += 1
    nowpos = 0
    for val in range(0, largest):
        for i in range(count[val]):
            lst[nowpos] = val + minval[0]
            nowpos += 1
    return lst


def calcs(lst):
    ht = {}

    for element in lst:
        if element not in ht.keys():
            ht[element] = 1
        else:
            ht[element] += 1
    data = []

    for element in ht.keys():
        data.append((ht[element], element))
    dt = countingsort(data)
    dt = reversed(dt)
    noted = []
    for element in dt:
        if element not in noted:
            print({i for i in ht if ht[i] == element})
            noted.append(element)


def interface():
    dt = []
    while True:
        base = input()
        if base == '':
            break
        data = base.split()
        for element in data:
            dt.append(element)
    calcs(dt)


if __name__ == '__main__':
    interface()
