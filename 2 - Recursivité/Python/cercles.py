from turtle import *

title("Fractal Von Koch")  #Change le titre
color('red')
down()

def toHex(r,g,b):
    r=hex(r)[2:]
    g=hex(g)[2:]
    b=hex(b)[2:]
    if len(r)==1: r='0'+r
    if len(g)==1: r='0'+g
    if len(b)==1: r='0'+b
    rgb='#'+r+g+b
    print(rgb)
    return rgb

colorrgb=255
def c(r):
    global colorrgb
    d=r*2
    
    if r>5:
        forward(-d)
        c(r-1)
    #fillcolor(toHex(colorrgb,colorrgb,colorrgb))
    begin_fill()
    circle(r)
    end_fill()
    
    forward(d)
    colorrgb-=10
    
c(30)

