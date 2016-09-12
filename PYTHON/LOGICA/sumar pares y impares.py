def sumar_impares(ini,fin):
    res=0
    while ini<=fin:
        if ini%2!=0:
            res=res+ini
        ini=ini+1
    return res
print sumar_impares(11,15)

def sumar_pares(ini,fin):
    res=0
    while ini<=fin:
        if ini%2!=1:
            res=res+ini
        ini=ini+1
    return res
print sumar_pares(11,15)