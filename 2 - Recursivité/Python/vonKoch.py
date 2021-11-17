#!/usr/bin/env python3

import turtle
 
def courbe_koch(longueur,limit):
    """Fonction récursive pour dessiner une courbe de Von Koch
    (une fonction récursive étant une fonction s'appelant elle-même"""
    if longueur < limit:
        turtle.forward(longueur)
    else:
        courbe_koch(longueur/3,limit)
        turtle.left(90)
        courbe_koch(longueur/3,limit)
        turtle.right(90)
        courbe_koch(longueur/3,limit)
        turtle.right(90)
        courbe_koch(longueur/3,limit)
        turtle.left(90)
        courbe_koch(longueur/3,limit)
 
def flocon_koch(longueur, etape):
    """Fonction pour dessiner un flocon de Von Koch
    depuis le coin haut gauche"""
    for i in range(4):  #Pour chaque côté du triangle initial
        courbe_koch(longueur, etape)  #Courbe de Von Koch
        turtle.right(90)
    
    
if __name__ == "__main__":
    turtle.speed("fastest")
    turtle.hideturtle()
    flocon_koch(200,5)
