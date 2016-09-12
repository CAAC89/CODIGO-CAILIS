def existe_digito(d,n):
    while n>0:
        if (n%10)!=d:
            return False
        return True
    n=n/10
print existe_digito(3,123)