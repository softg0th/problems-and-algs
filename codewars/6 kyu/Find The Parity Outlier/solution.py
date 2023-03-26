def find_outlier(integers):
    even = 0
    odd = 0
    counter = 0

    for i in integers:
        if counter <= 5:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
            counter += 1
        else:
            break

    if even > odd:
        for i in integers:
            if i % 2 != 0:
                return i

    if odd > even:
        for i in integers:
            if i % 2 == 0:
                return i
