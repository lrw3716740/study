#coding:utf-8
f=open("./2.txt","r+")
for l in f.readlines():
    if "http" in l:
        continue
    else:
        try:
            result=l.split(",")
            body=result[0].split("{")[1]
            print "***body****======%s"%body
        except:
            print "-----except:%s"%l