# -*- coding: utf-8 -*-
from Tkinter import *

v0=Tk()
v0.resizable(0,0)
v0.title("ACELERADOR")
speed=StringVar()
label1=Label(v0,textvar=speed,font=(20)).grid()
b1=Button(v0,text="TERMINAR KILOMETRAJE",command=v0.destroy,font=(16)).grid()

gas=[180]
limite=[1]
velocidad=[1]
switch=[1]

def acelerador():
    v0.after(gas[0],acelerador)
    if gas[0] > limite[0] and switch[0]==1:
        gas[0]-=1
        print "Vamos a",velocidad[0],"Km/h"
        speed.set("Vamos a " + str(velocidad[0]) + " Km/h")
        velocidad[0]+=1
    else:
        switch[0] = 0
        limite[0]= 180
    if gas[0] < limite[0] and switch[0]==0:
        gas[0]+=1
        print "Vamos a",velocidad[0],"Km/h"
        speed.set("Vamos a " + str(velocidad[0]) + " Km/h")
        velocidad[0]-=1
    else:
        if switch[0]==0:
            switch[0]=1
            gas[0]=180
            velocidad[0]=1
            limite[0]= 1

acelerador()
v0.mainloop()
