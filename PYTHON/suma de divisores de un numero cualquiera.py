def suma_divisores(n):
    suma=0
    divisor=1
    while n>0:
        if n==0:
            print "ERROR"
        else:
            if (divisor<=n):
                if (n%divisor)!=0:
                    divisor=divisor+1
                else:
                    suma=suma+divisor
                    divisor=divisor+1
    return suma
print suma_divisores(6)