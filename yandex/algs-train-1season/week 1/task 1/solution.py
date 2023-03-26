def freeze(x, y):
    if x > y:
        return y
    return x


def heat(x, y):
    if y < x:
        return x
    return y


def auto(x, y):
    return y


def fan(x, y):
    return x


def interface():
    data = input()
    data = data.split()
    troom, tcond = data[0], data[1]
    command = input()
    if command == 'freeze':
        print(freeze(int(troom), int(tcond)))
    if command == 'heat':
        print(heat(int(troom), int(tcond)))
    if command == 'auto':
        print(auto(int(troom), int(tcond)))
    if command == 'fan':
        print(fan(int(troom), int(tcond)))


if __name__ == '__main__':
    interface()
