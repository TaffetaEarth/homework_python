class Person:
    def __init__(self, name):
        self.name = name

    def say(self):
        print(self.name)


class Complex_Person(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def say_more(self):
        super().say()
        print("I'm a complex person")


class Counter:
    __count = 0

    def add_count(self):
        self.__count += 1

    def get_count(self):
        return self.__count

    def counter_to_zero(self):
        self.__count = 0
