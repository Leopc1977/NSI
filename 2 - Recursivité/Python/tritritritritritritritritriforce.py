from turtle import *
import time

def t(c,n,a):
    """
    int s : size
    int n : iteration
    Dessine truc de Pascal
    """
    #time.sleep(0.5)
    if n==0: pass
    else:
        left(a)
        forward(c)

        t(c*3/4,n-1,a-45)
        t(c*3/4,n-1,a-45*3)

        forward(-c)
        left(a)

#LOAD
t(100,3,90)
