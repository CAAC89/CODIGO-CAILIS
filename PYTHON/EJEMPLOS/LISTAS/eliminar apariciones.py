def insertar_al_final(elemento,lista):
    if lista==[]:
        return [elemento]
    else:
        lista[-1:]=[lista,[-1],elemento]
        return lista
def eliminar_apariciones_lista(elemento,lista):
    nl=[]
    while lista!=[]:
        if lista[0]==elemento:
            lista=lista[1:]
        else:
            nl=insertar_al_final(lista[0],nl)
            lista=lista[1:]
    return nl
print eliminar_apariciones_lista(1,[1,2,3,4,5])