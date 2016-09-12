print"CONVERSION A EUROS"
E=float(raw_input("EUROS:  "))
I=float(raw_input("INTERESES:   "))
A=int(raw_input("ANOS:   "))
res=E*(1+(I/100))**A
print "SU RESULTADO ES :",res