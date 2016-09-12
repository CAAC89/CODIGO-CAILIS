l=[1,2,3,4]
def invertir(l):
    c=len(l)-1
    nl=[]
    while l!=[]:
        if l[c]>l[c-1]:
            nl.append(l[c])
            c=c-1
        elif l[c]<l[c-1]:
            nl.append(l[c-1])
            c=c-1
        else:
            c=c-1



print invertir(l)