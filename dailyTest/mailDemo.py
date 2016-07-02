#coding:utf-8
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
  
sender = 'lirw@chanjet.com'  
receiver = ['lirw@chanjet.com',]
subject = 'python email test'  
smtpserver = 'EXCHANGE01.chanjet.com'  
username = 'lirw@chanjet.com'  
password = '3716740'  
  
msg = MIMEText('</pre>你好<pre>','html','utf-8')  
#msg['Subject'] = Header(subject, 'utf-8')  
msg['Subject'] = subject 
  
smtp = smtplib.SMTP()  
smtp.connect(smtpserver)  
smtp.starttls()
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  