n=356725512199
def paso1(n):
    paso1=(n%1000)
    return paso1
def paso2(n):
    paso2=(n%1000000)/1000
    return paso2
def paso3(n):
    paso3=(n%1000000000)/1000000
    return paso3
def paso4(n):
    paso4=(n%1000000000000)/1000000000
########################################
def suma1(n):
    p1=paso1(n)
    suma=0
    while n>0:
        if (p1%10)!=0:
            suma=suma+(p1%10)
        p1=p1/10
    return suma
def suma2(n):
    p2=suma2(n)
    suma=0
    while n>0:
        if (p2%10)!=0:
            suma=suma+(p2%10)
        p2=p2/10
    return suma
def suma3(n):
    p3=suma3(n)
    suma=0
    while n>0:
        if (p3%10)!=0:
            suma=suma+(p3%10)
        p3=p3/10
    return suma
def suma4(n):
    p4=suma4(n)
    suma=0
    while n>0:
        if (p4%10)!=0:
            suma=suma+(p4%10)
        p4=p4/10
    return suma
#################################################
