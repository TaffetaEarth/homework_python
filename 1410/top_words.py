import string


def text(text):
    d = {}
    text = text.lower()
    for c in string.punctuation:
        text.replace(c, '')
    splitted = text.split()
    for value in set(splitted):
        d[value] = splitted.count(value)
    top = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print("Топ-10 слов:")
    for i in range(10):
        print(str(i+1) + ". " + str(top[i][0]) + ", количество: " + str(top[i][1]))
    return d


f = open('top_words.txt', 'r')
lines = ' '.join(f.readlines())
text(lines)
f.close()
