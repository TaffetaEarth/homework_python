import math


class Circle:
    def __init__(self, r):
        self.radius = r

    def get_c(self):
        return math.pi * 2 * self.radius

    def get_s(self):
        return math.pi * self.radius ** 2


cr1 = Circle(3)
print(cr1.get_s())
print(cr1.get_c())