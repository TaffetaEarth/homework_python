import numpy as np


def transpose(list1):
    return np.transpose(list1).tolist()


def multiplying(list1, list2):
    return np.dot(list1, list2).tolist()


def list_sum(list1, list2):
    return np.add(list1, list2).tolist()


def submatrix(list1, firstsring, laststring, firstcoloumn, lastcoloumn):
    list1 = np.reshape(list1, (len(list1), len(list1[0])))
    return list1[firstcoloumn:lastcoloumn, firstsring:laststring].tolist()


z = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
y = [[3, 3, 3],
     [3, 3, 3],
     [3, 3, 3]]
print(type(transpose(z)), "\n")
print(type(multiplying(z, y)), "\n")
print(type(list_sum(z, y)), "\n")
print(type(submatrix(z, 0, 2, 0, 2)), "\n")
