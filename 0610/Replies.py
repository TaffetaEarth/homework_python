def replies(list1):
    rep = set
    uniq_elements = set(list1)
    for value in uniq_elements:
        quan = list1.count(value)
        if quan > 1:
            print("Символ " + str(value) + " повторяется " + str(quan) + " раз")
    return rep


replies([1, 1, 2])