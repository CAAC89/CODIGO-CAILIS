lista=[2,4,1,6,1,3]
def menor_lista(lista):
    elmenor=lista[0]
    while lista!=[]:
        if lista[0]<=elmenor:
            elmenor=lista[0]
        lista=lista[1:]
    return elmenor

def contar(lista):
    el_menor=menor_lista(lista)
    cont=0
    while lista!=[]:
        if el_menor==lista[0]:
            cont=cont+1
        lista=lista[1:]
    return cont

nl=[menor_lista(lista),contar(lista)]
print nl

