
# coding:utf-8
def getFirstChar(s):
    
    print type(s)
    if type(s) == 'str':
        print "输入只能是字符串"
        return 
    
    else:
        for i in s:
            num = 0
            for j in s:
                if j == i:
                    num = num + 1
            if num == 1:
                return i
            
            
            
if __name__ == "__main__":
    
    print getFirstChar("4131255551")
