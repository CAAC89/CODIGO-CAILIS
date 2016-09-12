def comprobar_lista_ascendente(l):
    if l==[]:
        return False
    else:
        elmenor=l[0]
        l=l[1:]
        while l!=[]:
            if l[0]<elmenor:
                return False
                break
            else:
                elmenor=l[0]
                l=l[1:]
        if l==[]:
            return True
print comprobar_lista_ascendente([1,2,3,4])
