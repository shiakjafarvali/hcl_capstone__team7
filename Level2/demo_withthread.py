from threading import *
import time
def double(num):
    for n in num:
        time.sleep(2)
        print(2*n)
def square(num):
    for n in num:
        time.sleep(2)
        print(n*n)

num=[1,2,3,4,5]
bt=time.time()
#creating thread
t1=Thread(target=double,args=(num,))
t2=Thread(target=square, args=(num,))
t1.start() #runnable
t1.join()
t2.start()
t2.join()
et=time.time()
print(et-bt,sep=' ')
