def many_lists(list_of):
    default_set = set(list_of[0])
    for i in range(len(list_of)):
        default_set.intersection_update(list_of[i])
    return list(default_set)


print(many_lists([[1, 2, 3], [3, 4, 5], [3, 7, 8]]))
