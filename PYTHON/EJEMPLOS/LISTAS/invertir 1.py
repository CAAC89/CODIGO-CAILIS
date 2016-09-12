l=["alberto","carmen","benito","daniel"]
def ultimo(l):
    nl=[]
    cont_lista=len(l)-1
    while l!=[]:
        nl.append(l[cont_lista])
        return nl
#print ultimo(l)

def primero(l):
    nl=[]
    cont_lista=len(l)-1-1-1-1
    while l!=[]:
        nl.append(l[cont_lista])
        return nl
#print primero(l)

def segundo(l):
    nl=[]
    cont_lista=len(l)-1-1-1
    while l!=[]:
        nl.append(l[cont_lista])
        return nl
#print segundo(l)

def tercero(l):
    nl=[]
    cont_lista=len(l)-1-1
    while l!=[]:
        nl.append(l[cont_lista])
        return nl
#print tercero(l)

def concatena(l):
    return ultimo(l)+tercero(l)+segundo(l)+primero(l)
print concatena(l)