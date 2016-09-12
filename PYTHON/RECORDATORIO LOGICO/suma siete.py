#suma siete a cada digito
n=1221
def suma_siete(n):
    exp=0
    siete=7
    nnum=0
    while n>0:
        nnum=nnum+((n%10)+7)*(10**exp)
        exp=exp+1
        n=n/10
    return nnum
print suma_siete(n)