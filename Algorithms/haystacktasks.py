import random
import numpy as np


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def connect(self, next_node):
        self.next_node = next_node

    def add(self, head):
        while head.next_node:
            head = head.next_node
        head.next_node = self


def repeat_numbers(s):
    counter = 0
    for j in range(1, len(s)):
        table = []
        for i in range(len(s) - j + 1):
            print(s[i:i + j])
            table.append(s[i:i + j])
        hash_set = set(table)
        counter += len(table) - len(hash_set)
    return counter


# print(repeat_numbers("abcabc"))


def hash_table(strings):
    hashes = {}
    for i in strings:
        if hash(i) in hashes.keys():
            hashes[hash(i)] = Node(i)
        else:
            Node(i).add(hashes[hash(i)])
    return hashes


def hash_table_with_mistakes(table, queue):
    for key, value in table.items():
        if random.randint(0, 9) == 0 and value:
            while value:
                queue.insert(0, [key, Node("z" + value.data)])
                value = value.next_node
        else:
            while value:
                queue.insert(0, [key, value])
                value = value.next_node
    return queue


def mistake_founder(queue):
    while queue:
        curr = queue.pop()
        while curr[1]:
            if hash(curr[1].data) != curr[0]:
                print(f"Mistake in {curr[1].data}")
            else:
                print(curr[2].data)
            curr[1] = curr[1].next_node


def hash_func(string_to_hash, p=2):
    hash_sum = np.uint64()
    hash_sum += sum([pow(p, i) * (ord(string_to_hash[i]) - 64) for i in range(len(string_to_hash))])
    return hash_sum


f = lambda string_to_hash, p=2: sum(
    [pow(p, i) * (ord(string_to_hash[i]) - 64) for i in range(len(string_to_hash))]) if sum(
    [pow(p, i) * (ord(string_to_hash[i]) - 64) for i in range(len(string_to_hash))]) is not np.uint64 else "Error"


# print(f("jaashpoifpogs;lk;ajjfsdl;fjkiigf", 90))


def no_match_finder(string_to_match_in):
    hashes = {}
    counter = 0
    for i in string_to_match_in:
        if i in hashes[hash(i)]:
            hashes[hash(i)].append(i)
        else:
            hashes[hash(i)] = [i]
    for i in hashes.values():
        if len(i) == 1:
            counter += 1
    return counter


print(no_match_finder("abc"))
