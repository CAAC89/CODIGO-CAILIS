def suma_siete(n):
    exp=0
    nnum=0
    siete=7
    while n>0:
        nnum=nnum+((n%10)+siete)*(10**exp)
        exp=exp+1
        n=n/10
    return nnum
print suma_siete(1221)