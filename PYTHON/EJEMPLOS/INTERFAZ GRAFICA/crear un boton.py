from Tkinter import * # Importa el m?dulo

v0 = Tk() # Tk() Es la ventana principal
v0.config(bg="black") # Le da color al fondo
v0.geometry("500x500") # Cambia el tama?o de la ventana
b1=Button(v0,text="ABRIR VENTANA V1") # Primer bot?n
b1.pack() # El bot?n es cargado

v1=Toplevel(v0) # Crea una ventana hija

v1.withdraw() # Oculta la ventana v1
v0.mainloop() # Es el evento que llama al inicio de nuestro programa. Siempre lo lleva la ventana principal.
