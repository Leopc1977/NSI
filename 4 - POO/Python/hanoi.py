from _typeshed import ReadableBuffer
from turtle import *

class Hanoi():
    def __init__(self, nbDisk):
        print("=======================================================")
        print("\tFonction PlayStepbyStep : jouer pas à pas")
        print("=======================================================")
        print("\tFonction Resolve : résoudre la tour de Hanoi")
        print("=======================================================")

        self.n = nbDisk
        self.lstEmplacements=[[i for i in range(self.n,0,-1)],[],[]]
        self.firstTower, self.secondTower, self.thirdTower  = [i for i in range(self.n,0,-1)],[],[]

        self.colors=["navy","purple","violet","pink","blue","red","cyan","green","yellow"]
        self.disks=[]
        for i in range(n):
            t = Turtle()
            t.shape("square")
            t.shapesize(1,3+i)
            t.color(self.colors[i])
            self.disks.append(t)

        #print(self.lstEmplacements)

    def Affiche(s):
        print(s.firstTower)
        print(s.secondTower)
        print(s.thirdTower)
        print("=======================================================")

    def Move(self,start,end):
        if len(self.lstEmplacements[start-1])==0:
            return self.Play()
        startElement = self.lstEmplacements[start-1][-1]
        if len(self.lstEmplacements[end-1])==0: #emplacement vide
            self.lstEmplacements[start-1].pop(-1)
            self.lstEmplacements[end-1].append(startElement)
        else: #plusieurs ronds
            endElement = self.lstEmplacements[end-1][-1]
            print(startElement, endElement)
            if endElement>startElement:
                self.lstEmplacements[start-1].pop(-1) 
                self.lstEmplacements[end-1].append(startElement)

    def PlayStepbyStep(self):
        if self.lstEmplacements==[[],[],[i for i in range(self.n,0,-1)]]:
            print("Gagné !")
            return
        start = int(input("A quel emplacement voulez vous déplacer ?"))
        end = int(input("Vers où ?"))
        self.Move(start,end)
        print(self.lstEmplacements)
        self.PlayStepbyStep()

    def Resolve(self,n, firstTower, secondTower, thirdTower):
        self.firstTower, self.secondTower, self.thirdTower = firstTower, secondTower, thirdTower
        if n>0:
            self.Resolve(n - 1, firstTower, thirdTower, secondTower)
            if firstTower:
                thirdTower.append(firstTower.pop())
                self.Affiche()
            self.Resolve(n-1, secondTower, firstTower, thirdTower)
    def line(s, x,y,tourne,l,key):
        up()
        goto(x,y)
        left(tourne)
        down()
        color("black")
        forward(l)
        write(key+2)
        right(tourne)

    def Draw(s):
        xPeg = -200
        y0 = -100
        s.line(-600,y0,0,1200,0)
        for t in range(s.n,-1,-1):
            #pieu
            x,y,tourne,l,key = xPeg*(t-1),y0,90,500,0
            up()
            goto(x,y)
            left(tourne)
            down()
            color("black")
            forward(l)
            write(key+2)
            right(tourne)

            #disk
            for d in s.lstEmplacements[t]:
                pass


setup(600,600)
speed("fastest")
n=3
testHanoi=Hanoi(n)
testHanoi.Draw()

testHanoi.Resolve(n,testHanoi.lstEmplacements[0],[],[])
done()