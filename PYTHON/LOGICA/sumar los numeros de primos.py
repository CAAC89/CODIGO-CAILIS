#sumar primos
def primo(n):
    divisor=2
    while divisor<n:
        if n%divisor==0:
            return False
        else:
            divisor=divisor+1

    if n<2:
        return False
    else:
        return True

def sumar_primos(x,y):
    suma=0
    while x<=y:
        if primo(x):
            suma=suma+x
        x=x+1
    return suma
print sumar_primos(4,12)