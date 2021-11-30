def pprint(lst):
    for l in range(len(lst)):
        print("| ",end="")
        for c in range(len(lst[l])):
            print(lst[l][c],end=' | ')
        print("")

def resolve(lst,pos,end,path,score):
    #cas de fin
    if (pos[0],pos[1]) == end:
        return (path,score)
    l,c=pos[0],pos[1]
    s,e = (l+1,c,"s"),(l,c+1,"e")
    destPos = ()
    pointS,pointE =0,0
    #depassement tableau
    if s[0]==len(lst):
        pointE = lst[e[0]][e[1]]
        path.append(e)
        destPos = e
        score+= pointE 
        return resolve(lst,destPos,end,path,score)
    elif e[1]==len(lst[0]):
        pointS=lst[s[0]][s[1]]
        path.append(s)
        destPos = s
        score+= pointS 
        return resolve(lst,destPos,end,path,score)
    #meilleur choix
    pointS,pointE = lst[s[0]][s[1]],lst[e[0]][e[1]]
    if pointS >= pointE:
        path.append(s)
        destPos = s
        score+= pointS
    else:
        path.append(e)
        destPos = e
        score+= pointE
    return resolve(lst,destPos,end,path,score)

def allWayPossible(map,currentPos,allPaths):
    #cas de base
    endPos = (len(map)-1,len(map[0])-1)
    if currentPos == endPos:
        allPaths.append(currentPos)
        return allPaths

    l,c=currentPos[0],currentPos[1]
    southPos,eastPos = (l+1,c),(l,c+1)

    #ajout pos + ajout paths possibles
    #dépassement par bas
    allPaths.append(currentPos)
    if southPos[0] > endPos[0]:
        e = allWayPossible(map,eastPos,allPaths)
        allPaths.append(e)
        return allPaths
    #dépassement par droite
    elif eastPos[1] > endPos[1]:
        s = allWayPossible(map,southPos,allPaths)
        allPaths.append(s)
        return allPaths
    else:
        e = allWayPossible(map,eastPos,allPaths)
        s = allWayPossible(map,southPos,allPaths)
        allPaths.append(s)
        allPaths.append(e)
        return allPaths

from random import randint, seed
l=3
c=4
start = (l-2,c-2)
end = (l-1,c-1)
seed(1)

lst1 = [[randint(0,9) for i in range(c)] for i in range(l)]
p = allWayPossible(lst1,start,[])
paths = []
start = 0
pprint(lst1)
print(p)
print("==========================")

for oc in range(len(p)):
    ocouch = p[i]
    for so in range(len())
for i in range(len(p)):
    path = p[i]
    print("current path",path)
    if path == end:
        paths.append([p[start:i+1]])
        start = i

for path in paths:
    for ath in path:
        print(ath)
        print("==========================")
