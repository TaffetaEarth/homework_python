class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.marker = False
        k = 0
        for i in range(len(matrix)):
            if len(self.matrix[0]) == len(self.matrix[i]):
                k += 1
        if k == len(self.matrix):
            self.marker = True
        else:
            print("Матрица введена некорректно")

    def trans(self):
        if self.marker:
            n = len(self.matrix)
            m = len(self.matrix[0])
            for i in range(m):
                for j in range(n):
                    print(self.matrix[j][i], end=' ')
                print()


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]])
matrix1.trans()

