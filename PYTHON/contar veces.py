def contar_veces(d,c):
    suma=0
    while c>0:
        if (c%10)==d:
            suma=suma+1
        c=c/10
    return suma
print contar_veces(3,635248)