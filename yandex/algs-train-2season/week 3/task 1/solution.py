def calcs(lst1, lst2):
    return len(set(lst1).intersection(lst2))


def interface():
    first = input()
    second = input()

    first = first.split(' ')
    second = second.split(' ')

    first_nums = [int(i) for i in first]
    sec_nums = [int(i) for i in second]
    print(calcs(first_nums, sec_nums))


if __name__ == '__main__':
    interface()
