class Stack():
    def __init__(s):
        s.items = []
    def push(s,item):  s.items.append(item)
    def pop(s):        return s.items.pop(-1)
    def isEmpty(s):    return s.items == []
    def getPeek(s):    return s.items[-1]
    def getSize(s):    return len(s.items)
    def print(s):      print(s.items)
    def getMax(s):
        save = Stack()
        max = s.pop()
        save.push(max)
        indiceMax = 1
        cnt = 1

        while not s.isEmpty():
            peek = s.pop()
            cnt=cnt+1
            if peek>max:
                max = peek
                indiceMax = cnt
            save.push(peek)

        while not save.isEmpty():
            s.push(save.pop())
        return indiceMax
    def reverse(s,end):
        pileReverse = Stack()
        pileOrder = Stack()
        for i in range(end):
            pileReverse.push(s.pop())
        for i in range(end):
            pileOrder.push(pileReverse.pop()) 
        for i in range(end):
            s.push(pileOrder.pop()) 
    def getMax2(s,end):
        save = Stack()
        max = s.pop()
        save.push(max)
        indiceMax = 1
        cnt = 1
        while cnt < end:
            peek = s.pop()
            cnt=cnt+1
            if peek>max:
                max = peek
                indiceMax = cnt
            save.push(peek)
        while not save.isEmpty():
            s.push(save.pop())
        return indiceMax
    def pancakesMiamNon(s,len):
        if len<=2:
            return s.items
        iMax = s.getMax2(len)
        s.reverse(iMax)
        s.reverse(len)
        return s.pancakesMiamNon(len-1)
    def len(s):
        return len(s.items)
class Arbre:
    def __init__(s,pArbre):
        s.dict = pArbre
        s.matriceAdj = [[0 for i in range(len(pArbre))] for i in range(len(pArbre))]
        for key,values in pArbre.items():
            for v in values:
                s.matriceAdj[key][v]=1
    def pprint(s):
        lst = s.matriceAdj
        for l in range(len(lst)):
            print("| ",end="")
            for c in range(len(lst[l])):
                print(lst[l][c],end=' | ')
            print("")          
    def isLeaf(s,coord): 
        l,c = coord[0],coord[1]
        for i in range(len(s.matriceAdj)):
            if (s.matriceAdj[c][i]==1):
                return False
        return True
    def hasOneFather(s,coord):
        l,c = coord[0],coord[1]
        nbFather = 0
        for i in range(len(s.matriceAdj)):
            if (s.matriceAdj[i][c]==1):
                nbFather += 1
        return nbFather==1
    def getChilds(s,coord):
        l,c = coord[0],coord[1]
        lstChilds = []
        for i in range(len(s.matriceAdj)):
            if (s.matriceAdj[l][i] == 1):
                lstChilds.append((l,i))
        return lstChilds

    def DepthFirstSearch(s):
        pile = Stack()
        pile.push(0)
        while not pile.isEmpty():
            currentNodeLine = pile.pop()
            lstChilds = s.getChilds((currentNodeLine,"_"))
            for i in range(len(lstChilds)):
                print(lstChilds[i][1])
                pile.push(lstChilds[i][1])
    
    def DFSRecursive(s,pos,pile,lstNode):
        if s.isLeaf(("_",pos)):
            return pos
        lstChilds = s.getChilds((pos,"_"))
        for child in lstChilds:
            lstNode.append(child[1])
            pile.push(s.DFSRecursive(child[1],pile,lstNode))
        return (pile,lstNode)

    def parcours_profondeur(s):
        n = len(s.matriceAdj)
        pile = Stack()
        pile.push(0)
        while not pile.isEmpty():
            currentNode = pile.pop()
            childs = s.getChilds((currentNode,"_"))
            childs.reverse()
            for child in childs:
                pile.push(child[1])

    def parcourBF(s):
        file = [0]
        parcours = []
        
arbre = { 0:[1 , 2 , 3] , 1:[4 , 5 ] , 2:[6] , 3:[7 , 8] , 4:[] , 5:[] , 6:[] , 7:[] , 8 : [9,10] , 9:[], 10:[]}
a = Arbre(arbre)
#a.DepthFirstSearch()
#print(a.DFSRecursive(0,Stack(),[])[1])
a.parcours_profondeur(  )