import matplotlib.pyplot as plt


def graphic_maker():
    while True:
        xs = input("x :").split()
        ys = input("y :").split()
        color = input("color :")
        try:
            xs_int = [int(x) for x in xs]
            ys_int = [int(y) for y in ys]
            plt.plot(xs_int, ys_int, color)
        except ValueError:
            print("Введено некорректное значение аргументов")
        print("Хотите добавить еще график?")
        if input() == "n":
            plt.show()
            break


graphic_maker()
