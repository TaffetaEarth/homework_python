import threading
import time


def wait_event():
    print('Старт WAIT_EVENT()')
    event.wait()
    print('Код обработки по событию в WAIT_EVENT()')


def wait_timeout(time_out):
    print('Старт WAIT_TIMEOUT() ')
    while not event.is_set():
        is_set = event.wait(timeout=time_out)
        print(f'TimeOut {time_out} секунды истек')
        if is_set:
            print('Код обработки по событию в WAIT_TIMEOUT()')
        else:
            print('Пока ждем события, код обработки чего-то другого')
            time.sleep(3)


event = threading.Event()
t1 = threading.Thread(name='blocking',
                      target=wait_event)
t1.start()
t2 = threading.Thread(name='non-blocking',
                      target=wait_timeout,
                      args=(2,))
t2.start()
print('Ожидание перед вызовом Event.set()')
time.sleep(5)
event.set()
print('Установлено событие в основном потоке')
