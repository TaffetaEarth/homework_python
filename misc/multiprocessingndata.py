import multiprocessing
import os
import time


def say(what):
    print('Process %s says: %s' % (os.getpid(), what))


for f in range(4):
    process = multiprocessing.Process(target=say, args=('I am process %s' % f,))
    process.start()


def long_process(i=0):
    while i < 374673434:
        print(i)
        i += 1


process = multiprocessing.Process(target=long_process)
process.start()
time.sleep(3)
process.terminate()
