#coding:utf-8
import threading
import time
class Mythread(threading.Thread):
    
    def __init__(self,function,args):
        threading.Thread.__init__(self)
        self.function=function
        self.args=args
        
    def run(self):
        
        apply(self.function,self.args)
        
    
    
def sayHello(name):
    
    for i in range(0,30):
        print "第%s次，hello  %s"%(i,name)
        time.sleep(1)
        
def introduce(name,age,t):
    
    for i in range(0,30):
        print "第%s次，我名字是%s,年龄是%s"%(i,name,age)
        time.sleep(t)

if __name__=="__main__":
    
    m1=Mythread(sayHello,("jim",))
    m2=Mythread(introduce,("eason",20,1,))
    m3=Mythread(introduce,("刘德华",50,0.5,))
    
    m1.start()
    m2.start()
    m3.start()
    
    m1.join()
    m2.join()
    #m3.join()
    
    print "主线程结束！！！"
    
    
    