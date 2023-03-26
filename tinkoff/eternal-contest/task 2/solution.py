def calculate(num):
    tag = 1
    answer = 0
    while num > tag:
        tag *= 2
        answer += 1
    return answer


def interface():
    parts = int(input())
    print(calculate(parts))


if __name__ == '__main__':
    interface()
