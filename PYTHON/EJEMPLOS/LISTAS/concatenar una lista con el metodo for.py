#concatenar
a=[1,2,3,4]
b=[5,6,7,8]
def concatenar(a,b):
    nl=[]

    for i in range(0,len(a)):
        nl.append(a[i])

    for i in range(0,len(b)):
        nl.append(b[i])
    return nl
print concatenar(a,b)