
# -*- coding: utf-8 -*-
from Tkinter import *

v0=Tk()
v0.resizable(0,0)
v0.title("OBJETOS")

def crear_botones(n):
    ind,acumulador,fila,columna=1,0,0,0
    while ind <= n:
        Button(v0,text=" " + str(ind) + " ",width=2).grid(row=fila,column=columna)
        if acumulador==39: fila,columna,acumulador=fila+1,0,0
        else: acumulador,columna=acumulador+1,columna+1
        ind+=1

crear_botones(600)
v0.mainloop()
