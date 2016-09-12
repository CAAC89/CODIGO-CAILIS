l=[1,2,3,4,5]
def elevado_indice(l):
    nl=[]
    for i in range(0,len(l)):
        nl.append(l[i]**i)
    return nl
print elevado_indice(l)