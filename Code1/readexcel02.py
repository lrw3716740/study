#coding:utf-8
import time
import xlrd
from pylab import *  
import dateutil, pylab,random
from matplotlib import pyplot
def GetTime(tuList):
    rel=[]
    for i in tuList:
        if type(i)==tuple:
            s="%s-%s"%(i[0],i[1])
            rel.append(s)
        else:
            rel.append(i)
    return rel
def open_excel(file= 'file.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
        
#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file= 'file.xlsx',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    #print nrows,ncols
    colnames =  table.row_values(colnameindex) #某一行数据 
    country_list=[]
    date_list=[]
    result_list=[]
    row = table.row_values(0)
    time_tu=[]
    
    #得到时间列表
    for i in range(1,len(row)/2+1):
        try:
            
            time_tu.append(xlrd.xldate_as_tuple(row[2*i-1], 0))
            
        except:
            
            time_tu.append( row[2*i-1])
    date_list=GetTime(time_tu)
        
    #
    for rownum in range(2,nrows):
        reli_list=[]
        _number_list=[]
        _price_list=[]
        app=[]
        row = table.row_values(rownum)
        if row:
            country_list.append(row[0])#得到国家列表。
            for i in range(1,(len(colnames)+1)/2):
                 
                _number_list.append(row[2*i-1])
                _price_list.append(row[2*i])
                
            reli_list=[_number_list,_price_list]
        
        result_list.append(reli_list)
    return country_list,date_list,result_list
    
#excel_table_byindex(file='F:\liumi\data\No29gb.xlsx',colnameindex=2,by_index=3)

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= './N029gb.xlsx',colnameindex=2,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list
#excel_table_byname(file=F:\liumi\data\No29gb.xlsx',colnameindex=2,by_name=u'29011000')
def main():
    tables = excel_table_byindex(file='./N029gb.xlsx',colnameindex=0,by_index=3)
    
    x=tables[1]
    print x
    y=tables[2][0][0]
    
    print len(x),len(y)
    
    
if __name__=="__main__":
    main()
    
    
    
    
    
    