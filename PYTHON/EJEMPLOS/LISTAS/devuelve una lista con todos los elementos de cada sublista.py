def insertar_al_final(elemento,l):
    if l==[]:
        return [elemento]
    else:
        l[-1:]=[l[-1],elemento]
        return l
def primeros(l):
    if l==[]:
        return []
    else:
        nl=[]
        while l!=[]:
            if l[0]!=[]:
                nl=insertar_al_final(l[0][0],nl)
            l=l[1:]
        return nl
print primeros([[1],[1,2,3],["hola","adios"],[]])