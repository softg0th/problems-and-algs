def fib(n):
    counter = 0
    fib1 = 1
    fib2 = 1
    while counter < n - 2:
        sum = fib1 + fib2
        fib1 = fib2
        fib2 = sum
        counter += 1
    return fib2


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
