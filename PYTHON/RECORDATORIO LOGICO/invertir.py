n=76453
def contador(n):
    s=0
    while n>0:
        s=s+1
        n=n/10
    return s
def invertir(n):
    nnum=0
    exp=contador(n)-1
    while n>0:
        nnum=nnum+((n%10)*(10**exp))
        n=n/10
        exp=exp-1
    return nnum
print invertir(n)