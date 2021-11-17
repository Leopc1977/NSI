from random import *
from pygame import color
import sys
import pygame as pg

seed(randint(1,100)) #garder le randint pour avoir un labyrinthe 99.99% aléatoire

class Map():
    def  __init__(self,m,n):
        self.m = m
        self.n = n
        self.map=[]
        self.resolved=False
    
    def gen(self):
        laby = []
        nbLig = self.m
        nbCol = self.n
        bord= [ 3 for c in range (nbCol+2)]  ## bordure haute, murs non cassables
        laby.append(bord)
        for l in range(1, nbLig+1) :
            if l %2 == 0 :
                ligne = [ 2 for c in range (nbCol)]  ## ligne de murs cassables
                ligne=[3] + ligne + [3]
            else :
                ligne = [3] ## mur extérieur non cassable, bord gauche
                for c in range (1, nbCol+1) :
                    if c % 2 == 0 :
                        ligne.append(2)
                    else :
                        ligne.append(0)   ## 0 pour cellule libre
                ligne.append(3)  ## bord droit
            laby.append(ligne)
        laby.append(bord)  ## bord du bas

        ## Entrée et sortie (code 4 sur les bords)
        laby[1][0]= 4    ## entrée
        laby[-2][-1]= 5 ## sortie
        self.map = laby

    def randomizeMap (self,laby , pile) :
        height = len(laby)
        width = len(laby[0])
        ## cas de terminaison
        if len(pile) == 0 :
            return laby
        ## sinon, on prend la cellule courante au sommet de la pile
        (x , y ) = pile[-1]
        laby[x][y] = 1 ## visité
        ## Examiner les cellules voisines (N/S/E/O) non encore visitées.
        voisins = []  ## liste des coordonnées des cellules libres voisines (code 0 ou 2)
        ## on regarde par dessus les murs ici
        for i in (-2,2) : ## sans visiter les bordures (3)
            if 0< x+i < height-1  and laby[x+i][y] in (0,2):
                voisins.append( (x+i , y) )
        for j in (-2,2) :
            if 0< y+j < width-1 and laby[x][y+j] in (0,2) :
                voisins.append( (x , y+j) )
        nbVoisins = len(voisins)
        if nbVoisins == 0 and len(pile) >0 :
            pile.pop()   ## depiler, retour en arrière 
        else : 
        ## choisir un voisin aléatoirement,
        ## casser si besoin le mur qui le sépare de la cellule courante
            next = voisins[randint(0,nbVoisins-1)]
            laby[next[0]][next[1]]= 1   ## visitée
            laby[ (x + next[0]) //2][(y + next[1]) //2] = 1 ## visitée (mur cassé)
            pile.append( next )
        ## on recommence, récursivement
        return self.randomizeMap (laby, pile)
    
    def resolve(self,pos,pile):
        #print(pile)
        if self.resolved==False:
            #print("Current pos:",pos)
            l,c=pos[0],pos[1]
            self.map[l][c]=20 #VISITED
            voisins=[(l-1,c,'n'), (l,c-1,'w'), (l+1,c,'s'), (l,c+1,'e')]
            #FILTRE LES VOISINS VALIDES
            for i in range(len(voisins)-1,-1,-1):
                currentVoisin = voisins[i]
                line,column = currentVoisin[0],currentVoisin[1]
                typeCase=self.map[line][column]
                #print("TYPE CASE: ",typeCase)
                #CASE D'ARRIVEE
                if typeCase==5:
                    #pile.append((currentVoisin[0],currentVoisin[1],currentVoisin[2]))
                    pile.append((l,c,'e')) #la case sortie est à droite donc east
                    for j in range(len(pile)): #met à jour la map avec pathfinding
                        line,column=pile[j][0],pile[j][1]
                        dir = pile[j][2]
                        self.map[line][column]=(10,dir) 
                    #print("found the exit at ",line,column,"!")
                    self.resolved = True
                    return pile
                elif line <0 or column <0 or line >= len(self.map) or column>=len(self.map[0]):
                    voisins.pop(i)
                elif typeCase!=1: 
                    voisins.pop(i)
            #print("Voisins après tri : ",voisins," len:",len(voisins))
            #print(pile)
            
            if len(voisins)==0: #CHEMIN SANS ISSUE
                #print("pas de chemin pos: ",l,c)
                return None
            elif len(voisins)==1: #CHEMIN UNIQUE
                #print('chemin unique pos: ',l,c)            
                line, column =voisins[0][0],voisins[0][1] 
                pile.append((l,c,voisins[0][2]))
                return self.resolve((line,column),pile)
            else: #PLUSIEURS CHEMINS
                #print("plusieurs chemins pos: ",voisins) 
                for i in range(len(voisins)): #2 chemins
                    currentVoisin = voisins[i]
                    lVoisin, cVoisin =currentVoisin[0],currentVoisin[1] 
                    tmpPile=list(pile)
                    dir = currentVoisin[2]
                    tmpPile.append((l,c,dir))
                    tmpPile.append(currentVoisin)
                    self.resolve((lVoisin,cVoisin),tmpPile)
        else:
            return None

    def affiche(self):
        _map = self.map
        print("Affichage de la map....")
        for l in range(len(_map)):
            for c in range(len(_map[0])):
                print(_map[l][c], end=" ")
            print("\n")
        print("Fin de l'affichage") 

    def Load(self):
        self.gen()
        self.map = self.randomizeMap(self.map,[(3,1)])
        startPos = (1,1)
        self.pile=self.resolve(startPos,[])
        #self.affiche()
        pg.init()

testMap = Map(21,21) #l,c
testMap.Load()

tileSet=[pg.image.load("res/break.png"),pg.image.load("res/way.png"),pg.image.load("res/wall.png"),pg.image.load("res/start.png"),pg.image.load("res/end.png"),pg.image.load("res/path.png"),pg.image.load("res/visited.png")]
display_surface = pg.display.set_mode((32*testMap.m+64,32*testMap.n+64))

while 1:
    line,column = testMap.m, testMap.n
    display_surface.fill((255,255,0))

    for l in range(len(testMap.map)):
        for c in range(len(testMap.map[0])):
            x=(c*32)
            y=(l*32)
            e=testMap.map[l][c]
            if e==4:
                display_surface.blit(tileSet[3],(x,y))  #START
            elif e == 5:
                display_surface.blit(tileSet[4],(x,y))  #END
            elif e==3:
                display_surface.blit(tileSet[2], (x,y)) #WALL EXTERIEUR
            elif e==2:
                display_surface.blit(tileSet[0], (x,y)) #WALL INTERIEUR
            elif e==1 or e==20:
                display_surface.blit(tileSet[1],(x,y))  #WHITE WAY
            """elif e==10:
                display_surface.blit(tileSet[6],(x,y)) #VISITED"""
            else: 
                #print(e)
                dir = e[1]
                if dir == 'n':
                    angle=0
                elif dir == 'w': #west 90
                    angle=90
                elif dir == 's': #south 180
                    angle=180
                elif dir == 'e': #east 90*3
                    angle=90*3
                img = pg.transform.rotate(tileSet[5], angle)
                display_surface.blit(img,(x,y)) #FLECHE WAY
                
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            sys.exit()
        pg.display.update() 
