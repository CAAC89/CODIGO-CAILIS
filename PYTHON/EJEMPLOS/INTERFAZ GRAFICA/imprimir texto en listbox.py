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
mitexto=StringVar()
label1=Label(v0,textvar=mitexto)
label1.pack()

def cargarlistbox(lista,listbox):
    ind,largo=0,len(lista)
    while ind < largo:
        listbox.insert(END,lista[ind])
        ind+=1

ListaNombres=['Laura','Roger','Fabiola']

def imprimir_en_label():
    label1.after(100, imprimir_en_label) # Llamada recursiva con .after
    ind = list1.curselection()
    if list1.curselection() != ():
        sel = list1.get(ind)
        mitexto.set(sel)

cargarlistbox(ListaNombres,list1)
imprimir_en_label()

v0.mainloop()
