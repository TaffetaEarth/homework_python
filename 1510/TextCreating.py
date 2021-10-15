def text_create(args, pos="left", lng=100, sy='-'):
    if pos == "center":
        pos = "^"
    elif pos == "right":
        pos = ">"
    else:
        print("Wrong position, position is _default left_")
        pos = "<"
    return ''.join([("{0:%s%s%ss}" % (sy, pos, str(lng))).format(c) for c in args])


print(text_create(open("top_words.txt", 'r').readlines(), "center", 110, "^"))
