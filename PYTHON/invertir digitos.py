def contar_digitos(n):
    res=0
    while n>0:
        res=res+1
        n=n/10
    return res
print contar_digitos(76453)
def invertir(n):
    exp=contar_digitos(n)-1
    res=0
    while n>0:
        c=((n%10)*(10**exp))
        res=res+c
        n=n/10
        exp=exp-1
    return res
print invertir(76453)