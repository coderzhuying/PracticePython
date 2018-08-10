import time
import threading

VALUE = 0

gLock = threading.Lock()

def coding():
    for x in range(0,3):
        print("正在编码%s"%x)
        time.sleep(1)

def drawing():
    for x in range(3):
        print("正在画画%s"%x)
        time.sleep(1)


def single_threading():
    coding()
    drawing()

def many_threading():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()

class Coding(threading.Thread):
    def run(self):
        for x in range(3):
            print("正在编码%s"%x)
            time.sleep(1)

class Drawing(threading.Thread):
    def run(self):
        for x in range(3):
            print("正在画画%s"%x)
            time.sleep(1)

def many_threading2():
    t1 = Coding()
    t2 = Drawing()
    t1.start()
    t2.start()

def lock_thread():
    # t1 = threading.Thread(target=add_value)
    # t2 = threading.Thread(target=cut_value)
    #
    # t1.start()
    # t2.start()

    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()



def add_value():
    global VALUE
    for x in range(1000000):
        gLock.acquire()
        VALUE = VALUE + 1
        gLock.release()
    print("VALUE=%d"%VALUE)

def cut_value():
    global VALUE
    for x in range(1000000):
        gLock.acquire()
        VALUE = VALUE - 1
        gLock.release()
    print("VALUE=%d"%VALUE)


if __name__ == '__main__':
    # single_threading()

    # many_threading2()

    lock_thread()
