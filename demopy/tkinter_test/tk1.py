# coding:utf8

from tkinter import *  

root = Tk()
Label(root, text="Anage: ").pack(side=LEFT, padx=5, pady=10)
e = StringVar() 
Entry(root, width=40, textvariable=e).pack(side=LEFT)
e.set("A shore! Ashroe! My dingkom for a shroe! nihao wangshengyun zhongqiujiekuaile")



# -----------------------------------------------------------
# Radiobutton(root, text, value, variable, indicatoron).ack(anchor,fill,ipadx)
# -----------------------------------------------------------
var = IntVar() 
for text, value in [ ('Red Leicestest', 1), ('Tilsit', 2), ('Caerphilly', 3),
                    ('Stilton', 4), ('Emental', 5), ('Roquefort', 6), ('bride', 7)]:
    Radiobutton(root, text = text, value=value, variable=var, indicatoron=0).ack(
        anchor=W, fill= X, ipadx=18)
var.set(3) 


mainloop()