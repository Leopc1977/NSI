#NOEL

import pygame as pg
import sys

pg.init()

bg = pg.image.load("Avent/calendrier.jpg")

screen = pg.display.set_mode((bg.get_width(),bg.get_height()))
screen.blit(bg,(0,0))

caseW = bg.get_width()//5
caseH = bg.get_height()//5
lstImage=[[[None,False] for i in range(5)] for i in range(5)]
for i in range(5):
    lstImage[0][i][0] = pg.image.load("C:/Users/leophancao/Documents/NSI/Divers/Avent/"+str(i)+".jpg")

while 1:
    for i in range(len(lstImage)):
        for k in range(len(lstImage[i])):
            if lstImage[i][k][1]:
                if lstImage[i][k][0]:
                    screen.blit(lstImage[i][k][0],(i*caseW,k*caseH))
    pg.display.update() 
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            sys.exit()
        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            caseX = pos[0]//caseW
            caseY = pos[1]//caseH
            lstImage[caseX][caseY][1]=True