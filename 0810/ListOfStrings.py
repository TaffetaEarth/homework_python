import random
import string


def relation(arr):
    upper = 0
    equal = 0
    lower = 0
    for value in arr:
        if register_count(value) == 1:
            upper += 1
        elif register_count(value) == 0:
            equal += 1
        else:
            lower += 1
    print("A>a " + str(int(upper/len(arr)*100)) + "%")
    print("A=a " + str(int(equal / len(arr) * 100)) + "%")
    print("A<a " + str(int(lower / len(arr) * 100)) + "%")


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


def string_generation(leng):
    s = ""
    for i in range(leng):
        s += random.choice(string.ascii_letters)
    return s


def arr_generation(n):
    arr = []
    for i in range(n):
        arr.append(string_generation(6))
    print(arr)
    return arr


relation(arr_generation(10))
