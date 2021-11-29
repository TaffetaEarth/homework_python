def instagram(*args):
    if len(args) == 0:
        return "no one likes it"
    if len(args) == 1:
        return str(args[0]) + " likes it"
    if len(args) == 2:
        return str(args[0]) + " and " + str(args[1]) + " like it"
    if len(args) == 3:
        return str(args[0]) + ", " + str(args[1]) + " and " + str(args[2]) + " like it"
    if len(args) > 3:
        return str(args[0]) + " and " + str(len(args) - 1) + " others like it"


def weight_sort(list1):
    d = {}
    for value in list1:
        d[value] = sum(int(i) for i in str(value))
    sort = sorted(d.items(), key=lambda x: x[1])
    for i in range(len(sort)):
        for j in range(len(sort) - i):
            if sort[i][1] == sort[j][1]:
                if sort[i][0] < sort[j][0]:
                    sort[j], sort[i] = sort[i], sort[j]
    return sort


def nod(list1):
    gcf = 1
    for i in range (2, sorted(list1)[0]+1):
        is_cf = True
        for num in list1:
            if num % i != 0:
                is_cf = False
        if is_cf:
            gcf = i
        return gcf


def check(pos):
    lett = ord(pos[0])
    num = int(pos[1])
    if (lett % 2 == 0 and num % 2 == 0) or (lett % 2 != 0 and num % 2 != 0):
        return "White"
    else:
        return "Black"


def proverkaAllSkob(skob_str):
    stack_from_strings = []
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    for i in skob_str:
        if i in open_list:
            stack_from_strings.append(i)
        elif i in close_list:
            if len(stack_from_strings) > 0:
                if open_list[close_list.index(i)] == stack_from_strings[-1]:
                    stack_from_strings.pop()
            else:
                return False
    if len(stack_from_strings) == 0:
        return True
    else:
        return False


# print(weight_sort([111, 23, 1111, 9, 10, 13]))
#print(nod([10, 15, 20]))
print(proverkaAllSkob('[(])[]'))
