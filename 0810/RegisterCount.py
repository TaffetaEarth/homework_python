def register_count(st):
    upper = 0
    lower = 0
    for i in st:
        if i.isupper():
            upper += 1
        else:
            lower += 1
    if upper > lower:
        return 1
    elif upper == lower:
        return 0
    else:
        return -1


print(register_count("AAA"))