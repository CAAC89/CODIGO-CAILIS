def plano(l):
    nl=[]
    while l!=[]:
        ele=[l[0][0]]*l[0][1]
        nl.extend(ele)
        del l[0]
    return nl
print plano([[3,2],[1,2],[4,4],[6,1]])
