import time
from datetime import datetime as d

path="C:\Windows\System32\drivers\etc\hosts"

direct="127.0.0.1"

l=[]

n=int(input("Enter the number of website to be blocked:")) 
print("Enter the URL of the website to be blocked") 
for i in range(n):
     x=input() 
     l.append(x)
if d(d.now().year,d.now().month,d.now().day,10)<d.now()<d(d.now().year,d.now().month,d.now().day,15):
        print("WEbsite blocked")
        with open(path, 'r+') as file:
             c=file.read()
             for i in l:
                if i in c:
                    pass
                else:
                    file.write("\t"+direct+"\t"+i+"\n")
else: 
    with open(path, 'r+') as file: 
                 c=file.readlines() 
                 file.seek(0)    
                 for line in c:
                      if not any(website in line for website in l):
                           file.write(line) 
                 file.truncate()
                 print("Fun hours...")
