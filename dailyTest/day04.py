#coding:utf-8
import threading
import thread

tlock=threading.Lock()
num=0
class Mythread(threading.Thread):
    
    
    
    def run(self):
        
        global num
        
        if  tlock.acquire(1):
            
            num=num+1
            msg=self.name+'set num to '+str(num+1)
            
            print msg
            tlock.release()
            
def test():
    for i in range(0,10):
        t=Mythread()
        t.start()
        t.join()    
if __name__=="__main__":
    
    test()
    print "主线程已经结束"
    print thread.name
    
    
            
            
            
        
        
    
    