# -*- coding: utf-8 -*-
from Tkinter import *

v0=Tk()
v0.resizable(0,0)
v0.title("Dos Listbox")
gsel=StringVar()
switch=[0]

def llenar_listbox(lista,listbox):
    ind,largo=0,len(lista)
    while listbox.size() > 0: # Un while para limpiar el listbox
        listbox.delete(0)
    while ind < largo: # Un while que inserta todos los elementos en una lista
        listbox.insert(END,lista[ind])
        ind+=1

def vargrupo():
    v0.after(200,vargrupo)
    if l2.curselection() != ():
        print l2.get(l2.curselection())
    if l1.curselection() != ():
        gsel.set(l1.get(l1.curselection()))
    if gsel.get() == "Computacion":
        llenar_listbox(Compu,l2)
    if gsel.get() == "Agronomia":
        llenar_listbox(Agro,l2)
    if gsel.get() == "Administracion":
        llenar_listbox(Turistas,l2)
    if gsel.get() == "Turismo":
        llenar_listbox(Admin,l2)

ListaCarreras=["Computacion","Agronomia", "Administracion","Turismo"]
Compu=["Ana","Alejandra","Ronald","Andrey"]
Agro=["Jefry"]
Turistas=["Laura","Jose María"]
Admin=["Andrea","Roberta"]

l1=Listbox(v0)
l1.grid(row=1,column=0)
l2=Listbox(v0)
l2.grid(row=1,column=1)
b1=Button(v0,text="SALIR",width=40,command=v0.destroy)
b1.grid(row=2,column=0,columnspan=2)

vargrupo()
llenar_listbox(ListaCarreras,l1)
v0.mainloop()

