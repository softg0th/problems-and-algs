def add(s):
    if len(s) == 1:
        se = f'0{s}'
        return se
    else:
        return s


def make_readable(num):
    seconds = 0

    while num % 60 != 0:
        seconds += 1
        num -= 1

    temp = num // 60
    minutes = 0

    while temp % 60 != 0:
        minutes += 1
        temp -= 1

    houres = temp // 60

    seconds = add(str(seconds))
    minutes = add(str(minutes))
    houres = add(str(houres))

    buf = [seconds, minutes, houres]

    output = f'{buf[2]}:{buf[1]}:{buf[0]}'
    return output
