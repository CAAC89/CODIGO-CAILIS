def desencriptar_base_ocho(n):
    nnum=0
    exp=0
    while n>0:
        if (n%10)==8:
            nnum+=222*(10**exp)
            exp+=3
        elif (n%10)==9:
            nnum+=33*(10**exp)
            exp+=2
        else:
            nnum+=(n%10)*(10**exp)
            exp+=1
        n=n/10
    return nnum
print desencriptar_base_ocho(289)