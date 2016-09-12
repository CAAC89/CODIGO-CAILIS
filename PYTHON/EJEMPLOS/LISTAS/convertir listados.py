def cons(elemento,l):
    l[0:0]=[elemento]
    return l
def convertir_listados(ele,l):
    if l==[]:
        return [l]
    else:
        nl=[]
        while l!=[]:
            nl=cons(ele,nl)
            l=l[1:]
        return nl
print convertir_listados([123],[1,2,3,4,5])