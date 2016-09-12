lista=[["Ana",20],["Luis",30],["Carlos",10],["Rosa",8]]
def ordenar(x,lista):
    i=0
    while i<len(lista):
        if x[1]>lista[i][1]:
            i=i+1
        elif x[1]==lista[i][1]:
            lista.insert(i,x)
            return lista
        else:
            lista.insert(i,x)
            return lista
    lista.append(x)
    return lista
def principal(lista):
    nl=[]
    while lista!=[]:
        nl=ordenar(lista[0],nl)
        del (lista[0])
    return nl
print principal(lista)