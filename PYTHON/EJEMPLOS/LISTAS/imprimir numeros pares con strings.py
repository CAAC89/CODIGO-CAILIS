def imprime_numpares_con_strings(lista):
    for texto in lista:
        if type(texto)==int:
            if texto%2==0:
                print texto
print imprime_numpares_con_strings([1,2,["mmmm"],3,4,["saludos"],5,6,["hola"]])
