#coding:utf-8
import requests
import hashlib
import json



def getCustomerHeader():

    url = "http://cia.csp.chanapp.com/internal_api/client_authentication_with_userInfo"


    #username="customer_test06@qq.com"
    #password="111111"
    #username="1814364817@qq.com"
    #password="123456"
    username="lilyishu010@163.com"
    password="111111"
    h=hashlib.md5()
    h.update(password)
    pwd=h.hexdigest()
    params={"client_id":"newapp",
        "client_secret":"secret",
        "auth_username":username,
        "password":pwd,}


    result=requests.get(url,params=params)
    print result.content
    result=json.loads(result.content)
    token=result["access_token"]
    header={}
    header["Device-Searal"]='121212'
    header["Device-Type"]='Android'
    header["Content-Type"]='application/json'
    header["App-Short-Name"]='customer'
    header["Item-Short-Name"]='customer'
    header["App-Version"]='1.3.3.0'
    header["Token"]=token
    print header
    return header


def test_cus_getCustomer_success():
        headers =getCustomerHeader()
        params = {
                "first":"0",
                "max":"25",
                "keyword":"",
                 }
        #url = "http://urlps3jfnq0l.chanapp.com"+"/chanjet/customer/restlet/mobile/Customer"
        url = "http://upjb22mw440r.chanapp.com"+"/chanjet/customer/restlet/mobile/Customer"
        
        #url="http://58.83.201.102"+"/chanjet/customer/restlet/mobile/Customer"

        print url
        result = requests.get(url,params=params,headers=headers)
        print result.status_code
        print checkJson(result.content)
        
def checkJson(jstr):
        if jstr.startswith("<"):
            print jstr
            return jstr
        else:
            try:
                jsonstr = json.loads(jstr)
                return json.dumps(jsonstr,indent=4,ensure_ascii=False)
            except:
                print "****************返回格式有问题！"
                print jstr

if __name__=="__main__":
    
    test_cus_getCustomer_success()
    
    
    