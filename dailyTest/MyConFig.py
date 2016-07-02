import ConfigParser
configPath="./test.conf"
import logging

class MyConfig:
    
    def __init__(self,section_name="inte",configPath=configPath):
        self.section_name=section_name
        self.con=ConfigParser.ConfigParser()
        self.con.read(configPath)
        
    def getIp(self,option="ip"):
        return self.con.get(self.section_name,"ip")
    
    def getStr(self,str):
        return self.con.get(self.section_name,str)
    def getPort(self):
        port=self.con.get(self.section_name,"port")
        if port=="":
            raise NameError("port is null")
        return port
if __name__=="__main__":
    my=MyConfig()
    #print my.getIp()
    #print my.getStr("username")
    print my.getPort()
    
        
        
        