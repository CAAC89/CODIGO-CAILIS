listica=[1,2,3,4,5]
def promedio(listica):
    suma=0.0
    for i in range(0,len(listica)):
        suma=suma+listica[i]
    return suma/len(listica)
print promedio(listica)