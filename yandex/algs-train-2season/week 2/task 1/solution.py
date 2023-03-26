def count_max(lst):
    count = 0
    highest = max(lst)

    for i in lst:
        if i == highest:
            count += 1
    return count


def interface():
    nums = []

    while True:
        num = int(input())
        if num == 0:
            break
        nums.append(num)

    if len(nums) == 1:
        print(1)
        return 0

    print(count_max(nums))


if __name__ == '__main__':
    interface()
