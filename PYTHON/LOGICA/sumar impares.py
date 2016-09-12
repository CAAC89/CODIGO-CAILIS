def sumar_impares(x,y):
    contador=0
    while x<=y:
        if(x%2==1):
            contador=contador+x
    x=x+1
    return(contador)
print sumar_impares(3,3)
