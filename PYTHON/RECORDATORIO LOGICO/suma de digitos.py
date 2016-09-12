n=4523
def suma_digitos(n):
    result=0
    while n>0:
        if n%10!=0:
            result=result+(n%10)
        n=n/10
    return result
print suma_digitos(n)