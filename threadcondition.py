import threading
import random
import time

gMoney = 1000

gTotalTime = 10

gTime = 0

gCondition = threading.Condition()

class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTotalTime
        global gTime
        while True:
            money = random.randint(100,1000)
            if gTime < gTotalTime:
                gCondition.acquire()
                gMoney = gMoney + money
                print("%s生产者生产了%d元钱,剩余%d元钱 %d"%(threading.current_thread(),money,gMoney,gTime))
                gTime = gTime + 1
                gCondition.notify_all()
                gCondition.release()
                time.sleep(0.5)

            else:
                break

class Consumer(threading.Thread):
    def run(self):
        global gMoney
        global gTotalTime
        global gTime
        while True:
            money = random.randint(100,1000)
            gCondition.acquire()
            while gMoney < money:
                if gTime >= gTotalTime:
                    gCondition.release()
                    return

                print("%s消费者准备消费%d元钱,但还有%d元钱,余额不足" % (threading.current_thread(), money, gMoney))
                gCondition.wait()


            gMoney = gMoney - money
            print("%s消费者消费了%d元钱,剩余%d元钱" % (threading.current_thread(), money, gMoney))
            gCondition.release()
            time.sleep(0.5)

def main():

    for x in range(4):
        t = Consumer(name='消费者线程%d'%(x+1))
        t.start()

    for x in range(5):
        t = Producer(name='生产者线程%d'%(x+1))
        t.start()



if __name__ == '__main__':
    main()











