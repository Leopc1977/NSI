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
        self.disks=[[],[],[]]
        for i in range(n):
            t = Turtle()
            t.shape("square")
            t.shapesize(1,3+i)
            t.color(self.colors[i])
            self.disks[0].append(t)

    def resolveDraw(s,n , source, destination, auxiliary):
        if n==1:
            print ("Move disk 1 from source",source,"to destination",destination)
            s.disks[destination].append(s.disks[source].pop(-1))
            s.lstEmplacements[destination].append(s.lstEmplacements[source].pop(-1))
            return
        s.resolveDraw(n-1, source, auxiliary, destination)
        print("Move disk",n,"from source",source,"to destination",destination)
        s.Draw()
        s.resolveDraw(n-1, auxiliary, destination, source)

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
        y0 = -250
        s.line(-500,y0,0,700,0)
        for t in range(s.n-1,0,-1):
            #pieu
            x,y,tourne,l,key = xPeg*(t-1),y0,90,500,0
            up()
            goto(x,y)
            left(tourne)
            down()
            color("black")
            forward(l)
            write(key+1)
            right(tourne)

            #disk of the current tower
            """for k in range(len(s.disks[t])-1,0,-1):
                d = s.disks[t][k]
                d.goto(x, y0)"""

setup(600,600)
speed("fastest")
n=3
testHanoi=Hanoi(n)
#testHanoi.Draw()

#testHanoi.Resolve(n,testHanoi.lstEmplacements[0],[],[])
testHanoi.resolveDraw(n, 0,2,1)
done()