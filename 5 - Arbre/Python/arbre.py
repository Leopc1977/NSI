class Arbre:
    def __init__(s,pArbre):
        s.dict = pArbre
        s.matriceAdj = [[0 for i in range(len(pArbre))] for i in range(len(arbre))]
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

    """
    function deepcopy(orig)
        local orig_type = type(orig)
        local copy
        if orig_type == 'table' then
            copy = {}
            for orig_key, orig_value in next, orig, nil do
                copy[deepcopy(orig_key)] = deepcopy(orig_value)
            end
            setmetatable(copy, deepcopy(getmetatable(orig)))
        else -- number, string, boolean, etc
            copy = orig
        end
        return copy
    end
    """

    def getdeepFrom(s,coord,deep):
        if s.isLeaf(coord):
            return deep
        l,c = coord[0],coord[1]
        lstChilds = s.getChilds(coord)
        for i in range(len(lstChilds)):
            print(s.getdeepFrom(lstChilds[i],deep+1))
        return deep



    
arbre = { 0:[1 , 2 , 3] , 1:[4 , 5 ] , 2:[6] , 3:[7 , 8] , 4:[] , 5:[] , 6:[] , 7:[] , 8 : [9,10] , 9:[], 10:[]}
a = Arbre(arbre)
a.pprint()
a.getdeepFrom((0,3),0)