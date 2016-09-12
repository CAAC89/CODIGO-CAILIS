def contar_veces(x,num):
    result=0
    while num>0:
        if num%10==x:
            result=result+1
        num=num/10
    return result
print contar_veces(3,635233348)
