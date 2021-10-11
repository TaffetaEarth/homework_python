import math


class Triangle:
    def __init__(self, a, b, c):
        self.first = a
        self.second = b
        self.third = c

    def get_p(self):
        return self.first + self.second + self.third

    def get_s(self):
        p = self.get_p()/2
        return math.sqrt(p*(p-self.first)*(p-self.second)*(p-self.third))


tr1 = Triangle(3, 4, 5)
print(tr1.get_p())
print(tr1.get_s())
