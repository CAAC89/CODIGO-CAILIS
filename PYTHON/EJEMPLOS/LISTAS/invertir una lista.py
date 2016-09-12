def cons(elemento,lista):
    lista[0:0]=[elemento]
    return lista
def invertir_lista(lista):
    li=[]
    while lista!=[]:
        li=cons(lista[0],li)
        lista=lista[1:]
    if lista==[]:
        return li
print invertir_lista([1,2,3,4,5,6])