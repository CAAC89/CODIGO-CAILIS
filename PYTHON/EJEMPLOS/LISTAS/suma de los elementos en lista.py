lista=[1,2,3,4,5]
def suma_de_lista(lista):
    suma=0
    for i in range(0,len(lista)):
        suma=suma+lista[i]
    return suma
print suma_de_lista(lista)