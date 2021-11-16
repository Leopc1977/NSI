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
        #print(self.lstEmplacements)

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
        self.Play()

    def Resolve(self,n, firstTower, secondTower, thirdTower):
        self.firstTower, self.secondTower, self.thirdTower = firstTower, secondTower, thirdTower
        print(self.firstTower, self.secondTower, self.thirdTower)
        if n > 0:
            # move tower of size n - 1 to helper:
            self.Resolve(n - 1, firstTower, thirdTower, secondTower)
            # move disk from source peg to target peg
            if firstTower:
                thirdTower.append(firstTower.pop())
            # move tower of size n-1 from secondTower to target
            self.Resolve(n-1, secondTower, firstTower, thirdTower)

testHanoi=Hanoi(3)
testHanoi.Resolve(len(testHanoi.lstEmplacements[0]),testHanoi.lstEmplacements[0],[],[])
print(testHanoi.firstTower, testHanoi.secondTower, testHanoi.thirdTower)