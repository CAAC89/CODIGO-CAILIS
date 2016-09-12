def insertar_al_final(elemento,l):
    if l==[]:
        return [elemento]
    else:
        l[-1:]=[l[-1],elemento]
        return l
def listar_string(s):
    if s=="":
        return []
    else:
        s=s+""
        switch=0
        nl=[]
        ns=""
        while s!="":
            if switch==1:
                s=s[1:]
                nl=insertar_al_final(ns,nl)
                ns=""
                switch=0
            else:
                if s[0]=="":
                    switch=1
                else:
                    ns=ns+s[0]
                    s=s[1:]
        return nl
print listar_string("BIENVENIDOS AL TEC")