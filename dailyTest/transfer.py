#coding:utf-8

#query代表传入的字符串，keepblank代表是否反转空格的顺序
def transfer(query="",keepblank=True):

    query_list = []
    blank_list = []

    if query == "":
       return "query should not be empty"
    if " " not in query:
       return query

    word = ""
    blank = ""
    query = query.strip()
    for key in query:
        if key == " ":
           if word == "":
              blank = blank + key
           else:
              query_list.append(word)
              word = ""
              blank = blank + " "
        else:
           if blank == "":
              word = word + key
           else:
              blank_list.append(blank)
              blank = ""
              word = word + key
    if word != "":
       query_list.append(word)
    if blank != "":
       blank_list.append(blank)
    if len(query_list)-1 != len(blank_list):
       return "caculate error"
    else:
       result = ""
       for i in range(0,len(blank_list)):
          if keepblank:
             result = result + query_list[len(query_list)-i-1] + blank_list[i]
          else:
             result = result + query_list[len(query_list)-i-1] + blank_list[len(blank_list)-i-1]
       result = result + query_list[0]
       return result

if __name__ == '__main__':
   s = "i      am a yong boy from beijing   china"
   print s
   r = transfer(s,True)
   print r

