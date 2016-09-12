def cons(elemento,l):
    l[0:0]=[elemento]
    return l
def pivot(l):
    if l==[]:
        return False
    else:
        ele=l[0]
        l=l[1:]
        lmen=[]
        lmay=[]
        while l!=[]:
            if l[0]<ele:
                lmen=cons(l[0],lmen)
            else:
                lmay=cons(l[0],lmay)
            l=l[1:]
        return [lmen,lmay]
print pivot([2,1,4,5,6,7,8,5,4,3])