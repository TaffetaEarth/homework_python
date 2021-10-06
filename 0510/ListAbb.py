def abb(name):
    full = name.split()
    if full[0][0].isupper and full[0][1:].islower and full[1][0].isupper and full[1][1:].islower and full[2][
        0].isupper and full[2][1:].islower:
        full[1] = full[1][0] + "."
        full[2] = full[2][0] + "."
        return ' '.join(full)
    else:
        return 'False'


def listabb(name):
    for value in range(len(name)):
        print(abb(name[value]))


listabb(["Ya Yo Yu", "If Of Uf"])
