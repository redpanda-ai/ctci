import threading
import time

mutex = threading.Lock()  # equal to threading.Semaphore(1)


def fun1():
    while True:
        mutex.acquire()
        print(1)
        mutex.release()
        time.sleep(0.5)


def fun2():
    while True:
        mutex.acquire()
        print(2)
        mutex.release()
        time.sleep(0.5)


t1 = threading.Thread(target=fun1).start()
t2 = threading.Thread(target=fun2).start()