def abb(name):
    full = name.split()
    if full[0][0].isupper and full[0][1:].islower and full[1][0].isupper and full[1][1:].islower and full[2][
        0].isupper and full[2][1:].islower:
        full[1] = full[1][0] + "."
        full[2] = full[2][0] + "."
        return ' '.join(full)
    else:
        return 'False'


def name_input():
    list_of_names = []
    while input() != "q":
        b = [input(), input(), input()]
        if abb(' '.join(b)):
            list_of_names.append(abb(' '.join(b)))
        else:
            print("Error")
            break
    print(list_of_names)



