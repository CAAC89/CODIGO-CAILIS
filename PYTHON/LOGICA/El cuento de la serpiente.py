# -*- coding: iso-8859-15 -*-

print "El cuento de las Serpientes"
print "TEC SSC, Jueves 03 de Febrero, A?o 2011"

t1="?Qu? quieres hacer?"
t2="-----------------------------"

estado=0
cuadros=[2]
ini=[0]
respuesta=[0]
parada=""
nombre=[""]

def conclusion():
    if estado==0:
        print "|||| Este juego a?n no ha sido terminado y est? en fase beta ||||"
    elif estado ==1:
        print "|||| Juego Finalizado. Gracias por jugar ||||"


def g1():
    while ini[0] < 1:
        print t2
        print t1
        print "1. Jugar F?tbol Sala"
        print "2. Hackear empresas"
        print "3. Dormir"
        print "4. Escuchar m?sica"
        print "5. Tengo hambre"
        elegiste=raw_input(">>")
        if elegiste == "1":
            ini[0]+=1
            respuesta[0]=1
        elif elegiste == "2":
            ini[0]+=1
            respuesta[0]=2
        elif elegiste == "3":
            ini[0]+=1
            respuesta[0]=3
        elif elegiste == "4":
            ini[0]+=1
            respuesta[0]=4
        elif elegiste == "5":
            ini[0]+=1
            respuesta[0]=5
    return g2()

def g2():
    print """
Tienes frente a t? una puerta. Al otro lado de la puerta se escucha un grupo de gente gritando

La puerta est? cerrada."""
    parada=raw_input("")
    if respuesta[0]==1:
        raw_input("Tus amigos te esperan en la cancha")
    elif respuesta[0]==2:
        raw_input("Necesitas visitar a un amigo hacker")
    elif respuesta[0]==3:
        raw_input("No puedes dormir con tanto ruido")
    elif respuesta[0]==4:
        raw_input("La m?sica puede esperar. ?Qu? rayos sucede afuera?")
    elif respuesta[0]==5:
        raw_input("Hay un restaurante cerca donde acostumbras ir a comer")
    while ini[0]<2:
        print t2
        print t1
        print "1. Abrir la puerta"
        print "2. Hay un libro sobre la mesa al lado de la puerta. Quiero leer lo que dice la portada"
        print "3. Te da miedo salir"
        print "4. Hay un cuadro en la pared mirarlo"
        print "5. Hay un reloj despertador sobre la mesa donde est? el libro. ?De qu? marca es?"
        elegiste=raw_input(">>")
        if elegiste == "1":
            ini[0]+=1
        elif elegiste == "2":
            raw_input("La portada pone 'Mundodisco'")
        elif elegiste == "3":
            raw_input("...Pero por otro lado, quieres saber qu? hay afuera...")
        elif elegiste == "4":
            raw_input("Hay una enorme serpiente en el cuadro")
        elif elegiste == "5":
            raw_input("El reloj es marca patito")
    return g3()

def g3():
    print """
Al abrir la puerta te encuentras con una multitud que ocupa toda la plaza. La gente se empuja, un ni?o llora,
unas personas se ven enojadas. Otras gritan cosas que no logras comprender del todo. Tienes que abrirte paso entre la gente."""
    parada=raw_input("")
    if respuesta[0]==1: raw_input("La cancha queda al otro lado de la multitud, el partido empieza en 10 minutos...")
    elif respuesta[0]==2: raw_input("La casa de tu amigo hacker est? cerca de un valle, pero la gente no te deja pasar")
    elif respuesta[0]==3: raw_input("No comprendes del todo qu? sucede, pero no podr?s dormir con toda esa gente haciendo ruido.")
    elif respuesta[0]==4: raw_input("No tengo tiempo para escuchar m?sica, necesito saber qu? sucede aqu?!")
    elif respuesta[0]==5: raw_input("El restaurante est? abierto pero hay mucha gente bloqueando el paso")
    while ini[0]<3:
        print t2
        print t1
        print "1. Una persona choca contigo. ?Voltear?s para saber quien es?"
        print "2. Comenzar a empujar a todo el mundo para abrirte paso"
        print "3. Te da mucho miedo como para moverte. Mamaaaa..."
        print "4. Escuchas ladridos. ?No ser? que tu perro se sali? de la casa?"
        print "5. Tienes mucha curiosidad y comienzas a caminar educadamente entre la enfurecida multitud"
        elegiste=raw_input(">>")
        if elegiste == "1":
            raw_input("La persona se pierde entre la multitud y no puedes ver su rostro")
        elif elegiste == "2":
            ini[0]+=1
        elif elegiste == "3":
            raw_input("...Pero no te vas a quedar ah? todo el d?a...")
        elif elegiste == "4":
            raw_input("Ahora que recuerdo mi mascota es un drag?n, y los dragones no ladran")
        elif elegiste == "5":
            ini[0]+=1
    return g4()

