from random import randint, shuffle

def dictToAdjMatrix(dict):
    n = len(dict)
    res = [[0 for _ in range(n)] for _ in range(n)]
    # i->j
    for i in dict:
        for j in dict[i]:
            res[i][j]=1
    return res
arbre = { 0:[1 , 2 , 3] , 1:[4 , 5 ] , 2:[6] , 3:[7 , 8] , 4:[] , 5:[] , 6:[] , 7:[] , 8 : [9,10] , 9:[], 10:[]}
AdjMatrix = dictToAdjMatrix(arbre)

def adjMatrixToDict(lst):
    dict = {}
    for i in range(len(lst)):
        dict[i]=[]
        for j in range(len(lst[i])):
            if lst[i][j] == 1:
                dict[i].append(j)
    return dict
arbreTest = adjMatrixToDict(AdjMatrix)
assert (arbreTest==arbre)

def createAdj(n):
    return [[randint(0,1) for _ in range(n)] for _ in range(n)]

def createDict(n):
    dict = {}
    nodes = list(range(n))
    for i in range(n):
        shuffle(nodes)
        dict[i] = nodes[:randint(0,3)]
    return dict 

def isOriented(adjMatrice):
    for i in range(len(adjMatrice)):
        for j in range(len(adjMatrice[i])):
            if adjMatrice[i][j]!=adjMatrice[j][i]:
                return False
    return True
dictTest = createDict(5)