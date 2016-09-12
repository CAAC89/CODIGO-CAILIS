from Tkinter import * # Importa el m?dulo

v0 = Tk() # Tk() Es la ventana principal
v0.config(bg="black") # Le da color al fondo
v0.geometry("500x500") # Cambia el tama?o de la ventana

v1=Toplevel(v0) # Crea una ventana hija

v1.withdraw()  # oculta v1
v0.mainloop()