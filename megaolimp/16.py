def prefix(strs):
    strs = sorted(strs)
    longest = 0
    for char in range(len(strs[0])):
        if strs[0][char] == strs[-1][char]:
            longest += 1
        else:
            break
    return strs[0][:longest]


def interface():
    strs = list(map(str, input().split()))
    output = prefix(strs)
    print(output)


if __name__ == '__main__':
    interface()
