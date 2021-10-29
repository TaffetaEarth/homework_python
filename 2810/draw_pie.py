import matplotlib.pyplot as plt


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


draw_pie((30, "Args", 'r',), (60, "Kwargs", "b"), (10, "Positional", 'g'))


