a=[1,3,2]
b=[1,8,2,4]
def esta_incluida(a,b):
    a.sort()
    b.sort()
    for i in range(0,len(a)):
        if (a[i]!=b[i]):
            return False
    else:
        return True
print esta_incluida(a,b)
