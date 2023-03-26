def solution(args):
    inters = []
    con = []
    merg = []
    maybe = []
    for i in range(len(args)-1):
        if args[i] - args[i - 2] == 2:
            if args[i - 2] not in inters:
                inters.append(args[i - 2])
            inters.append(args[i])
        elif args[i] - args[i-1] != 1 and args[i+1] - args[i] != 1:
            merg.append(args[i])
        else:
            maybe.append(args[i])
    merg = merg + maybe
    for i in range(len(inters)):
        if type(inters[i]) and type(inters[i - 1]) is not str:
            if inters[i] - inters[i - 1] != 2:
                inters.insert(i, 'flag')

    inters = inters[1:]
    strok = " ".join(map(str, inters))
    inters = strok.split("flag")
    for i in inters:
        j = list(i.strip())
        con.append([str(j[0] + j[1]), str(j[-2] + j[-1])])

    merge = []
    print(con)
    for i in con:
        for j in i:
            merge.append(int(j))
    print(sorted(merg))
    print(merge)


print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))
