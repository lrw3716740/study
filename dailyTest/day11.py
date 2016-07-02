import requests

r=requests.get("https://www.baidu.com")
print r.content
#print r.status_code