#coding:utf-8
import Queue
import threading
import time
#q=Queue.LifoQueue()  这样的队列是先进后出
q=Queue.Queue()
qlock=threading.Lock()
nameList=["李仁伟","刘德华","陈奕迅","王菲","谢安琪"]
for name in nameList:
    q.put(name)

def getData(q,name):
    #qlock.acquire()
    if  not q.empty():
        data=q.get()
        print "%s 获得了 %s"%(name,data)
        #qlock.release()
class MyThread(threading.Thread):
    
    def __init__(self,q,name):
        threading.Thread.__init__(self)
        self.q=q
        self.name=name
    
    def run(self):
        for i in range(0,10):
            getData(self.q,self.name)
'''print q.qsize() 
while not q.empty():
    print q.get()
print q.qsize()'''
        
if __name__=="__main__":
    m1=MyThread(q,"线程A")
    m2=MyThread(q,"线程B")
    m1.start()
    m2.start()