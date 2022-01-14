db = dict()


def add_to_hash(login, password):
    for value in db.values():
        if login in value:
            print("Такой пользователь уже существует")
            return -1
    if hash(password) not in db.keys():
        db[hash(password)] = login
    else:
        db[hash(password)].append(hash(password))


import hashlib

h = hashlib.sha512()


def auth(login, password):
    if db.get(hash(password)):
        return login in db[hash(password)]
    else:
        return False


# add_to_hash("abc", "abs1234")
# add_to_hash("abc", "abs156")
# print(db)
# print(auth("abc", "abs1234"))

# while True:
#     login = input("login: ")
#     password = input("password: ")
#     if auth(login, password):
#         print("Success!")
#         break
#     else:
#         print("Try again")


def hash_find(arr, sample):
    counter = 0
    for i in arr:
        if hash(i) == hash(sample):
            if i == sample:
                counter += 1
    return counter

print(hash_find(['h', 'h', 'o'], 'h'))