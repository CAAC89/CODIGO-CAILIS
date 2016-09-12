a=[1,2,3,4,5]
b=[6,7,8,9,10,1]
def union_de_conjuntos(a,b):
    a.sort()
    b.sort()
    nl=[]
    for i in a:
        if i not in nl:
            nl.append(i)
    for y in b:
        if y not in nl:
            nl.append(y)
    return nl
print union_de_conjuntos(a,b)