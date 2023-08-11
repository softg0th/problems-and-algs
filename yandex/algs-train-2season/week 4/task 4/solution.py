def calcs(data):
    ht = {}
    electoral = {}
    all_votes = 0
    first_electoral = 0
    mods = {}
    sum = 0
    for element in data:
        key = ' '.join(element[0])
        ht[key] = element[1]

    for vote in ht.values():
        all_votes += vote

    first_electoral = all_votes // 450

    for vote in ht.keys():
        print(ht[vote], first_electoral)
        result = ht[vote] // first_electoral
        electoral[vote] = result
        sum += result
    if sum < 450:
        for element in ht.keys():
            result = ht[element] % first_electoral
            mods[element] = result
        sorted_mods = dict(sorted(mods.items(), key=lambda item: item[1]))
        print(electoral)
        for element in sorted_mods.keys():
            sorted_mods[element] = electoral[element]
        dt = []
        for i in sorted_mods:
            dt.append(i)

        while True:
            for key in dt:
                sorted_mods[key] += 1
            sum += 1
            if sum == 450:
                break
        print(sum, sorted_mods)
    print(electoral)


def interface():
    dt = []
    while True:
        base = input()
        if base == '':
            break
        data = base.split()
        data = [data[0:-1], int(data[-1])]
        dt.append(data)
    calcs(dt)


if __name__ == '__main__':
    interface()
