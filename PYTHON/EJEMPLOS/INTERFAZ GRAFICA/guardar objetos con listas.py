import pickle

def guardar_lista(lista,ruta):
    fichero = file(ruta, "w")
    nl=lista
    pickle.dump(nl, fichero)

def cargar_lista(ruta):
    fichero = file(ruta)
    lista_recuperada = pickle.load(fichero)
    return lista_recuperada

class persona:
    def __init__(self,nombre):
        self.nombre=nombre
        print "Ha nacido",nombre

Roxana=persona("Roxana")

ListaPersonas=[Roxana]
print "Esta es ListaPersonas:",ListaPersonas

guardar_lista(ListaPersonas,"C:\salvaobjetos.txt")
ListaPersonas2 = cargar_lista("C:\salvaobjetos.txt")
print "Esta es ListaPersonas2",ListaPersonas2

print "Nombre de primer elemento en ListaPersonas:",ListaPersonas[0].nombre
print "Nombre de primer elemento en ListaPersonas2:",ListaPersonas2[0].nombre
