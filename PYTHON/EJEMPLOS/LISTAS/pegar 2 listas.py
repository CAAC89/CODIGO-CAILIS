def insertar_al_final(elemento,l):
    if l==[]:
        return [elemento]
    else:
        l[-1:]=[l[-1],elemento]
        return l
def pegar(l1,l2):
    while l2!=[]:
        l1=insertar_al_final(l2[0],l1)
        l2=l2[1:]
    return l1
print pegar ([0,1,2,3,4,5],[6,7,8,9,10])