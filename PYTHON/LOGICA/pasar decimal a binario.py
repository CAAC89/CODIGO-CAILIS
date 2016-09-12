def dec_bic(n):
    res=0
    exponente=0
    while n > 0:
        if (n%10) == 0 or (n%10) == 1:
            res+=(n%2)*(2**exponente)
            exponente+=1
        n=n/10
    return res
print dec_bic(1110)
