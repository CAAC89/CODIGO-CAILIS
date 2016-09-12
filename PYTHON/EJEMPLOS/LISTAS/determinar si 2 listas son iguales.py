l1=[1,3,2,4]
l2=[1,2,4,3]
def son_listas_iguales(l1,l2):
    l1.sort()
    l2.sort()
    if len(l1)!=len(l2):
        return False
    else:
        for i in range(0,len(l1)):
            if (l1[i]!=l2[i]):
                return False
    return True
print son_listas_iguales(l1,l2)