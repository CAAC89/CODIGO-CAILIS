# -*- coding: utf-8 -*-
from Tkinter import *

v0=Tk()
v0.resizable(0,0)
v0.title("FORMULARIO")
Label(v0,text="Formulario de Contacto",width=50).grid(row=0,column=0,columnspan=4)
Label(v0,text="Nombre: ").grid(row=1,column=0,sticky=W)
Entry(v0).grid(row=1,column=2)
Label(v0,text="Email: ").grid(row=2,column=0,sticky=W)
Entry(v0).grid(row=2,column=2)
Label(v0,text="Teléfono: ").grid(row=3,column=0,sticky=W)
Entry(v0).grid(row=3,column=2)
Label(v0,text="Profesión: ").grid(row=4,column=0,sticky=W)
Entry(v0).grid(row=4,column=2)
Label(v0,text="Cédula: ").grid(row=5,column=0,sticky=W)
Entry(v0).grid(row=5,column=2)
l1=Listbox(v0,height=6)
l1.grid(row=0,column=3,rowspan=20)
l1.insert(END,"Costa Rica"),l1.insert(END,"Croacia"),l1.insert(END,"Estados Unidos")
Button(v0,text="Registrar",width=50).grid(row=10,column=0,columnspan=4)

v0.mainloop()
