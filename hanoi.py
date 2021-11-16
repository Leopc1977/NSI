class Hanoi():
    def __init__(self):
        self.n = 3#int(input("Choissisez le nombre de ronds:"))
        self.lstEmplacements=[[i for i in range(self.n,0,-1)],[],[]]
        print(self.lstEmplacements)

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

    def Play(self):
        if self.lstEmplacements==[[],[],[i for i in range(self.n,0,-1)]]:
            print("Gagné !")
            return
        start = int(input("A quel emplacement voulez vous déplacer ?"))
        end = int(input("Vers où ?"))
        self.Move(start,end)
        print(self.lstEmplacements)
        self.Play()

testHanoi=Hanoi()
testHanoi.Play()