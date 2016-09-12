from math import sqrt
print"Area y perimetro de triangulo con semiperimetro"
a=float(raw_input("A:  "))
b=float(raw_input("B:  "))
c=float(raw_input("C:  "))
P=a+b+c
semi=(P)/2
Area=sqrt((semi)*(semi-a)*(semi-b)*(semi-c))
print"EL PERIMETRO ES: ",P
print"EL AREA ES: ",Area