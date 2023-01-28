#import threading
#print(threading.current_thread().getName())
#how to create a thread
from threading import *
import time
def demo_thread():
    time.sleep(3)
    print("hello")

#creating thread
t1=Thread(target=demo_thread)#method
t1.start() #