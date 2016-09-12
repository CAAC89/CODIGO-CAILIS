lista=[1,2,3,4,5]
def suma_pares(lista):
    suma=0
    for i in range(0,len(lista)):
        if i % 2 == 0:
            suma=suma+lista[i]
    return suma
print suma_pares(lista)

def suma_impares(lista):
    suma=0
    for i in range(0,len(lista)):
        if i % 2 !=0:
            suma=suma+lista[i]
    return suma
print suma_impares(lista)