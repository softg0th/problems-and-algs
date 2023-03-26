from itertools import zip_longest


def cou_s(lst):
    count = max(lst)+1
    edited = [0]*count
    for x in lst:
        edited[x] += 1
    b = []
    for x in range(count):
        print(x)
        print(edited)
        b += [x]*edited[x]
    return b


def convert_ord(lst):  # ну, я пытался изобрести сортировку сравнением с линейной сложностью :)
    ords = []
    for i in lst:
        ords.append(ord(i))
    return ords


def remove_common(lst):
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique


asc_str = "gggghfjhvlmayhdsopleznshix"
ords = convert_ord(asc_str)
k = max(ords)
print(ords)
ords = cou_s(ords)
chrs = []
print(ords)
for i in ords:
    chrs.append(chr(i))
print(chrs)

