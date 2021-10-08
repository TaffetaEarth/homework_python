import random


def rand_arr(leng, first, last):
    arr = []
    for i in range(leng):
        arr.append(random.randint(first, last))
    return arr


print(rand_arr(int(input()), int(input()), int(input())))