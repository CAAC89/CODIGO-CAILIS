def primo(n):
    divisor=2
    while n>divisor:
        if n%divisor==0:
            return False
        divisor=divisor + 1
    return True
def validar(n):
    c=primo(n)
    while n!=c:
        return False
    return True
print validar(primo(4))
print validar(primo(3))