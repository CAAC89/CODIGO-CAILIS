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
    switch=1
    while l!=[]:
        if l[0]==elemento and switch==1:
            l=l[1:]
            switch=0
        else:
            nl=insertar_al_final(l[0],nl)
            l=l[1:]
    return nl
def menor_lista(l):
    if l==[]:
        return False
    else:
        elmenor=l[0]
    while l!=[]:
        if l[0]<=elmenor:
            elmenor=l[0]
        l=l[1:]
    return elmenor
def ordenar_lista_descendentemente(l):
    nl=[]
    while l!=[]:
        nl=cons(menor_lista(l),nl)
        l=eliminar_aparicion_lista(menor_lista(l),l)
    return nl
print ordenar_lista_descendentemente([1,2,7,6,4,8,9,3])