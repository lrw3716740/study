import thread
import time
def printTime(th_name,delay):
    
    for i in range(0,10):
        print "%s ---> %s"%(th_name,i)
        time.sleep(delay)
        
    
try:
    thread.start_new_thread(printTime,("t1",0.5,))
    thread.start_new_thread(printTime,("t2",0.5))
    thread.start_new_thread(printTime,("t3",1))
    time.sleep(10)
except Exception,e:
    print e
        
    