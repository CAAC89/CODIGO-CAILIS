def menor_lista(lista):#para minimo
    if lista==[]:
        return False
    else:
        elmenor=lista[0]
    while lista!=[]:
        if lista[0]<=elmenor:
            elmenor=lista[0]
        lista=lista[1:]
    return elmenor
print menor_lista([2,5,3,7,7,2,3,2])
def mayor_lista(lista):#para maximo
    if lista==[]:
        return False
    else:
        elmayor=lista[0]
    while lista!=[]:
        if lista[0]>=elmayor:
            elmayor=lista[0]
        lista=lista[1:]
    return elmayor
print mayor_lista([2,5,3,7,7,2,3,2])
def sacar_ceros(lista):
    cont1=menor_lista(lista)-1
    cont2=mayor_lista(lista)
    nnum=[]
    while cont1<cont2:
        nnum.append(0)
        cont1=cont1-1
    return nnum
print sacar_ceros([2,5,3,7,7,2,3,2])

