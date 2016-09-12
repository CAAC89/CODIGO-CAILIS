def suma_digitos(n):
    res=0
    while n>0:
        if (n%10)!=0:
            res=res+(n%10)
        n=n/10
    return res
def suma1(n):
    c=suma_digitos(n)
    res=0
    while c>0:
        if (c%10)!=0:
            res=res+(c%10)
        c=c/10
    return res
def divisible(n):
    suma=suma1(n)
    if (suma%3)!=0:
        return False
    return True
print divisible(suma1(suma_digitos(96395)))