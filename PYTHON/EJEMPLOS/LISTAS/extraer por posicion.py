def extraer_por_posicion(posicion,lista):
    ind=0
    while lista!=[]:
        if posicion==ind+1:
            return lista[0]
            break
        else:
            lista=lista[1:]
            ind=ind+1
    if lista==[]:
        return"no existe el elemento de la lista"
print extraer_por_posicion(1,[1,2,3,4,5,6])