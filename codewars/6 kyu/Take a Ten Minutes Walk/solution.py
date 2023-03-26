def is_valid_walk(walk):
    up = 0
    down = 0
    left = 0
    right = 0

    for i in walk:
        if i == 'n':
            up += 1
            down -= 1
        if i == 's':
            down += 1
            up -= 1
        if i == 'w':
            left += 1
            right -= 1
        if i == 'e':
            right += 1
            left -= 1

    buf = [up, down, left, right]
    counter = 0
    for j in buf:
        if j == 0:
            counter += 1

    if len(walk) == 10 and counter == 4:
        return True
    return False
