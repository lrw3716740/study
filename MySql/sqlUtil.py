#coding:utf-8
import MySQLdb

class sqlUtil:
    
    def __init__(self,host,username,password,DBname):
        
        self.host=host
        self.username=username
        self.password=password
        self.DBname=DBname
        self.con=MySQLdb.connect(host=self.host,username=self.username,password=self.password,db=self.DBname,charset="utf8")
        self.cursor=self.con.cursor()
        
        
        
    def excuteSql(self,sql):
        
        self.cursor.excute(sql)