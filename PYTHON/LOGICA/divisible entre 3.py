#divisible entre tres
def divisible_tres(n):
    result=0
    while n>0:
        if n%10!=0:
            result=result+(n%10)
        n=n/10
    return result
print divisible_tres(96395)

def suma(n):
    result=0
    while n>0:
        if n%10!=0:
            result=result+(n%10)
        n=n/10
    return result
print suma(divisible_tres(96395))

def divisible(n):
    if n%3!=0:
        return False
    else:
        return True
print divisible(suma(divisible_tres(96395)))