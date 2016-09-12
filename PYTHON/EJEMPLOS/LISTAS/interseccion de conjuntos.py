l1=[0,1,2,3]
l2=[3,4,5]
def interseccion_de_conjuntos(l1,l2):
    nl=[]
    while l1!=[]:
        while l1[0]==l2[0]:
            nl.append(l1[0])
            l2=l2[1:]
        else:
            l1=l1[1:]
    return nl
print interseccion_de_conjuntos(l1,l2)