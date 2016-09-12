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
print reemplazar_en_lista("ma?ana","tarde",["te llamo en la","tarde"])
