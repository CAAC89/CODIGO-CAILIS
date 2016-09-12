def insertar_al_final(elemento,l):
    if l==[]:
        return [elemento]
    else:
        l[-1:]=[l[-1],elemento]
        return l
def reemplazar_en_lista(remplazo,original,l):
    if l==[]:
        return"ERROR"
    else:
        In=[]
        while l!=[]:
            if l[0]==original:
                In=insertar_al_final(remplazo,In)
            else:
                In=insertar_al_final(l[0],In)
            l=l[1:]
        return In
def excalibur(l1,l2):
    if l1==[]:
        return l2
    elif l2==[]:
        return l2
    else:
        In=l2
        while l2!=[]:
            In=reemplazar_en_lista(l2[0],l1[0],In)
            l1=l1[1:]
            l2=l2[1:]
        return In
print excalibur([1,2,3],[4,5,6])