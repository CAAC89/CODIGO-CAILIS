n=635248
d=3
def numero_veces(n,d):
    cont=0
    while n>0:
        if (n%10)==d:
            cont=cont+1
        n=n/10
    return cont
print numero_veces(n,d)