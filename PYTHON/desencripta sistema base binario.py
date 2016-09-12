def dec_bic(n):
    res=0
    exp=0
    while n>0:
        if (n%10)==1 or (n%10)==0:
            res=res+((n%10)*(10**exp))
            exp=exp+1
        n=n/10
    return res

def contador(n):
    res=0
    db=dec_bic(n)
    while db>0:
        res=res+1
        db=db/10
    return res

def finalizar(n):
    res=0
    exp=contador(n)-1
    db=dec_bic(n)
    while db>0:
        if db!=0:
            res=res+((db%10)*(10**exp))
            exp=exp-1
        db=db/10

    return res
