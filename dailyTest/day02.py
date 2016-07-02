import threading
import time
class Mythread(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        pass
    
    def run(self):
        for i in range(0,20):
            print i,
            time.sleep(1)
            
if __name__=="__main__":
    
    m1=Mythread()
    m2=Mythread()
    m3=Mythread()
    
    m1.start()
    m2.start()
    m3.start()
    
    m1.join()
    m2.join()
    m3.join()
    
    print "all is done!"