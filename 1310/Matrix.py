import random


def content(n, m):
    matrix = [[]]
    for i in range(n):
        for j in range(m):
            matrix[i][j].append(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    return matrix


class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.content = content(self.n, self.m)

    def transpose(self):
        matrixt = [[]]
        for i in range(self.n):
            for j in range(self.m):
                matrixt[j][i] = self.content[i][j]
        return matrixt


mat = Matrix(3, 4)
print(mat.transpose())
