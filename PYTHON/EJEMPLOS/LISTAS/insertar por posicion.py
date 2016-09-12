def insertar_por_posicion(elemento,posicion,lista):
    posicion=posicion-1
    lista[posicion:posicion]=[elemento]
    return lista
print insertar_por_posicion("ELEMENTO",1,[0,1,2,3,4,5])