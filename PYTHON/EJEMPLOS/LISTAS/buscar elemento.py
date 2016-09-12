lista=[1,2,3,4]
elemento=3
def buscarElemento(lista, elemento):
   for i in range(0,len(lista)):
    	     if(lista[i] == elemento):
                        return i
print buscarElemento(lista,elemento)