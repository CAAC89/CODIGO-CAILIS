from Tkinter import *

v0=Tk()
v0.geometry("200x200")

b1=Button(v0,text="ARRIBA").pack(side=TOP)
b2=Button(v0,text="IZQUIERDO").pack(side=LEFT)
b3=Button(v0,text="ABAJO").pack(side=BOTTOM)
b4=Button(v0,text="DERECHO").pack(side=RIGHT)

v0.mainloop()
