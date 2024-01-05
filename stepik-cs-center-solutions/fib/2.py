def fib_digit(n):
    if n in (1, 2):
        return n
    memory = {}
    memory['1'], memory['2'] = 1, 2
    for i in range(2, n):
        memory['i'] = memory[str((i-1))] + memory[str(i-2)]
    return memory[str(n)] % 10


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
