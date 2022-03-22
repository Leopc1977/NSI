from random import randint
from copy import deepcopy
class Vector2():
    """
    n: nombre de ligne
    m: nombre de ressources
    renvoie un vecteur2 de taille (n,m)
    """
    def __init__(s,n,m):
        s.v = [[0 for i in range(m)] for i in range(n)]
        s.n = n
        s.m = m
    def pprint(s):
        for i in s.v:
            print(i)
    def sub(s,vec):
        for i in range(len(s.v)):
            for k in range(len(s.v[i])):
                s.v[i][k]-=vec.v[i][k]
        return s.v
    def addInt(s,k):
        for i in range(len(s.v)):
            for k in range(len(s.v[i])):
                s.v[i][k]+=k      
    def add(s,vec):
        for i in range(len(s.v)):
            for k in range(len(s.v[i])):
                s.v[i][k]+=vec.v[i][k]
        return s.v

    def __le__(s, vec2):
        for i in range(s.m):
            for k in range(s.n):
                if s.v[k][i] > vec2.v[k][i]:
                    return False
        return True

def getMaxSystem(m,max):
    vec = Vector2(m,1)
    for i in range(m):
        vec.v[i] = randint(max-3,max)
    return vec

def getMaxToFinish(n,m,maxSystem):
    vec = Vector2(n,m)
    for i in range(len(vec.v)):
        for k in range(len(vec.v[i])):
            vec.v[i][k]=randint(1, maxSystem.v[k])
    return vec

def getAlloc(max,maxSystem):
    alloc = deepcopy(max)
    for c in range(len(max.v[0])):
        total = 0
        for l in range(len(max.v)):  
            sub = randint(0,1)
            if total+sub < maxSystem.v[c]:
                total+=sub
                alloc.v[l][c]=sub 
    return alloc

def calcAvailable(maxSystem,alloc):
    available = deepcopy(maxSystem)
    for c in range(len(maxSystem.v)):
        sub = 0
        for l in range(len(alloc.v)):
            sub+= alloc.v[l][c]
        available.v[c]-=sub
    return available

def minNeed(need):
    lstSum = []
    for i in range(len(need.v)):
        lstSum.append(sum(need.v[i]))         
    return lstSum.index(min(lstSum))
    
maxProcess = 50
nbRessources = 30
nbProcessus = 10

#maximum de ressources allouables par le système pour chaque ressource 
print("==========MAX_SYSTEM==========")
maxSystem = getMaxSystem(nbRessources,maxProcess)
print(maxSystem.v)

#objectifs de ressources à atteindre pour chaque processus 
print("==========MAX_PROCESS_TO_FINISH==========")
max = getMaxToFinish(nbProcessus,nbRessources,maxSystem)
max.pprint()

#Ressources alloué pour chaque processus
print("==========ALLOC==========")
alloc = getAlloc(deepcopy(max),deepcopy(maxSystem))
alloc.pprint()

endProcessus = False 
nbLoop = 0
margeError = 10
while True:
    print("==========BOUCLE n°"+str(nbLoop)+"==========")
    #Ressources demandé pour chaque processus pour finir 
    print("==========NEED==========")
    need = deepcopy(max)
    need.sub(alloc)
    need.pprint()

    #Ressources allouable par le systeme
    print("==========AVAILABLE==========")
    available = calcAvailable(maxSystem, alloc)
    print(available.v)

    print("==========BANQUIER==========")
    processIndex = minNeed(need)
    currentProcessNeed = need.v[processIndex]
    if currentProcessNeed <= available.v:
        alloc.v.remove(alloc.v[processIndex])
        alloc.n-=1
        max.v.remove(max.v[processIndex])
        max.n-=1
        need.v.remove(need.v[processIndex])
        need.n-=1
        nbProcessus-=1
        available = calcAvailable(maxSystem, alloc)
    nbLoop+=1
    if max.v == []:
        print("==========[FINI]: 0 PROCESSUS==========")
        break
    if nbLoop >nbProcessus+margeError:
        print("==========[BLOCAGE]: "+str(nbProcessus)+"_PROCESSUS==========")
        break