import sys

N = int(input())


def dp(n):
    if n == 3:
        return 1

    sh = [0, 0, 1]
    for i in range(3, n):
        sh.append(2 ** (i-2) + sh[i-1] + sh[i-2] + sh[i-3])
    return sh[-1]


def calc(n):
    return 2**n - dp(n)


for i in range(3, N):
    print(calc(N))

