def find_brute(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        flag = True
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                flag = False
                break
        if flag:
            print(i)


# сложность - O(haystack * needle)

# find_brute("abcabchbc", "bc")


def prefix(s):
    a = [0] * len(s)
    for i in range(len(s)):
        for j in range(i):
            if s[0:j] == s[i - j:i]:
                a[i - 1] = j
    return a


def prefix_optimal(s):
    a = [0] * len(s)
    for i in range(1, len(s)):
        k = a[i - 1]
        while k != 0 and s[i] != s[k]:
            k = a[k - 1]
        if s[k] == s[i]:
            k += 1
        a[i] = k
    return a


def z_func(s):
    z = [0] * len(s)
    for i in range(1, len(s)):
        while z[i] + i < len(z) and s[z[i]] == s[z[i] + i]:
            z[i] += 1
    z[0] = len(s)
    return z


def z_optimal(s):
    z = [0] * len(s)
    n = len(s)
    for i in range(1, len(s)):
        while z[i] + i < len(z) and s[z[i]] == s[z[i] + i]:
            z[i] += 1
    z[0] = len(s)
    return z


# print(prefix_optimal("abcabchbc"))


def restoring(a):
    restored = ""
    letter_num = 97
    for i in range(len(a)):
        if a[i] == 0:
            restored += chr(letter_num)
            letter_num += 1
        else:
            restored += restored[a[i] - 1]
    return restored


# print(restoring(prefix_optimal("abcasdabcdbdjfkabc")))


find = lambda main_str, str_to_find, i=0: i + 1 if main_str[i:i + len(str_to_find)] == str_to_find else find(main_str,
                                                                                                             str_to_find,
                                                                                                             i + 1)

rfind = lambda main_str, str_to_find, i=0: i + 1 if main_str[i:i + len(
    str_to_find)] == str_to_find and str_to_find not in main_str else find(main_str, str_to_find, i + 1)


# print(find("abcdef", "ef"))

# print(rfind("abcdef", "ef"))


def kmp(s, t):
    index = -1
    s_prefix = prefix_optimal(s)
    k = 0
    for i in range(len(t)):
        while k > 0 and s[k] != t[i]:
            print(f"while: k = prefix[{k - 1}]")
            k = s_prefix[k - 1]
        if s[k] == t[i]:
            print(f"s[k] == t[i]: k = {k + 1}")
            k += 1
        if k == len(s):
            print(f"index = {i - len(s) + 1}")
            index = i - len(s) + 1
            break
    return index


# print(kmp("ghjkl", "jslsjfklghjakhkfhkjfhajkjfsfghjklkjdhkahfhjkdf"))


def rabin_karp(sub, s):
    n = len(s)
    m = len(sub)
    hsub = h.update(sub)
    hs = h.update(s)
    for i in range(0, n - m + 1):
        print(hs, hsub)
        if hs == hsub:
            if s[i:i + m] == sub:
                return i
        hs = h.update(s[i + 1:i + m + 1])
    return -1


# print(rabin_karp("abcd", "abcd"))

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


add_to_hash("abc", "abs1234")
add_to_hash("abc", "abs156")
print(db)
print(auth("abc", "abs1234"))

while True:
    login = input("login: ")
    password = input("password: ")
    if auth(login, password):
        print("Success!")
        break
    else:
        print("Try again")
