n=8
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print factorial(n)
def fibonacci (n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print fibonacci(n)