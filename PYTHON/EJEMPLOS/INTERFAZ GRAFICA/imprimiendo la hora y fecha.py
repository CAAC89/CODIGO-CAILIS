import time

def imprimir_fecha():
    return str(time.localtime()[2]) + "/" + str(time.localtime()[1]) + "/" + str(time.localtime()[0]) + ", " + str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5])

print imprimir_fecha()

