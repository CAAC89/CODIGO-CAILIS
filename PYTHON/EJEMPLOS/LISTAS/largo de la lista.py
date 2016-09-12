def largo_lista(lista):
    c=0
    while lista!=[]:
        c=c+1
        lista=lista[1:]
    if lista==[]:
        return c
print largo_lista([0,1,2,3,4,5])