def miembro(ele,l):
    while l!=[]:
        if ele==l[0]:
            return True
            break
        else:
            l=l[1:]
    if l==[]:
        return False
def insertar_al_final(elemento,l):
    if l==[]:
        return [elemento]
    else:
        l[-1:]=[l[-1],elemento]
        return l
def extraer_por_posicion(p,l):
    ind=0
    while l!=[]:
        if p==ind+1:
            return l[0]
            break
        else:
            l=l[1:]
            ind=ind+1
    if l==[]:
        return"NO EXISTE EL ELEMENTO EN LA LISTA"
def listar_string(s):
    if s=="":
        return []
    else:
        s=s+""
        swith=0
        nl=[]
        ns=""
        while s!="":
            if swith==1:
                s=s[1:]
                nl=insertar_al_final(ns,nl)
                ns=""
                swith=0
            else:
                if s[0]==" ":
                    swith=1
                else:
                    ns=ns+s[0]
                    s=s[1:]
            return nl
def limpiar_palabra(l,s):
    if s=="":
        return s
    elif l==[]:
        return s
    else:
        np=""
        saux=s
        while s!="":
            if not miembro(s[0],l):
                np=np+s[0]
            s=s[1:]
        return np
def obtener_palabra_por_posicion(p,s):
    s=listar_string(s)
    return limpiar_palabra([",",".",":",";","-","_"],extraer_por_posicion(p,s))
print obtener_palabra_por_posicion(4,"hola como va todo,")