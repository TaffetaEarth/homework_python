import threading
import queue
import random as rnd


def exponentiation(numbers, exponent):
    while True:
        number = numbers.get()
        print(pow(number, exponent))
        numbers.task_done()


def generation(low, high, q, numbers):
    for i in range(q):
        num = rnd.randrange(low, high)
        numbers.put_nowait(num)


nums_queue = queue.Queue()

for n in range(2):
    exp_thr = threading.Thread(target=exponentiation, args=(nums_queue, 2), daemon=True)
    exp_thr.start()

generation(1, 15, 10, nums_queue)
nums_queue.join()
