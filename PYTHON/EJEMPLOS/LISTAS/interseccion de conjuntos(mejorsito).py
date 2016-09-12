a=[1,3,2,5]
b=[2,4,6,8,5]
def interseccion(a,b):
    a.sort()
    b.sort()
    nl=[]
    for i in a:
        for y in b:
            if i==y:
                if i not in nl:
                    nl.append(i)
    return nl
print interseccion(a,b)
