import random


def rand_arr(leng, first, last):
    arr = []
    i = 0
    for i in range(leng):
        arr.append(random.randint(first, last))
    return arr


def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                n = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = n
    return arr


print(sort(rand_arr(int(input()), int(input()), int(input()))))