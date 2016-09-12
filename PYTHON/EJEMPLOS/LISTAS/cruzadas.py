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
def cruzadas(l1,ele,l2):
    if l1==[]:
        return l2
    elif l2==[]:
        return []
    else:
        In=l2
        l2aux=l2
        while l1!=[]:
            while l2!=[]:
                if l1[0]==l2[0]:
                    In=reemplazar_en_lista(ele,l1[0],In)
                l2=l2[1:]
            l2=In
            l1=l1[1:]
        return In
print cruzadas([1,2,3],"ola",[1,2,3])
