import matplotlib.pyplot as plt


def many_graphics_creator(*args, **kwargs):
    i = 1
    for list1 in args:
        x, y = list1[0], list1[1]
        color = "color_" + str(i)
        try:
            if color in kwargs.keys():
                plt.plot(x, y, color=kwargs[color])
            else:
                plt.plot(x, y, color="b")
        except Exception as e:
            print(e)
        i += 1
    plt.show()


def many_bars_creator(*args, **kwargs):
    t = 1
    try:
        bar = plt.bar([value[0] for value in args], [value[1] for value in args])
        for i in range(len(bar)):
            color = "color_" + str(t)
            if color in kwargs:
                bar[i].set_color(kwargs[color])
                t += 1
    except Exception as e:
        print(e)
    plt.show()


def draw_pie(*args):
    sizes = []
    labels = []
    colors = []
    for size, label, color in args:
        sizes.append(size)
        labels.append(label)
        colors.append(color)
    plt.pie(sizes, colors=colors, startangle=90, autopct='%1.2f%%')
    plt.legend(labels, loc='best')
    plt.show()


many_graphics_creator([[1, 2, 3, 4, 5, 6, 7], [6, 7, 8, 4, 5, 9, 3]], [[4, 44, 67, 3], [5, 7, 8, 56]], color_1="r")
# many_bars_creator(["First", 2], ["Second", 3], color_1="r", color_2="g")