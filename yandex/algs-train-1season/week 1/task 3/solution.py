class Storage:
    nums = []
    symbs = ['(', '-', ')']


s = Storage()


def check(num):
    if len(s.nums) == 0:
        s.nums.append(num)
        return 'NO'

    if num in s.nums:
        return 'YES'

    edited_num = ''
    for i in num:
        if i not in s.symbs:
            edited_num += i

    if num in s.nums:
        return 'YES'

    if edited_num[0:1] == '+7':
        edited_num = edited_num[2:]
        edited_num = '8' + edited_num

    if num in s.nums:
        return 'YES'

    maybe = ''
    if len(edited_num) != 1:
        maybe = f'8{edited_num[1:]}'
