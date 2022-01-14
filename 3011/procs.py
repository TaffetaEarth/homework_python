import multiprocessing as mp
import random as rnd


def exponentiation(numbers, exponent):
    while True:
        number = numbers.get()
        print(pow(number, exponent))
        numbers.task_done()


def generation(low, high, q, numbers):
    for i in range(q):
        num = rnd.randrange(low, high)
        numbers.put(num)


nums_queue = mp.JoinableQueue()
exponentiation_pr = mp.Process(target=exponentiation, args=(nums_queue, 2))
exponentiation_pr.daemon = True
exponentiation_pr.start()
generation(0, 10, 5, nums_queue)
nums_queue.join()
