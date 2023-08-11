def calcs(lst, data):
    sums = [0] * (len(data)+1)
    temp = 0

    for i in range(1, len(data)+1):
        

    '''
    for i in range(1, len(data)):
        if lst[data[i][0]] == temp:
            sums[i] = sums[i - 1] + lst[data[i-1][1]]
        else:
            temp = lst[data[i-1][0]]
            sums[i] = lst[data[i-1][1]]
    return sums
    '''

def interface():
    size, count = map(int, input().split())
    data = input()
    data = data.split()
    data = [int(x) for x in data]
    otrs = []
    data.insert(0, 0)
    for x in range(count):
        i, j = map(int, input().split())
        otrs.append([i, j])
    dt = calcs(data, otrs)
    for i in dt:
        print(i)


if __name__ == '__main__':
    interface()
