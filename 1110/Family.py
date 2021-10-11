import random


class Parent:
    def __init__(self, n, e, h):
        self.name = n
        self.eyes = e
        self.hair = h


class Child:
    def __init__(self, name, parents):
        self.name = name
        possible_hair = [parent.hair for parent in parents]
        possible_eyes = [parent.eyes for parent in parents]
        self.eyes = random.choice(possible_eyes)
        self.hair = random.choice(possible_hair)

    def return_info(self):
        return "Имя: " + self.name + "\n" + "Цвет глаз: " + self.eyes + "\n" + "Цвет волос: " + self.hair + "\n"


pr1 = Parent("Ольга", "Серый", "Каштановые")
pr2 = Parent("Василий", "Зеленый", "Черные")
ch1 = Child("Ксения", [pr1, pr2])
print(ch1.return_info())
