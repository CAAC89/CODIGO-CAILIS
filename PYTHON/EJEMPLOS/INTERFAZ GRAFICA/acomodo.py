from Tkinter import *

v0=Tk()
v0.geometry("200x200")

b1=Button(v0,text="ARRIBA")
b1.pack(side=TOP)
b3=Button(v0,text="ABAJO")
b3.pack(side=BOTTOM)
b2=Button(v0,text="IZQUIERDO")
b2.pack(side=LEFT)
b4=Button(v0,text="DERECHO")
b4.pack(side=RIGHT)

v0.mainloop()

