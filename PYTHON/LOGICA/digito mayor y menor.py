def digito_menor(n):
    el_menor=n%10
    while n>0:
        if n%10<el_menor:
            el_menor=n%10
        n=n/10
    return el_menor
print digito_menor(322144)

def digito_mayor(n):
    el_mayor=n%10
    while n>0:
        if n%10>el_mayor:
            el_mayor=n%10
        n=n/10
    return el_mayor
print digito_mayor(6423457)