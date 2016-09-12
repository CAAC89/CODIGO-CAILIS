def comprobar_lista_alternado(l):
    if l==[]:
        return True
    else:
        anterior=l[0]
        l=l[1:]
        while l!=[]:
            if l[0]==anterior:
                return False
                break
            else:
                anterior=l[0]
                l=l[1:]
        if l==[]:
            return True
print comprobar_lista_alternado([1,0,1,0])
print comprobar_lista_alternado([1,1,1,0,1,0,1])
