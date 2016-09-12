from Tkinter import * # Importa el m?dulo

v0 = Tk() # Tk() Es la ventana principal
v1=Toplevel(v0) # Crea una ventana hija
v1.protocol("WM_DELETE_WINDOW", "onexit") # Elimina la opci?n de salir para evitar el error
v0.resizable(0,0) # Evita que la ventana se pueda cambiar de tama?o
v1.resizable(0,0) # Evita que se le pueda cambiar de tama?o a la ventana

def mostrar(ventana): ventana.deiconify() # Muestra una ventana
def ocultar(ventana):ventana.withdraw() # Oculta una ventana
def ejecutar(f): v0.after(200,f) # Una forma de ejecutar las funciones
def imprimir(texto): print texto # Imprime un texto

v0.config(bg="black") # Le da color al fondo
v0.geometry("500x500") # Cambia el tama?o de la ventana

b1=Button(v0,text="ABRIR VENTANA V1",command=lambda: ejecutar(mostrar(v1)) or imprimir("hola") or imprimir("tercera funci?n")) # Primer bot?n
b1.grid(row=1,column=1) # El bot?n es cargado
b2=Button(v1,text="OCULTARME",command=lambda: ejecutar(ocultar(v1))) # Segundo bot?n
b2.grid(row=1,column=2) # El bot?n es cargado

b3=Button(v0,text="OCULTAR VENTANA V1",command=lambda: ejecutar(ocultar(v1)))
b3.grid(row=1,column=2) # El bot?n es cargado

v1.withdraw() # Oculta la ventana v1
v0.mainloop() # Es el evento que llama al inicio de nuestro programa.