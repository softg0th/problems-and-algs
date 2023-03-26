import sys

first = input()
second = input()

first = first.split()
second = second.split()

first = [int(x) for x in first]
second = [int(x) for x in second]

for step in range(10**6):
    if len(first) == 0:
        print('second', step)
        sys.exit()
    if len(second) == 0:
        print('first', step)
        sys.exit()

    case_first = False
    case_sec = False

    first_el = first.pop(0)
    sec_el = second.pop(0)

    if sec_el == 0 and first_el == 9:
        case_sec = True

    if sec_el == 9 and first_el == 0:
        case_first = True

    if case_first is True or first_el > sec_el and case_sec is not True:
        first.extend([first_el, sec_el])

    else:
        second.extend([first_el, sec_el])

print("botva")
