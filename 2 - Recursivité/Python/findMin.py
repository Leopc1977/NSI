from random import randint

etape=0

def fMin(lst,indice,minimum):
    global etape
    if indice==0:
        print(minimum)
    else:
        etape+=1
        e=lst[indice]
        if minimum > e:
            minimum= e
        fMin(lst,indice-1,minimum)
        
for i in range(20):
    etape=0
    lst1=[randint(-10,10) for i in range(20)]
    print(lst1)
    fMin(lst1,len(lst1)-1,lst1[len(lst1)-1])
    print(etape)

