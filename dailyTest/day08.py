
#coding:utf-8

#实现一个得到验证码的功能。

import random
import code

def getVotifyCode(number=6):
    
    strList="0123456789abcdefghijklmnopqrstuvwxyz"
    code=""
    for i in range(0,number):
       
        code=code+strList[random.randint(0,len(strList)-1)]
    return code


if __name__=="__main__":
    
    print getVotifyCode()
    