def g4():
    print """
--------------------------------------------------------
CAP?TULO 1: El Misterio

?rase una vez un reino, en el siglo 21. Un reino que poca gente conoc?a, pero aunque, este reino exist?a,
no en la era de los dragones y doncellas, si no entre computadores y multinacionales, la gente todav?a disfrutaba
del viento y el cantar de los ?rboles, que se mec?an en un bosque tan misterioso como jamas se crey? hubiera uno.

Este reino tenia un rey, que de alguna manera, era conocido por cada persona del lugar, que no era una aldea, sino
una ciudad con una tecnologia como cualquier otra ciudad con tecnologia.

Hace algunas semanas el rey habia enfermado, y un dia , que lleg? justo cuando nadie lo esperaba, la tragedia se
apoder? de este reino, y aunque los doctores lo intentaron, nada pudo salvar al rey...

Las personas no sab?an nada hasta que sali? el sol, y la noticia corri? por cada rinc?n, pero iba acompa?ada
de un oscuro rumor, donde se especulaba que el cuerpo del rey hab?a desaparecido del hospital.

Pronto la gente comenz? a llegar a la plaza donde se encontraba el hospital. Era una plaza grande donde
viv?an gran parte de las personas que trabajaban en el hospital. La gente gritaba y exig?a saber lo que
hab?a sucedido con el cuerpo de el rey.

Un joven se hacia espacio entre la multitud...

La gente murmuraba cosas...

"""

    raw_input("Ciudadano: Yo escuch? que el cuerpo del rey sufri? una maldici?n terr...")
    raw_input("Otro ciudadano: Yo no creo que a estas alturas alguien sea tan cr?dulo")

    print """

(La gente de esta era ya no es tan cr?dula, mucho menos creer en maldiciones ni leyendas)

    """

    raw_input("Ciudadano: Posiblemente haya sido malpraxis y lo quieren encubrir. ")
    raw_input("Ciudadano: ?D?nde est? la reina?")
    print """
(La gente te empuja sin misericordia pero logras salir de la multitud)

El joven que se encontraba tratando de salir de la multitud, por fin lo logra, pero es detenido por un
guarda al intentar cruzar un callej?n.

"""

    print "Guarda: ?C?mo te llamas? (El guarda te pregunta el nombre)"
    while nombre[0] == "":
        nombre[0]=raw_input("[ESCRIBE TU NOMBRE]: ")
    print nombre[0]+" : ","Soy ",nombre[0]
    raw_input("Guarda: El rey ha muerto y se sospecha que fue asesinado, todo ciudadano es sospechoso")
    raw_input(nombre[0]+" :"+"?Qu?? El rey...")
    raw_input("Guarda: ?Qu? haces en este callej?n? ?Hacia donde te diriges?")
    if respuesta[0] == 1:
        raw_input(nombre[0]+" :"+"Al sal?n a jugar futbol sala")
    elif respuesta[0] == 2:
        raw_input(nombre[0]+" :"+"A casa de un amigo (Tu amigo el hacker)")
    elif respuesta[0] == 3:
        raw_input(nombre[0]+" :"+"Err... solo pasaba por aqu?, no sab?a lo del Rey")
    elif respuesta[0] == 4:
        raw_input(nombre[0]+" :"+"Umm... soy un ciudadano y puedo ir por donde quiera...")
    elif respuesta[0] == 5:
        raw_input(nombre[0]+" :"+"Al restaurante que est? cruzando el callej?n")
    raw_input("(Se escucha un ruido y una sombra distrae al guarda por un momento)")
    raw_input("Guarda: Qu?date aqu?, en un momento vuelvo")
    raw_input(nombre[0]+" :"+"Ok... (Me largo en cuanto lo pierda de vista)")
    raw_input("(Se escucha un grito)")
    raw_input(nombre[0]+" :"+"?????")
    raw_input("Guarda: Argghhh!!")
    raw_input(nombre[0]+" :"+"Q...?????")
    raw_input("""Te percatas de que est?s solo, el guarda acaba de ser atacado. En el suelo hay varias cosas;
un hacha vieja con un trozo del mango destrozado, un trozo de papel con algo escrito, un l?piz labial, un sombrero y un
pase especial al parque de diversiones.""")

    while ini[0]<4:
        print t2
        print t1
        print "1. Coger el pase especial al parque de diversiones"
        print "2. Coger el l?piz labial"
        print "3. Recoger el trozo de papel, la curiosidad es demasiada...."
        print "4. Recoger el hacha con el mango destrozado"
        print "5. Recoger el sombrero y pon?rtelo"
        elegiste=raw_input(">>")
        if elegiste == "1":
            raw_input("Oh, ya caduc? el pase.. Lo vuelves a tirar...")
        elif elegiste == "2":
            raw_input("Mejor no, ?Para qu? quieres un l?piz labial?")
        elif elegiste == "3":
            raw_input("El papel dice: 'Por favor ayudenme, estoy encerrado en el apartamento 201014364'")
        elif elegiste == "4":
            raw_input(nombre[0]+" :"+"Con esto bastar? si se quieren meter conmigo!")
            ini[0]+=1
        elif elegiste == "5":
            raw_input("El sombrero est? clavado al suelo y no lo puede coger para pon?rtelo...")
    return g5()

