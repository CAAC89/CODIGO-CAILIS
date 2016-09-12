def suma_digitos(n):
    res=0
    while n>0:
        if (n%10)!=0:
            res=res+(n%10)
        n=n/10
    return res
print suma_digitos(4523)