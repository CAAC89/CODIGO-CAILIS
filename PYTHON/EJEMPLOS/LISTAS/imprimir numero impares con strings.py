def imprimir_impares(lista):
    while lista!=[]:
        if type(lista[0])==int:
            if (lista[0]%2)!=0:
                print lista[0]

        lista=lista[1:]
print imprimir_impares([["hooa"],1,2,["mmm"],3,4,["foggh"]])