def contar_digitos(n):
    suma=0
    while n>0:
        suma=suma+1
        n=n/10
    return suma
def suma_siete(n):
    siete=7
    exp=contar_digitos(n)-1
    res=0
    while n>0:
        c=((n%10)+(siete))
        res=res+((c)*(10**exp))
        n=n/10
        exp=exp-1
    return res
print suma_siete(1221)