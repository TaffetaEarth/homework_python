def adress_book():
    a = {}
    while True:
        print("Имя - ")
        name = input()
        if name != "q":
            print("Номер - ")
            phone = input()
            if (phone[0] == "+" and phone[2] == "-" and phone[6] == "-"
                    and phone[10] == "-" and phone[13] == "-"):
                if phone[1:].replace("-", "").isdigit():
                    a[name] = phone
        else:
            break
    return a


print(adress_book())
