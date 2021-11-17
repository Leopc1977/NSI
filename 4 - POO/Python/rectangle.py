class Rectangle():
    def __init__(s,w,h):
        s.color = "Black"
        s.pos = (0,0)
        s.w=w
        s.h=h

    def setPos(s,pos):
        s.pos = pos 
    def setColor(s,color):
        s.color = color
    
    def getSurface(s):
        return s.w*s.h

    def getPerimetre(s):
        return s.w+s.h

    def pprint():
        pass
    
from turtle import *
from math import pi

def drawRec(rec):
    fillcolor(rec.color)
    begin_fill()
    forward(rec.w)
    right(90)
    forward(rec.h)
    right(90)
    forward(rec.w)
    right(90)
    forward(rec.h)
    end_fill()
rec= Rectangle(100,50)
drawRec(rec)

class Cercle():
    def __init__(s,pos,r):
        s.pos = pos
        s.r = r

    def getPerimetre(s):
        return 2*pi*s.r
    def getSurface(s):
        return 2*pi*s.r**2

def drawCercle(c):
    up()
    goto(c.pos)
    down()
    circle(c.r)

c = Cercle((100,100),50)
drawCercle(c)
c = Cercle((50,100),10)
drawCercle(c)