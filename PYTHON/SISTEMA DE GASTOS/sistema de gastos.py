# -*- coding: utf-8 -*-
#########bibliotecas#############
from Tkinter import *#modulo grafico para que el programa sea visto de una mejor manera
import pickle#utlizado para guardar en archivos,leer y cerrarlos etc
#################################
#listas son utilizas para guardar la informacion
Lista_Usuarios=[]
Lista_Gastos=[]
Lista_Ingresos=[]

##################################
#clases son abstracciones
class Usuario:
    def __init__(self):
        self.nombre=""
        self.cedula=""
        self.telefonos=""
        self.nombre_usuario=""
        self.contrasena=""
    def crear_nombre(self,nombre):
        self.nombre=nombre
    def info_nombre(self):
        return self.nombre
    def crear_cedula(self,cedula):
        self.cedula=cedula
    def info_cedula(self):
        return self.cedula
    def crear_telefonos(self,telefonos):
        self.telefonos=telefonos
    def info_telefonos(self):
        return self.telefonos
    def crear_NombreUsuario(self,nombre_usuario):
        self.nombre_usuario=nombre_usuario
    def info_NombreUsuario(self):
        return self.nombre_usuario
    def crear_contrasena(self,contrasena):
        self.contrasena=contrasena
    def info_contrasena(self):
        return self.contrasena
    def informacion_Usuario(self):
        return self.nombre,self.cedula,self.telefonos,self.nombre_usuario,self.contrasena
class Gastos:
    def __init__(self):
        self.fecha=""
        self.categoria_gasto=""
        self.descripcion_gasto=""
        self.monto=""
        self.usuario=""
    def crear_fecha(self,fecha):
        self.fecha=fecha
    def info_fecha(self):
        return self.fecha
    def crear_categoria_gasto(self,categoria_gasto):
        self.categoria_gasto=categoria_gasto
    def info_categoria_gasto(self):
        return self.categoria_gasto
    def crear_descripcion_gasto(self):
        self.descripcion_gasto=descripcion_gasto
    def info_categoria_gasto(self):
        return self.descripcion_gasto
    def crear_monto(self):
        self.monto=monto
    def info_monto(self):
        return self.monto
    def crear_usuario(self):
        self.usuario=usuario
    def info_usuario(self):
        return self.usuario
    def informacion_gastos(self):
        return self.fecha,self.categoria_gasto,self.descripcion_gasto,self.monto,self.usuario
class ingresos:
    def __init__(self):
        self.fecha=""
        self.categoria_ingreso=""
        self.monto=""
        self.usuario=""
    def crear_fecha(self,fecha):
        self.fecha=fecha
    def info_fecha(self):
        return self.fecha
    def crear_categoria_ingreso(self,categoria_ingreso):
        self.categoria_ingreso=categoria_ingreso
    def info_categoria_gasto(self):
        return self.categoria_ingreso
    def crear_monto(self):
        self.monto=monto
    def info_monto(self):
        return self.monto
    def crear_usuario(self,usuario):
        self.usuario=usuario
    def info_usuario(self):
        return self.usuario
    def informacion_ingresos(self):
        return self.fecha,self.categoria_ingreso,self.monto,self.usuario
###################################
#funciones
def ocultar(ventana):ventana.withdraw()
def mostrar(ventana):ventana.deiconify()
def SALIR_SISTEMA(): return exit()
def usuarios():
    global Lista_Usuarios
    f=open("Usuarios.txt","r")
    try:
        x=pickle.load(f)
        Lista_Usuarios=x
    except:
        Lista_Usuarios=[]

    ind=Usuario()
    Nombre=campo1.get()
    if Nombre!=[]:
        ind.crear_nombre(Nombre)
    Cedula=campo2.get()
    if Cedula!=[]:
        ind.crear_cedula(Cedula)
    Telefonos=campo3.get()
    if Telefonos!=[]:
        ind.crear_telefonos(Telefonos)
    Nombre_Usuario=campo4.get()
    if Nombre_Usuario!=[]:
        ind.crear_NombreUsuario(Nombre_Usuario)
    Contrasena=campo5.get()
    if Contrasena!=[]:
        ind.crear_contrasena(Contrasena)
    f=open("Usuarios.txt","w")
    pickle.dump(Lista_Usuarios,f)
    f.close()
