def chet_nechet(row):
    if len(row) == 1:
        return row[0]
    row.insert(0, 0)
    left = 1
    right = len(row) - 1
    tag = 0
    output = 0
    while left < right:
        if (((left % 2 != 0) and (row[left] % 2 != 0)) and ((right % 2 != 0) and (row[right] % 2 != 0))) or (
                ((left % 2 == 0) and (row[left] % 2 == 0)) and ((right % 2 == 0) and (row[right] % 2 == 0))):
            left += 1
            right -= 1

        if (tag == 1) and (((left % 2 != 0 and row[left] % 2 == 0) or (left % 2 == 0 and row[left] % 2 != 0)) or
                           ((right % 2 != 0 and row[right] % 2 == 0) or (right % 2 == 0 and row[right] % 2 != 0))):
            tag = 2
            break

        if ((right % 2 == 0) and (row[right] % 2 == 0)) or ((right % 2 != 0) and (row[right] % 2 != 0)):
            right -= 1

        if ((left % 2 == 0) and (row[left] % 2 == 0)) or ((left % 2 != 0) and (row[left] % 2 != 0)):
            left += 1

        if ((left % 2 != 0) and (row[left] % 2 == 0) or (left % 2 == 0) and (row[left] % 2 != 0)) and \
                ((right % 2 != 0) and (row[right] % 2 == 0) or (right % 2 == 0) and (row[right] % 2 != 0)) and (left != right):
            if tag == 0:
                buf = row[right]
                row[right] = row[left]
                row[left] = buf
                tag = 1

    if tag == 0 or tag == 2:
        output = '-1 -1'
        return output
    if tag == 1:
        output = row
        output = output[1:]
        output = [str(i) for i in output]
        output_str = ' '.join(output)
        return output_str


def interface():
    sher = int(input())
    people = input()
    people = people.split()
    people = [int(i) for i in people]
    print(chet_nechet(people))


if __name__ == '__main__':
    interface()
