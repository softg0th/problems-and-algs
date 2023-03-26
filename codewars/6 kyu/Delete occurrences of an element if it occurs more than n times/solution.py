def delete_nth(order, max_e):
    elements = set(order)
    capacity = {}
    final = []
    for i in elements:
        capacity[i] = 0
    for i in order:
        if capacity[i] >= max_e:
            continue
        else:
            final.append(i)
            capacity[i] += 1
    return final
