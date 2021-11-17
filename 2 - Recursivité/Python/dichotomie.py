from random import randint

def d(lst,e):
    m=len(lst)//2
    currentElement=lst[m]
    if len(lst)==0:
        return None
    elif len(lst)==1: 
        lastIsGood=lst[0]==e
        return lastIsGood
    elif currentElement==e:
        return True
    elif e<currentElement:
        return d(lst[:m],e)
    else:
        return d(lst[m:],e)

def d2(lst,e,start,end):
    lenLst=end-start
    m=lenLst//2
    currentElement=lst[m]
    
    if lenLst==0:
        return None
    elif lenLst==1: 
        lastIsGood=lst[m]==e
        return lastIsGood
    elif currentElement==e: 
        return True
    elif e<currentElement:
        return d2(lst,e,start,end-lenLst//2)
    else:
        return d2(lst,e,start+lenLst//2,end)

for i in range(20):
    lst = [randint(-10,10) for i in range(10)]
    lst.sort()
    print(lst)
    print("Quel est la valeur recherchée ?")
    s=int(input())
    print(d2(lst,s,0,len(lst)-1))