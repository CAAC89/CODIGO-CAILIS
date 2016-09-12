def comprobar_lista_numeral(l):
    if l==[]:
        return False
    else:
        while l!=[]:
            if type(l[0])!=int:
                return False
                break
            else:
                l=l[1:]
        if l==[]:
            return True
print comprobar_lista_numeral([1,2,3,4,5,6,7,"hola"])