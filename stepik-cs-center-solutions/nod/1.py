def gcd(a,b):
    if a % b == 0:
        return b
    r = a % b
    return gcd(b, r)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
