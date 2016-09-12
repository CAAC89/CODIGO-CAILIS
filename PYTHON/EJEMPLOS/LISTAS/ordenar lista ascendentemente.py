def insertar_al_final(elemento,l):
    if l==[]:
        return [elemento]
    else:
        l[-1:]=[l[-1],elemento]
        return l
def cons(elemento,l):
    l[0:0]=[elemento]
    return l
def eliminar_aparicion_lista(elemento,l):
    nl=[]
    swich=1
    while l!=[]:
        if l[0]==elemento and swich==1:
            l=l[1:]
            swich=0
        else:
            nl=insertar_al_final(l[0],nl)
            l=l[1:]
    return nl
def mayor_lista(l):
    elmayor=0
    while l!=[]:
        if l[0]>elmayor:
            elmayor=l[0]
        else:
            l=l[1:]
    if l==[]:
        return elmayor
def ordenar_lista_ascendentemente(l):
    nl=[]
    while l!=[]:
        nl=cons(mayor_lista(l),nl)
        l=eliminar_aparicion_lista(mayor_lista(l),l)
    return nl
print ordenar_lista_ascendentemente([3,4,6,7,1,2,9,0,5])
