def add_binary(a, b):
    sum = a + b
    binary = ''

    while sum > 0:
        binary = str(sum % 2) + binary
        sum = sum // 2

    return binary
