import pickle

def guardar_lista(lista,ruta):
    fichero = file(ruta, "w")
    nl=lista
    pickle.dump(nl, fichero)

def cargar_lista(ruta):
    fichero = file(ruta)
    lista_recuperada = pickle.load(fichero)
    return lista_recuperada

guardar_lista([1,2,3,4,5,6,7],"datos.txt")
print cargar_lista("datos.txt")
