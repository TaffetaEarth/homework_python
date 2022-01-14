import threading
import time


def wait_event():
    print("Process starting...")
    time.sleep(2)
    t2.start()
    event.wait()
    t2.join()
    time.sleep(2)
    print("Process finished")


def wait_timeout(time_out, i):
    while not event.is_set():
        is_set = event.wait(timeout=time_out)
        print(i)
        i += 1
        if is_set:
            print("Finishing...")


event = threading.Event()
t1 = threading.Thread(target=wait_event)
t2 = threading.Thread(target=wait_timeout, args=(1, 0))
t1.start()
event.wait(timeout=13)
event.set()
