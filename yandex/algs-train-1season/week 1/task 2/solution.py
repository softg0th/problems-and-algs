def triange(x, y, z):
    if x + y > z and x + z > y and z + y > x:
        return 'YES'
    return 'NO'


def interface():
    a = int(input())
    b = int(input())
    c = int(input())
    print(triange(a, b, c))


if __name__ == '__main__':
    interface()
