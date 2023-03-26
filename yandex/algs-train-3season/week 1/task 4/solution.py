
count = int(input())
sequence = input()

seq = sequence.split()
seq = [int(x) for x in seq]
ideal = sorted(seq)
stack = []
lounge = []


for vag in seq:
    if len(stack) == 0:
        stack.append(vag)
    else:
        if stack[-1] < vag:
            stack.append(vag)
        if stack[-1] > vag:
            while len(stack) > 0 and stack[-1] > vag:
                buf = stack.pop()
                lounge.append(buf)
            stack.append(vag)

print(lounge)

for i in range(len(lounge)):
    buf = lounge.pop()
    stack.append(buf)

if stack == ideal:
    print('YES')

else:
    print('NO')
