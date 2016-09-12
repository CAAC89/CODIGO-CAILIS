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
print elimina_primera_aparicion(2,12345)
###################################################################
def contar_digitos(n):
    contador=0
    while n>0:
        contador = contador+1
        n=n/10
    return contador
def invertir(n):
    exponente = contar_digitos(n)-1 # Por la posicion
    resultado=0
    while n > 0:
        elemento = (n%10) * (10**exponente)
        resultado= resultado + elemento
        n=n/10
        exponente = exponente-1
    return resultado
def eliminar_aparicion_por_izquierda(d,n):
    n=invertir(n)
    resultado=invertir(eliminar_por_derecha(d,n))
    return resultado
print elimina_primera_aparicion(3,123445)
#####################################################################
def digito_mayor(n):
    elmayor=n%10
    while n > 0:
        if n%10 > elmayor:
            elmayor=n%10
        n=n/10
    return elmayor
def digito_menor(n):
    elmenor=n%10
    while n > 0:
        if n%10 < elmenor:
            elmenor=n%10
        n=n/10
    return elmenor
def ordenar_ascendente(n):
    resultado=0
    exponente=0
    while n > 0:
        elemento = digito_mayor(n)*(10**exponente)
        resultado=resultado + elemento
        n = elimina_primera_aparicion(digito_mayor(n),n)
        exponente=exponente+1
    return resultado
print ordenar_ascendente(354127)
def ordenar_descendente(n):
    resultado=0
    exponente=0
    while n > 0:
        elemento = digito_menor(n)*(10**exponente)
        resultado=resultado + elemento
        n = elimina_primera_aparicion(digito_menor(n),n)
        exponente=exponente+1
    return resultado
print ordenar_descendente(354127)
