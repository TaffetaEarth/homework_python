class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def get_p(self):
        return 2 * (self.width + self.height)

    def get_s(self):
        return self.width * self.height


p_1 = Rectangle(4, 5)
print(p_1.get_p())
