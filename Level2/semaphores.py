from threading import *
import time
s=Semaphore(2)#2 limited resources
def wish(name):
    s.acquire()
    for i in range(10):
        print("Good evening ",end='')
        time.sleep(2)
        print(name)
    s.release()
t1=Thread(target=wish,args=('jose',))
t2=Thread(target=wish,args=('Mich',))
t3=Thread(target=wish,args=('Mart',))
t4=Thread(target=wish,args=('solomon',))
t5=Thread(target=wish,args=('jafar',))
t6=Thread(target=wish,args=('vali',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()