
# -*- coding: utf-8 -*-
from Tkinter import *

a=Tk()
a.resizable(0,0)
a.geometry("550x400")
a.title("BINARIUM")
b=StringVar()
b.set("""
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010

""")
c="""
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
1001010101010010010101010010110010101010100100101010100101
0100101010101001001010101001001001010101010010010101010010
"""

def ds(h):
    f,g=0,len(h)
    while f < g:
        if h[f] != " ":
            return False
            break
        f+=1
    return True

def s(h):
    taud=h
    if not ds(h):
        h = " " + h[0:-1]
        return h
    else: return c

def j(t): print t

def i():
    a.after(1,i)
    b.set(s(b.get()))

label1=Label(a,textvar=b,font=(16)).pack(side=TOP)
i()
a.mainloop()