#Interfaz grafica
def registrar_usuarios():
    V_REGISTRAR=Tk()
    V_REGISTRAR.geometry("440x250")
    V_REGISTRAR.config(bg="black")
    V_REGISTRAR.title("REGISTRAR USUARIOS")

    Label1_registrar=Label(V_REGISTRAR,text="NOMBRE: ").grid(row=1,column=0)
    Label2_registrar=Label(V_REGISTRAR,text="CEDULA: ").grid(row=2,column=0)
    Label3_registrar=Label(V_REGISTRAR,text="TELEFONOS: ").grid(row=3,column=0)
    Label4_registrar=Label(V_REGISTRAR,text="NOMBRE DE USUARIO: ").grid(row=4,column=0)
    Label5_registrar=Label(V_REGISTRAR,text="CONTRASEÑA").grid(row=5,column=0)

    Textbox1_registrar=Entry(V_REGISTRAR,width=25).grid(row=1,column=1)
    Textbox2_registrar=Entry(V_REGISTRAR,width=25).grid(row=2,column=1)
    Textbox3_registrar=Entry(V_REGISTRAR,width=25).grid(row=3,column=1)
    Textbox4_registrar=Entry(V_REGISTRAR,width=25).grid(row=4,column=1)
    Textbox5_registrar=Entry(V_REGISTRAR,width=25).grid(row=5,column=1)

    boton1_registrar=Button(V_REGISTRAR,text="DEVOLVER A MENU PRINCIPAL",command=lambda:ocultar(V_REGISTRAR) or mostrar(V_PRINCIPAL) )
    boton1_registrar.grid(row=7,column=1)

    boton2_registrar=Button(V_REGISTRAR,text="REGISTRADO",command=lambda:usuarios())
    boton2_registrar.grid(row=7,column=3)

    V_REGISTRAR.mainloop()

def ingresar():
    V_INGRESAR=Tk()
    V_INGRESAR.geometry("440x200")
    V_INGRESAR.config(bg="black")
    V_INGRESAR.title("INGRESAR AL SISTEMA")

    Label1_ingresar=Label(V_INGRESAR,text="NOMBRE DE USUARIO: ").grid(row=1,column=0)
    Label2_ingresar=Label(V_INGRESAR,text="CONTRASEÑA").grid(row=2,column=0)

    Textbox1_ingresar=Entry(V_INGRESAR,width=25).grid(row=1,column=1)
    Textbox2_ingresar=Entry(V_INGRESAR,width=25).grid(row=2,column=1)

    boton1_registrar=Button(V_INGRESAR,text="DEVOLVER A MENU PRINCIPAL",command=lambda: ocultar(V_INGRESAR) or mostrar(V_PRINCIPAL))
    boton1_registrar.grid(row=5,column=1)

    boton2_registrar=Button(V_INGRESAR,text="INGRESAR AL SISTEMA")
    boton2_registrar.grid(row=5,column=3)

    V_INGRESAR.mainloop()

def SALIR():
    SALIR=Tk()
    SALIR.geometry("440x220")
    SALIR.title("SALIR DEL SISTEMA")

    label1_salir=Label(SALIR,text="¿DESEAS SALIR DE LA APLICACION GASTOS?").grid(row=2,column=1)
    label1=Label(SALIR,text="¿DESEAS SALIR DE LA APLICACION JUEGO?  ").grid(row=2,column=1)

    b1=Button(SALIR,text="NO",command=lambda :mostrar(ocultar(SALIR) or mostrar(V_PRINCIPAL)) ).grid(row=4,column=3)
    b2=Button(SALIR,text="SI",command=lambda :salir_sistema()).grid(row=4,column=6)

V_PRINCIPAL=Tk()
IMAGEN_PRINCIPAL=PhotoImage(file="TEC.gif")
LABEL_PRINCIPAL = Label(V_PRINCIPAL, image=IMAGEN_PRINCIPAL)
LABEL_PRINCIPAL.grid(row=1,column=1)
V_PRINCIPAL.title("SISTEMA DE CONTROL DE GASTOS")
V_PRINCIPAL.geometry("480x300")
V_PRINCIPAL.config(bg="black")
boton_registrar=Button(V_PRINCIPAL,text="REGISTRAR USUARIO",command=lambda: ocultar(V_PRINCIPAL) or registrar_usuarios())
boton_registrar.grid(row=12,column=0)

boton_ingresar=Button(V_PRINCIPAL,text="INGRESAR AL SISTEMA",command=lambda:ocultar(V_PRINCIPAL) or ingresar())
boton_ingresar.grid(row=12,column=1)

boton_salir=Button(V_PRINCIPAL,text="SALIR DEL SISTEMA",command=lambda:SALIR())
boton_salir.grid(row=12,column=2)

boton_modificar=Button(V_PRINCIPAL,text="MODIFICAR INFORMACION")
boton_modificar.grid(row=13,column=0)

boton_baja=Button(V_PRINCIPAL,text="DARSE DE BAJA")
boton_baja.grid(row=13,column=1)

V_PRINCIPAL.mainloop()
