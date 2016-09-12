lista=[1,2,3,4,5]
def numeros_impares(lista):
    nl=[]
    for c in lista:
        if type(c)==int:
            if c%2==1:
                nl.append(c)
    return nl
print numeros_impares(lista)

def numeros_pares(lista):
    nl=[]
    for c in lista:
        if type(c)==int:
            if c%2==0:
                nl.append(c)
    return nl
print numeros_pares(lista)