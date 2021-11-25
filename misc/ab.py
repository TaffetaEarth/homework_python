def change(a, b):
    a += b
    b = a - b
    a = a - b
    print(a, b)


def arr(x, normal):
    if sum(x) == sum(normal):
        return 0
    else:
        return sum(x) - sum(normal)


def palindrome(x):
    x = str(x)
    for i in range(len(x)):
        if x[i] != x[-(i + 1)]:
            return False
    return True


def break_camel_case(x):
    # return ''.join([i if i.islower() else " " + i for i in x])
    # f = lambda x: "".join(x[i] if x[i].islower() else " " + x[i] for i in range(len(x)))
    f = lambda x: (x[i] if x[i].islower() else " " + x[i] for i in range(len(x)))
    return "".join(f(x))


a = 3
b = 5
change(a, b)

x = 121
print(palindrome(x))

string = "hdhhdHhdhkshdYydhdhJpskldk"
print(break_camel_case(string))
