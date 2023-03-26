def palindrom(string):
    p = string[::-1]
    strmas = string.strip()
    palmas = p.strip()
    count = 0

    for i in range(len(strmas)):
        if palmas[i] != strmas[i]:
            count += 1
    return count//2


def interface():
    strok = input()
    print(palindrom(strok))


if __name__ == '__main__':
    interface()
