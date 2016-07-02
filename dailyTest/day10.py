#coding:utf-8
import threading
import time
import Queue

qlock=threading.Lock()

def getData(q):
    qlock.acquire()
    if not q.empty():
        data=q.get()
        print data
    
def music(song):
    for i in range(0,10):
        print " %s 在听 %s"%(time.ctime(),song)
        time.sleep(1)
def printTime(number,delay):
    
    for i in range(0,number-1):
        print "打印当前时间:%s"%time.ctime()
        time.sleep(delay)

class MyThread(threading.Thread):
    
    def __init__(self,func,params):
        threading.Thread.__init__(self)  #这里必须用线程类本身的初始化函数。
        self.func=func
        self.params=params
        
    def run(self):
        apply(self.func,self.params)
        
if __name__=="__main__":
    
    m1=MyThread(music,("浮夸",))
    m2=MyThread(printTime,(8,1))
    m1.start()
    m2.start()
    m1.join()
    m2.join()
    print "all is done at %s"%time.ctime()
            
        
    
        
    