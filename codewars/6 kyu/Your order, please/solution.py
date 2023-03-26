def order(sentence):
    temp = {}
    buf = []
    output = ''

    for i in sentence:
        if i.isdigit() is True:
            buf.append(i)

    for i in buf:
        temp[i] = 'value'

    sentence = sentence.split(' ')

    for i in sentence:
        for j in i:
            if j in temp.keys():
                temp[j] = i

    stdout = sorted(temp.keys())

    for i in stdout:
        output += f'{temp[i]} '

    output = output[:-1]

    return output


print(order("4of Fo1r pe6ople g3ood th5e the2"))