from Tkinter import *

v0=Tk()

list1=Listbox(v0)
list1.pack()
mivalor=StringVar()
e1=Entry(v0,textvar=mivalor).pack()

def insertar_en_listbox():
    if mivalor.get() != "":
        list1.insert(END,mivalor.get())
    else: print "Por favor esciba alg?n texto"

b1=Button(v0,text="Insertar en Listbox",command=insertar_en_listbox).pack()

v0.mainloop()
