from Tkinter import *

v0=Tk()
mitexto=StringVar()
label1=Label(v0,textvar=mitexto).pack()

escribir=raw_input("")
mitexto.set(escribir)

v0.mainloop()
