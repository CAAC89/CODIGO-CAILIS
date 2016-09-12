def insertar_al_final(elemento,l):
    if l==[]:
        return [elemento]
    else:
        l[-1:]=[l[-1],elemento]
        return l
def duplo(ele,l):
    if l==[]:
        return [ele,ele]
    else:
        nl=[]
        while l!=[]:
            if l[0]==ele:
                nl=insertar_al_final(l[0],nl)
                nl=insertar_al_final(l[0],nl)
            else:
                nl=insertar_al_final(l[0],nl)
            l=l[1:]
        return nl
print duplo("hola",["hola","como","esta"])