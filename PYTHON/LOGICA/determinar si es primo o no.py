#determinar si es primo o no
def primo(n):
    divisor=2
    while divisor<n:
        if n%divisor==0:
            return False
        else:
            divisor=divisor+1
    if n<2:
        return False
    else:
        return True
print primo(int(raw_input("DIGITE EL NUMERO:       ")))