from random import randint, shuffle

def createDict(n):
    dict = {}
    nodes = list(range(n))
    for i in range(n):
        shuffle(nodes)      
        dict[i] = nodes[:randint(1,n)]
    return dict

def chemin (g, start,end):
    """ dict g : graphe
        int start,end : noeud
    """

    #pile à visiter (gris)
    pile = [start] 
    #chemin
    path = pile
    #coloriage/marquage
    couleur = {i:0 for i in g}

    while pile != []:
        print(couleur)
        node = pile.pop()
        couleur[node]=2 #noir, sommet visité
        path.append(node)
        #cas de base
        if node == end:
            return path
        #iter succ 
        for n in g[node]:
            if couleur[n]==0:
                pile.append(n)
                couleur[n]=1
     
    return False

def parcoursDFS (g, start):
    """ dict g : graphe
        int start,end : noeud
    """

    #pile à visiter (gris)
    pile = [start]
    #chemin
    path = [] 
    #coloriage/marquage
    couleur = {i:0 for i in g}

    while pile != [] or len(path)==len(g):
        if not pile:
            return path

        node = pile.pop()
        couleur[node]=2 #noir, sommet visité
        path.append(node)
        #iter succ 
        for succ in g[node]:
            if couleur[succ] == 0:
                couleur[succ]=1
                pile.append(succ) 
    return path

def parcoursBFS(g,start):
    """ dict g : graphe
        int start,end : noeud
    """
    pile = [start]
    path = []

    couleur = {i:0 for i in g}

    while pile != []:
        node = pile.pop()
        couleur[node]=2
        path.append(node)

        for succ in g[node]:
            if couleur[succ]==0:
                couleur[succ]=1
                pile = [succ]+pile
    return path

def distanceFrom(g,start):
    """
    noeuds atteinable depuis start, un parcours largeur avec avec enregistrement depuis à start
    """
    dist = 0

    pile = [(start,0)]
    path = [(start,dist)]
    couleur = {i:0 for i in g}
  
    while pile != []:
        node = pile.pop()
        couleur[node[0]]=2

        dist=node[1]+1
        for succ in g[node[0]]:
            if couleur[succ]==0:
                couleur[succ]=1
                pile = [(succ,dist)]+pile
                path.append((succ,dist))
    return path


g = {4:[2,5,6],2:[1,3,4],1:[2],3:[2],5:[4],6:[4,7],7:[6]}#createDict(5)
print(g)

print(distanceFrom(g,4))