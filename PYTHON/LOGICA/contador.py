def contador(n):
    cont=0
    while n>0:
        cont=cont+1
        n=n/10
    return cont
print contador(012350)
