from math import inf
from operator import index
from random import randint
import string

#fonctions pprint
def pprintMatrix(matrix):
    ascii_char_col = ord("A")
    print(" :  ",end="|")
    for i in range(len(matrix)):
        print("  %s   " %(chr(ascii_char_col)),end="|")
        ascii_char_col+=1
    print()
    ascii_char_line = ord("A")

    for i in range(len(matrix)):
        l=matrix[i]
        print("%s:  |" %(chr(ascii_char_line)),end="")
        ascii_char_line+=1

        for k in range(len(matrix[0])):
            c = l[k]
            if c==inf: 
                print("  inf ",end="|")
            elif c<10:
                print("  %s   " %(str(c)),end="|")
            else: 
                print("  %s  " %(str(c)),end="|")

        print()
def pprintLine(line):    
    ascii_A=ord("A")
    for tuple in line:
        letterFrom = ascii_A+tuple[1]
        dist = tuple[0]
        if dist == "x":
            print("  x   ",end="|")
        elif dist == inf:
            print("  inf ",end="|")
        elif dist < 10:
            print(" %s(%s) " %(str(dist),chr(letterFrom)),end="|")
        else:
            print(" %s(%s)" %(str(dist),chr(letterFrom)),end="|")
    print()

#variables
matrixTest =  [
     [0 , inf , inf , 13 , inf , inf , 5 , inf ],
 [8 , 0 , 6 , 5 , inf , inf , 10 , inf ],
 [19 , 11 , 0 , inf , 16 , 17 , 12 , inf] ,
 [14 , inf , 10 , 0 , 19 , inf , inf , inf] ,
 [inf , 8 , inf , 15 , 0 , inf , inf , 8 ],
 [inf , 10 , inf , inf , inf , 0 , 10 , inf] ,
 [inf , 6 , 16 , inf , 10 , 20 , 0 , inf ],
 [7 , 8 , inf , inf , 17 , 15 , 20 , 0 ]
 ]
letter =  list(string.ascii_uppercase[:10])
dijkstraTab = []
currentNode = 0
min = 0
lengthMatrix = len(matrixTest)
#liste des distances du départ vers le noeud correpandant à l'index
#(distance,provenance)
liste_distance = [(inf,None) for _ in range(lengthMatrix)] 

frozen = [0 for _ in range(lengthMatrix)]

print("____________________[MATRICE TEST]__________________________\n")
pprintMatrix(matrixTest)

print("_________________________[DIJKSTRA]_________________________\n")
#initialisation
line = [(inf,currentNode) for _ in range(lengthMatrix)]
line[currentNode]=(0,currentNode)
liste_distance[currentNode]=(0,currentNode)
frozen[currentNode]=1

dijkstraTab.append(line)
pprintLine(line)
#print("Noeud initial:",letter[currentNode])

#dijkstra
for _ in range(lengthMatrix):
    frozen[currentNode]=1

    line = [("x",currentNode) for _ in range(lengthMatrix)]
#cherche minimum des successeurs du noeud courant
    min = 0
    if min == currentNode:
        min = currentNode-1

    for c in range(lengthMatrix):
        currentColumnValue = matrixTest[currentNode][c]
        currentMinValue = matrixTest[currentNode][min]
        if c!=currentNode and frozen[c]==0:
            if currentColumnValue < currentMinValue:
                min = c

#cherche meileur distance vers le noeud c (letter[c])
        oldBestDistance = dijkstraTab[0][c]
       #oldBestDistance=(distance,provenance)
        if dijkstraTab[-1][c][0]!="x":
            for i in range(len(dijkstraTab)):
                if dijkstraTab[i][c][0] != "x":
                    if dijkstraTab[i][c][0] < oldBestDistance[0]:
                        oldBestDistance = dijkstraTab[i][c]

            distProvenance = dijkstraTab[0][currentNode][0]
            for i in range(len(dijkstraTab)):
                if dijkstraTab[i][currentNode][0] != "x":
                    if dijkstraTab[i][currentNode][0] < distProvenance:
                        distProvenance = dijkstraTab[i][currentNode][0]

            totalCurrentDistance = currentColumnValue+distProvenance
            if totalCurrentDistance < oldBestDistance[0]:
                line[c]=(totalCurrentDistance,currentNode)
                liste_distance[c]=(totalCurrentDistance,currentNode)
            elif totalCurrentDistance > oldBestDistance[0] and totalCurrentDistance != inf:
                line[c]=oldBestDistance
            elif oldBestDistance[0] == inf:
                line[c]=(inf,currentNode)

    pprintLine(line)
    dijkstraTab.append(line)
    currentNode = min
    print("Change de noeud:",letter[currentNode])

print("__________________________________________________________________\n")

print(liste_distance)

def routage(liste_dist,currentNode,goalNode):
    if currentNode==goalNode:
        print("Noeud d'arrivée: %s" %(letter[currentNode]))
        return [(0,goalNode)]

    print("Noeud: %s" %(letter[currentNode]))
    return [(liste_dist[currentNode])]+routage(liste_dist,liste_dist[currentNode][1],goalNode)

depart = 2
arrivee = 0
print("Noeud de départ: %s" %(depart))
print(routage(liste_distance,depart,arrivee))
