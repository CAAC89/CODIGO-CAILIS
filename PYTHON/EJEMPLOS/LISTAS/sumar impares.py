lista=[1,2,3,4]
def sumar_impares(lista):
    suma=0
    for i in range(0,len(lista)):
        if lista[i]%2!=0:
            suma=suma+lista[i]
    return suma
print sumar_impares(lista)