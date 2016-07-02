#coding:utf-8
import threading
import time

class Mythread(threading.Thread):
    
    def __init__(self,func,params):
        threading.Thread.__init__(self)
        self.func=func
        self.params=params
        
    def run(self):
        
        
        myApply(self.func,self.params)

def myApply(func,params,data={}):
    
    return apply(func,params)
    
def add(a,b):
    return a+b

def work(a,b,name):
    
    for i in range(0,a):
        print "线程%s：打印%s"%(name,i)
        time.sleep(b)
        
def getlen(l):
    return len(l)

if __name__=="__main__":
    
    #myApply(work,( 20,1,"线程1"))
    
    print "主线程开始%s"%time.time()
    m1=Mythread(work,(20,1,"线程1"))
    m2=Mythread(work,(40,0.5,"线程2"))
    m1.start()
    m2.start()
    m1.join()
    m2.join()
    print "主线程结束%s"%time.time()
    