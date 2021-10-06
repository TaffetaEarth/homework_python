def intersec_of_lists(list1, list2):
    return list(set(list1).intersection(set(list2)))


print(intersec_of_lists([1, 1, 2, 3, 4], [3, 4, 5, 7]))
