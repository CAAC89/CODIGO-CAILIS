def insertar_al_final(elemento,l):
    if l==[]:
        return [elemento]
    else:
        l[-1:]=[l[-1],elemento]
        return l
def repetir(num,ele,l):
    numaux=num
    if l==[]:
        return [ele,ele]
    else:
        nl=[]
        while l!=[]:
            if l[0]==ele:
                while num>0:
                    nl=insertar_al_final(l[0],nl)
                    num=num-1
            else:
                nl=insertar_al_final(l[0],nl)
                num=numaux
            l=l[1:]
        return nl
print repetir(3,"hola",["hola","que","tal","hola"])