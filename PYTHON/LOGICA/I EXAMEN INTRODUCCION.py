# Primera de Desarrollo (1 Funcion)
def desarrollo1(ini,fin):
    res=0
    while ini <= fin:
        if ini%2 != 0:
            res+= ini
        ini+=1
    return res

#print desarrollo1(11,15)

# Segunda de desarrollo (1 Funcion)
def desarrollo2(n):
    res=0
    exponente=0
    while n>0:
        if n%10 == 8:
            res+=222*(10**exponente)
            exponente+=3 # tenia que sumarle al exponente 3, por que son tres dos 222
        elif n%10 == 9:
            res+=33*(10**exponente)
            exponente+=2 # tenia que sumalre al exponente 2, porque son dos tres 33
        else:
            res+=(n%10)*(10**exponente)
            exponente+=1 # Si no es ni 8 ni nueve se arma normalmente
        n=n/10 # Como siempre debemos dividir, se pone afuera
    return res

#print desarrollo2(99)

# Tercera de desarrollo (2 Funciones)
def eliminar_apariciones(d,cifra):
    resultado=0
    exponente=0
    while cifra > 0:
        if (cifra%10) != d:
            elemento = (cifra%10) * (10**exponente)
            resultado = resultado + elemento
            exponente = exponente +1
        cifra = cifra / 10
    return resultado

def desarrollo3(n):
    exponente=0
    res=0
    while n > 0:
        res=res+(n%10)*(10**exponente)
        n=eliminar_apariciones((n%10),n)
        exponente=exponente+1
    return res

#print desarrollo3(255121)
#print desarrollo3(323442)
#print desarrollo3(2211)

# Cuarta de Desarrollo (2 Funciones)

def bin_dec(n):
    res=0
    exponente=0
    while n > 0:
        if n%10 == 1:
            res=res+(n%10)*(2**exponente)
        n=n/10
        exponente+=1
    return res

#print bin_dec(101)
#print bin_dec(1101110) # Esta en realidad da 110, no 189 como aparece en el examen
#print bin_dec(101111)

def desarrollo4(n):
    res=0
    exponente=0
    while n > 0:
        if (n%10) == 0 or (n%10) == 1:
            res+=(n%10)*(10**exponente)
            exponente+=1
        n=n/10
    res=bin_dec(res)
    return res

#print desarrollo4(22310411911)
#print desarrollo4(181809191310) # Esta da 110, no 189
#print desarrollo4(81091)
