def text(text):
    d = {}
    text = text.lower()
    text = text.replace(".", " ")
    text = text.replace(",", " ")
    text = text.replace("!", " ")
    text = text.replace("?", " ")
    text = text.replace(":", " ")
    splitted = text.split()
    for value in set(splitted):
        d[value] = splitted.count(value)
    top = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print("Топ-10 слов:")
    for i in range(10):
        print(str(i+1) + ". " + str(top[i][0]) + ", количество: " + str(top[i][1]))
    return d


text("Живут грызуны по лесам и полям что они едят эти зверьки грызут зерна и кору деревьев зайцы\
 обгладывают яблони в саду грызуны портят посевы")
