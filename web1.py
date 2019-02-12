from tkinter import *
import time
from datetime import datetime as dt
window= Tk()

e1_value=StringVar()
e1= Entry(window,textvariable=e1_value)
e1.grid(row=0,column=3)
hosts_temp =e1_value.get()
hosts_path="C:/Windows/WinSxS/amd64_microsoft-windows-w..ucture-other-minwin_31bf3856ad364e35_10.0.17134.1_none_1ac029cdce3c581c/hosts"
redirect ="127.0.0.1"
website_list =["wwww.facebook.com", "facebook.com"]
def final():
  while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,20) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,00):
        print("working hours...")
        with open (hosts_temp , "r+") as file:
            content = file.read()
            for webs in website_list:
                if webs in content :
                    pass
                else:
                    file.write(redirect +" " + webs+"\n")
    else:
        with open(hosts_temp , 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any (web in line for web in website_list):
                    file.write(line)
                file.truncate()
            print("fun hours..")
    time.sleep(5)
b= Button(window,text="block",command = final)
b.grid(row=0,column=2)


window.mainloop()

       