from Tkinter import *

v0=Tk()
v0.geometry("200x200")

l1=Label(v0,text="BIENVENIDO AL PROYECTO")
l1.pack()

frame0=Frame(v0)
frame0.pack(side=TOP)

frame1=Frame(frame0)
Label(frame1,text="T e x t o").pack()
Label(frame1,text="T e x t o").pack()
Label(frame1,text="T e x t o").pack()
Label(frame1,text="T e x t o").pack()
Label(frame1,text="T e x t o").pack()
frame1.pack(side=LEFT)

frame2=Frame(frame0)
Label(frame2,text="o t x e T").pack()
Label(frame2,text="o t x e T").pack()
Label(frame2,text="o t x e T").pack()
Label(frame2,text="o t x e T").pack()
Label(frame2,text="o t x e T").pack()
frame2.pack(side=RIGHT)

v0.mainloop()
