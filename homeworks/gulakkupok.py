import math

def circle(r):
    circter=r*r*math.pi
    return circter

def square(a,b):
    squarter=a*b
    return squarter

dec=int(input("Minek a térfogatát szeretnéd tudni? 1: gúla, 2: kúp -> "))
if dec==1:
    mag=float(input("Add meg a magasság értékét: "))
    hossz=float(input("Add meg a hossz értékét: "))
    szel=float(input("Add meg a szélesség értékét: "))
    gulterf=(square(hossz,szel)*mag)/3
    print("A megadott gúla térfogata: {0}".format(gulterf))
elif dec==2:
    sug=float(input("Add meg a sugarat: "))
    mag=float(input("Add meg a magasság értékét: "))
    kupterf=(circle(sug)*mag)/3
    print("A megadott kúp térfogata: {0}".format(kupterf))
else:
    print("invalid input")