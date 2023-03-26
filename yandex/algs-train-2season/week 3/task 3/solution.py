def calc(lst):
    data = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                break

            else:
                data.append(lst[i])
    return data


def interface():
    data = [int(s) for s in input().split()]
    print(calc(data))


if __name__ == '__main__':
    interface()
