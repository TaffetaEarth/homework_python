class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    knowledge = 0
    hw = 0

    def get_knowledge(self):
        self.knowledge += 1

    def get_hw(self, n):
        self.hw += n

    def do_hw(self):
        if self.hw > 0:
            self.hw -= 1
            self.get_knowledge()
        else:
            print("No hw")


class Teacher(Person):
    work = 0

    def give_knowledge(self, students):
        for student in students:
            student.get_knowledge()
            self.work += 1

    def give_hw(self, students, n):
        for student in students:
            student.get_hw(n)
            self.work += 1


t = Teacher("Petr")
st1 = Student("Leha")
st2 = Student("Sanya")

t.give_knowledge([st1, st2])
print(st1.knowledge)
print(t.work)
