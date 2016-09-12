def suma_impares(a,b):
    s=0
    while a<=b:
        if a%2!=0:
            s=s+a
        a=a+1
    return s
print suma_impares(2,10)
print suma_impares(11,15)