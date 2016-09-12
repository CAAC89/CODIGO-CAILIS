# -*- coding: utf-8 -*-
from Tkinter import *

v0=Tk()
v0.resizable(0,0)
v0.title("GRID")

Button(v0,width=25,height=7).grid(row=0,column=0,rowspan=2)
Button(v0,width=25,height=7).grid(row=1,column=0,rowspan=2)
Button(v0,width=25,height=7).grid(row=0,column=1)
Button(v0,width=25,height=7).grid(row=1,column=1)
Button(v0,width=25,height=7).grid(row=2,column=1)
Button(v0,width=25,height=7).grid(row=0,column=2,rowspan=2)
Button(v0,width=25,height=7).grid(row=1,column=2,rowspan=2)


v0.mainloop()
