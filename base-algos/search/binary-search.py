def binary_search(lst, value):
    mid = len(lst) // 2
    low = 0
    high = len(lst) - 1
    while lst[mid] != value and low <= high:
        if value > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return "No value"
    else:
        return mid


print(binary_search([1, 6, 7, 8, 9, 10], 9))
