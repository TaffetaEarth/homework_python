i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
how_often = []
counter = 0
f = open("test.txt")
a = f.readlines()
for string in a:
    collect = ""
    for value in i:
        quant = string.count(str(value))
        how_often.append(quant)
    while counter != len(how_often):
        counter = 0
        for j in how_often:
            if j == 0:
                counter += 1
        if counter != len(how_often):
            collect += str(i[how_often.index(max(how_often))])
            how_often[how_often.index(max(how_often))] = 0
    print(collect[::-1])
    print("\n")
    how_often.clear()

