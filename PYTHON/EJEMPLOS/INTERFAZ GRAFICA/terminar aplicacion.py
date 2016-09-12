from Tkinter import *

v0=Tk()
v1=Toplevel(v0)

def mostrar(ventana): ventana.deiconify()
def ocultar(ventana):ventana.withdraw()
def ejecutar(f): v0.after(200,f)

b1=Button(v0,text="TERMINAR APLICACI?N",command=v0.destroy).pack()
b2=Button(v1,text="OCULTAR VENTANA",command=lambda: ejecutar(ocultar(v1))).pack()

v0.mainloop()
