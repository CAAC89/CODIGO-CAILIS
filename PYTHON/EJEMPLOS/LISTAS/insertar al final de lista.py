def insertar_al_final(elemento,lista):
    if lista==[]:
        return [elemento]
    else:
        lista[-1:]=[lista[-1],elemento]
        return lista
print insertar_al_final("hola",[1,2,3,4,5])
