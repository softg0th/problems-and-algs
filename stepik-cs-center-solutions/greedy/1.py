def greedy(data):
    length = len(data)
    if length < 2:
        print()
        return
    counter = 0
    points = []
    data.sort(key=lambda x: x[1])
    for otr in range(len(data)):
        if points != [] and data[otr][0] <= points[-1]:
            continue
        pointer = data[otr][1]
        for next_otr in range(otr, length-1):
            if data[next_otr][0] > pointer:
                break
            counter += 1
            points.append(pointer)
            break
    if counter >= 1:
        print(counter)
        points = [str(x) for x in points]
        print(' '.join(points))
    print()
    return


def main():
    n = int(input())
    data = []
    for i in range(n):
        otr = tuple(map(int, input().split()))
        data.append(otr)
    greedy(data)


if __name__ == "__main__":
    main()
