def reloj(segundos):
    minutos=0
    horas=0
    while segundos>=60:
        if segundos>=3600:
            horas=horas+1
            segundos=segundos-3600
        elif (segundos<3600) and segundos>=60:
            minutos=minutos+1
            segundos=segundos-60
    t1="  HORAS CON  "
    t2="  MINUTOS Y  "
    t3="  SEGUNDOS   "
    return str(horas)+t1+str(minutos)+t2+str(segundos)+t3
print reloj(3600)