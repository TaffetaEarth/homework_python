def generation(string_to_repeat, n):
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            yield string_to_repeat * j
            j += 1
        i += 1


for i in generation('a', 5):
    print(i)