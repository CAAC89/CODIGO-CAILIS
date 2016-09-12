def eliminar_apariciones(digito,numero):
    res=0
    exp=0
    while numero>0:
        if (numero%10)!=digito:
            expp=(numero%10)*(10**exp)
            res=res+expp
            exp=exp+1
        numero=numero/10
    return res
print eliminar_apariciones(3,1235743)
