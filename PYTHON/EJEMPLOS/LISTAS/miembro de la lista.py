def miembro(elemento,lista):
    while lista!=[]:
        if elemento==lista[0]:
            return True
            break
        else:
            lista=lista[1:]
    if lista==[]:
        return False
print miembro(1,[1,2,3,4,5])
print miembro(0,[1,2,3,4,5])
