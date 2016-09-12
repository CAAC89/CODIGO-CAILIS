def contar_digitos(n):
    cont=0
    while n%10>0:
        cont=cont+1
        n=n/10
    return cont
def invertir(n):
    exp=contar_digitos(n)-1
    res=0
    while n>0:
        var=(n%10)*(10**exp)
        res=res+var
        n=n/10
        exp=exp-1
    return res
print invertir(1234)
