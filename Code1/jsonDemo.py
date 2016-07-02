#coding:utf-8
import json
import requests

data='{"name":"李仁伟","age":12}'
data1=json.loads(data)
#data2=json.dumps(data1,indent=4,ensure_ascii=False)
data2=json.dumps(data1,indent=4,ensure_ascii=False)
print data1
print data2