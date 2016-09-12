from __future__ import division
from math import sin,pi
print"AREA DE TRIANGULO CON GRADOS"
a=float(raw_input("A:    "))
b=float(raw_input("B:    "))
angulo=float(raw_input("ANGULO=     "))
cangulo=(pi/180)*angulo
AREA=1/2*a*b*sin(cangulo)
print "EL AREA ES: ",AREA