def insertar_al_final(elemento,lista):
    if lista==[]:
        return [elemento]
    else:
        lista[-1:]=[lista[-1],elemento]
        return lista
def lista_pares(lista):
    nueva_lista=[]
    for xpalabra in lista:
        if xpalabra %2==0:
            nueva_lista=insertar_al_final(xpalabra,nueva_lista)
    return nueva_lista
print lista_pares([1,2,3,4,5,6,7,8])