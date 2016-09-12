def cons(elemento,l):
    l[0:0]=[elemento]
    return l
def converse(elemento,cantidad):
    if cantidad==0:
        return []
    else:
        nl=[]
        while cantidad>0:
            nl=cons(elemento,nl)
            cantidad=cantidad-1
        return nl
print converse("ca",12)
