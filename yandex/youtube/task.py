a = [0, 2, 1, 5, 7, 8, 9, 4]

i = 0
j = 0
res = 0
max = -1
newit = False
array = [-1, -1]
l = len(a)

for ind in range(l):
    print(a[i ])
    if newit:
        res = 0
    if res == 0:
        array[0] = a[ind]
        array[1] = a[ind]
    if a[ind] < array[1] and max < res:
        max = res
        newit = True
    res += 1

print(array, res)