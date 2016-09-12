def insertar_al_final(elemento,lista):
    if lista==[]:
        return [elemento]
    else:
        lista[-1:]=[lista[-1],elemento]
        return lista
def elimina_por_primera_letra(letra,lista):
    nl=[]
    while lista!=[]:
        if lista[0][0]==letra:
            lista=lista[1:]
        else:
            nl=insertar_al_final(lista[0],nl)
            lista=lista[1:]
    return nl
print elimina_por_primera_letra("s",["hola","sandia","arroz","sandra","fabiola","sorbeto"])