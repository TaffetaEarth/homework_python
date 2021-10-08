import random
import string


def string_generation(leng):
    s = ""
    for i in range(leng):
        s += random.choice(string.ascii_letters)
    return s


print(string_generation(int(input())))