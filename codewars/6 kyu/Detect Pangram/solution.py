import re


def is_pangram(s):
    letters = []
    regex = "^[a-z]|[A-Z]$"
    for i in s:
        if not re.match(regex, i):
            continue
        if i in letters:
            continue

        if i.lower() in letters:
            continue

        if i.upper() in letters:
            continue

        else:
            letters.append(i)

    if len(letters) == 26:
        return True

    return False
