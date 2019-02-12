# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 18:29:17 2019

@author: DELL
"""

import json
from difflib import get_close_matches as g
from tkinter import *
data =json.load(open("D:/blo/data.json"))
window= Tk()
t1= Text(window, height =10, width= 35)
t1.grid(row=3,column = 0)
w="sorry wrong word"
def translate(word):
    word=word.lower()
    t1.insert(END,data(word))
def condition(word):
    if word in data:
       return condition(word)
    elif len(g(word, data.keys()))>0:
        e1=Entry(window)
        if e1.get() == "y" :
            return condition(data[g(word,data.keys()[0])])
        elif e1.get() == "n" :
           
           return w
        else:
           return w
    else:
         return w
e2=Entry(window)
e2.grid(row=0,column=0)
def final():
     
     word=e2.get()

     output = condition(word)
     if type(output) == list:
         for item in output:
             t1.insert(END,item)
     else:
        t1.insert(END,output)

b= Button(window,text="TRANSLATE",command = final)
b.grid(row=0,column=2)
window.mainloop()

        
