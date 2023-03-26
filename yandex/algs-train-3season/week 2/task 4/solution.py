def heapify(lst, size, value):
    largest = value
    leftChild = 2*value + 1
    rightChild = 2*value + 2

    if leftChild < value and lst[largest] < lst[leftChild]:
        largest = lst[leftChild]
    if rightChild < value and lst[largest] < lst[rightChild]:
        largest = lst[rightChild]

    if largest != value:
        lst[value], lst[largest] = lst[largest], lst[value]
        heapify(lst, size, largest)


def insert(lst, newValue):
    if len(lst) == 0:
        lst.append(newValue)
    else:
        lst.append(newValue)
        for i in range((len(lst) // 2) - 1, -1, -1):
            heapify(lst, len(lst), newValue)


def extract(lst):
    value = max(lst)
    lst.remove(value)
    print(value)
    for i in range((len(lst) // 2) - 1, -1, -1):
        heapify(lst, len(lst), i)


def interface():
    arr = []
    count = int(input())
    for i in range(count):
        data = input()
        if len(data) > 1:
            numb = data.split()
            numb = numb[1]
            insert(arr, int(numb))
        else:
            extract(arr)


if __name__ == '__main__':
    interface()
