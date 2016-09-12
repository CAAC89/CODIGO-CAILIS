lista=[1,2,3,4]
indice=1
elemento=0
def insertarElemento(lista, indice, elemento):
   lista.insert(indice,elemento)
   return lista
print insertarElemento(lista,indice,elemento)