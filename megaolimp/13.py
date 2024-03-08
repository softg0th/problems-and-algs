import regex as re


def string_fix(s):
    reg = "^(?=.{8,17})(?=.*?[a-z]{2,})(?=.*?[A-Z])(?=.*?\p{P}{2,})[^\p{C}\s]*$"
    for i in s:
        if re.match(reg, i):
            print(1, i)
        else:
            print(0, i)


def interface():
    num = int(input())
    data = []
    for i in range(num):
        st = input()
        data.append(st)
    string_fix(data)


if __name__ == '__main__':
    interface()


"""
Верные примеры:
1. Abcdef12!
2. Zzxyzk1@l
3. Pp@ssword9

Неверные примеры:
1. Abcd123 (недостаточно символов пунктуации)
2. AbC12345678901234 (слишком длинный)
3. lowercas3! (недостаточно заглавных символов)
4. SHORT1! (недостаточно строчных символов)
5. !@#$%^&*() (недостаточно букв и цифр)

"""