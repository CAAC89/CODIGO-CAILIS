l1=[0,1,2,3]
l2=[3,4,5]
def union(l1,l2):
    c=l1+l2
    c.remove(3)
    return c
print union(l1,l2)

