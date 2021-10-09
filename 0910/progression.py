def progression(item, quan=3):
    a = []
    i = 1
    counter = 0
    item = str(item)
    for k in range(quan):
        a.append(item * i)
        i += 1
    for n in a:
        counter += int(n)
    return "Result is " + str(counter)


print(progression(11, 9))
