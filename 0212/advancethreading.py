import queue
import threading
import time
from threading import Thread
import random


class MyThread(Thread):
    def __init__(self, limit):
        super().__init__()
        self.limit = limit

    def run(self):
        for _ in range(self.limit):
            print('message')
            time.sleep(1)


def bubble(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def gen_to_bubble(num):
    for i in range(num):
        bubble([random.randrange(100) for _ in range(1000)])
        print("Bubble " + str(i))


def sort_choice(nums):
    for i in range(len(nums)):
        lowest = i
        for k in range(i, len(nums)):
            if nums[k] < nums[lowest]:
                lowest = k
            nums[lowest], nums[i] = nums[i], nums[lowest]
    return nums


def gen_to_choice(num):
    for i in range(num):
        sort_choice([random.randrange(100) for _ in range(1000)])
        print("Choice " + str(i))


# thr_1 = threading.Thread(target=gen_to_bubble, args=(100,))
# thr_2 = threading.Thread(target=gen_to_choice, args=(100,))
# t = time.time()
# [x.start() for x in [thr_2, thr_1]]
# [x.join() for x in [thr_2, thr_1]]
# time_1 = time.time() - t
# t = time.time()
# gen_to_choice(100)
# gen_to_bubble(100)
# time_2 = time.time() - t
# print(time_2, time_1)


def exponentiation(numbers, q):
    for _ in range(q):
        num = random.randrange(100)
        exponent = random.randrange(10)
        numbers.put_nowait(str(num) + " pow " + str(exponent) + " is " + str(pow(num, exponent)) + "\n")


def writer(numbers):
    while True:
        number = numbers.get()
        f.write(str(number))
        numbers.task_done()


f = open("file.txt", "a")
q = queue.Queue()
exp_thr = threading.Thread(target=writer, args=(q,), daemon=True)
exp_thr.start()
exponentiation(q, 20)
q.join()
f.close()
