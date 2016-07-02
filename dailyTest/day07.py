import subprocess
import os
Scmd="ipconfig"
def getIp():
    
    result=subprocess.Popen(Scmd,stdout=subprocess.PIPE)
    result.wait()
    print (result.stdout.read())
    
def osGetIp():
    p=os.popen(Scmd)
    print p.read()
if __name__=="__main__":
    getIp()
    #osGetIp()
    
    