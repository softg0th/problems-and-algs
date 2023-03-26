def calc(lst):
    stores = []
    houses = []
    dists = []
    for element in range(len(lst)):
        if lst[element] == 2:
            stores.append(element)
        if lst[element] == 1:
            houses.append(element)

    for house in houses:
        maxEl = 99999
        for store in stores:
            dist = abs(house-store)
            if dist < maxEl:
                maxEl = dist
        dists.append(maxEl)
    return max(dists)


def interface():
    prosp = input()
    prosp = prosp.split()
    pr = []
    for i in prosp:
        pr.append(int(i))

    print(calc(pr))


if __name__ == '__main__':
    interface()
