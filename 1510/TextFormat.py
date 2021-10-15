f = open("top_words.txt", "r")
print("{0:-^100s}".format("Некоторая статья про Айфоны"))
for c in f.readlines():
    print("{0:-^100s}".format(c))
