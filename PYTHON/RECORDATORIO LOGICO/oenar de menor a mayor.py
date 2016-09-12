def elimina_primera_aparicion(d,cifra):
    exp=0
    res=0
    swith=1
    while cifra>0:
        if cifra%10==d and swith==1:
            cifra=cifra/10
            swith=0
        else:
            elemento=(cifra%10)*(10**exp)
            res=res+elemento
            exp=exp+1
            cifra=cifra/10
    return res
def digito_mayor(n):
    elmayor=n%10
    while n > 0:
        if n%10 > elmayor:
            elmayor=n%10
        n=n/10
    return elmayor
def ordenar_ascendente(n):
    resultado=0
    exponente=0
    while n > 0:
        elemento = digito_mayor(n)*(10**exponente)
        resultado=resultado + elemento
        n = elimina_primera_aparicion(digito_mayor(n),n)
        exponente=exponente+1
    return resultado
def ultimo_paso(n):
    if n==ordenar_ascendente(n):
        return True
    else:
        return False
print ultimo_paso(234516)
print ultimo_paso(24567)