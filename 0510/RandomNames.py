import random


def random_name(names, second_names, pre_names, quan):
    i = 0
    while i < quan:
        yield random.choice(names) + " " + random.choice(second_names) + " " + random.choice(pre_names)
        i += 1


for i in random_name(["Иванов", "Петров", "Козлов", "Сидоров"], ["Иван", "Петр", "Александр", "Андрей"],
                     ["Иванович", "Петрович", "Алексеевич", "Андреевич"], 10):
    print(i)
