def sumatoria_en_lista(l):
    if l==[]:
        return 0
    else:
        r=0
        while l!=[]:
            r=r+l[0]
            l=l[1:]
        return r
print sumatoria_en_lista([1,2,3,4,5,6])