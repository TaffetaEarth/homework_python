import string


def letters(line):
    d = {}
    for i in string.ascii_letters:
        d[i] = line.count(i)
    return d


print(letters("aAAaaaaBbb"))
