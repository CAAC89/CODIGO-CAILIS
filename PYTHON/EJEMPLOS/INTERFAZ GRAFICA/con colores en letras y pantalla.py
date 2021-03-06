from Tkinter import *

v0=Tk()
v0.config(bg="black")
v0.title("Ejemplo personalizado")
v0.geometry("210x190")

def colocar_scrollbar(listbox,scrollbar):
    scrollbar.config(command=listbox.yview)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.pack(side=LEFT, fill=Y)

frame1=Frame(v0,bg="black")
frame1.pack()
scroll1=Scrollbar(frame1)
list1=Listbox(frame1,bg="black",fg="white")
list1.pack()
colocar_scrollbar(list1,scroll1)
mitexto=StringVar()
label1=Label(v0,textvar=mitexto,bg="black",fg="white")
label1.pack()
b1=Button(v0,text="ELIMINAR TODOS",command=lambda: limpiar_listbox(list1),bg="black",fg="white")
b1.pack()

def cargarlistbox(lista,listbox):
    ind,largo=0,len(lista)
    while ind < largo:
        listbox.insert(END,lista[ind])
        ind+=1

ListaNombres=['Laura','Roger','Fabiola','Yendry','Esteban','Marta','Elias']

def imprimir_en_label():
    label1.after(100, imprimir_en_label) # Llamada recursiva con .after
    ind = list1.curselection()
    if list1.curselection() != ():
        sel = list1.get(ind)
        mitexto.set(sel)

def limpiar_listbox(listbox):
    while listbox.size() > 0:
        listbox.delete(0)

cargarlistbox(ListaNombres,list1)
imprimir_en_label()

v0.mainloop()