def g5():
    raw_input("Se escuchan pasos cerca de ti...")
    raw_input("......")
    raw_input(nombre[0]+" :"+"??Qui?n eres..!?")
    raw_input("Figura entre las sombras: Te conozco (Su voz era susurrante, casi inaudible)")
    raw_input("Figura entre las sombras: Ese guarda es una persona muy desafortunada")
    raw_input(nombre[0]+" :"+"??Qu? haz hecho con el guarda que estaba hace un momento aqu?!?")
    raw_input("""Figura entre las sombras: Digamos que no es su d?a de suerte. No creo que hayas sido t?
quien haya atacado el rey. No menciones a nadie sobre m? o sobre el guarda. Te conceder?
una ?nica pregunta antes de irme""")

    while ini[0]<5:
        print "1. ?C?mo te llamas?"
        print "2. ?Qu? sabes t? de la muerte del rey?"
        print "3. ?Qui?n eres y qu? tramas en este reino?"
        print "4. ?Porqu? te ocultas entre las sombras?"
        print "5. No tengo ninguna pregunta"
        elegiste=raw_input(">>")
        if elegiste == "1":
            raw_input("Figura entre las sombras: Ll?mame Shadow")
            ini[0]+=1
        elif elegiste == "2":
            raw_input("Figura entre las sombras: Busco al hombre que asesin? al rey, es todo lo que te puedo decir")
            ini[0]+=1
        elif elegiste == "3":
            raw_input("Figura entre las sombras: Soy Shadow, y busco al hombre que asesin? al rey")
            ini[0]+=1
        elif elegiste == "4":
            raw_input("Figura entre las sombras: Para saber la verdad necesito ocultarme y observar. Nos vemos")
            ini[0]+=1
        elif elegiste == "5":
            raw_input("Figura entre las sombras: Bien. Adi?s...")
            ini[0]+=1
    return g6()

def g6(): print "hola"


g1()
conclusion()




