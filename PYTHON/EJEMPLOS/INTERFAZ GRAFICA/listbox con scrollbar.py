from Tkinter import *

v0=Tk()

def colocar_scrollbar(listbox,scrollbar):
    scrollbar.config(command=listbox.yview)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.pack(side=LEFT, fill=Y)

frame1=Frame(v0)
frame1.pack()
scroll1=Scrollbar(frame1)
list1=Listbox(frame1)
list1.pack()
colocar_scrollbar(list1,scroll1)
mivalor=StringVar()
e1=Entry(v0,textvar=mivalor).pack()

def insertar_en_listbox():
    if mivalor.get() != "":
        list1.insert(END,mivalor.get())
    else: print "Por favor esciba alg?n texto"

b1=Button(v0,text="Insertar en Listbox",command=insertar_en_listbox).pack()

v0.mainloop()
