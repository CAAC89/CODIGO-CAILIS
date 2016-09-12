def eliminar_apariciones(d,n):
    nnum=0
    exp=0
    while n>0:
        if (n%10)!=d:
            ele=(n%10)*(10**exp)
            nnum=nnum+ele
            exp=exp+1
        n=n/10
    return nnum
def desencriptar(n):
    res=0
    exp=0
    while n>0:
        res=res+((n%10)*(10**exp))
        n=eliminar_apariciones((n%10),n)
        exp=exp+1
    return res
print desencriptar(2211)