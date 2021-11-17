def divideLst2(lst):
    #divise une liste en deux
    m = len(lst)//2
    return lst[:m], lst[m:]
i=0
def merge(lst1,lst2): #fusion de lst1 et lst2
    global i
    lst = []
    len1=len(lst1)
    len2=len(lst2)
    index1,index2=0,0

    #tri
    while index1<len1 and index2<len2:
        if lst1[index1]>lst2[index2]:
            lst.append(lst2[index2])
            index2+=1
        elif lst1[index1]<=lst2[index2]:
            lst.append(lst1[index1])
            index1+=1
        i+=1
    #Ajoute les elements restants
    if lst1:
        lst+=lst1[index1:]
    if lst2:
        lst+=lst2[index2:]
    return lst

def mergeSort(lst): #renvoie une liste triée
    #cas partiuliers
    if len(lst)<=1:
        return lst 
    else:
        lst1,lst2=divideLst2(lst)
        res1=mergeSort(lst1)
        res2=mergeSort(lst2)
        return merge(res1,res2)

#Tests
from random import *
"""for n in range (1,2000,50):
    m=0
    for k in range(100):
        i=0
        lst = [randint(-20,20)for j in range(n)]
        lstTriée = mergeSort(lst)
        m+=i
    print("pour n=",n,":",m/100)"""
    
def triParSelection(lst):
    n=len(lst)
    for i in range(n):
        j=i
        for k in range(i+1,n):
            if lst[j] > lst[k]:
                j=k
        lst[i],lst[j]=lst[j],lst[i]
from time import *
lst=[randint(-20,20)for j in range(10000)]
lst1=lst
print(lst1)
t1 = perf_counter()
triParSelection(lst1)
t2=perf_counter()
print(t2-t1)

lst=[randint(-20,20)for j in range(10000)]
t1 = perf_counter()
mergeSort(lst)
t2=perf_counter()
print(t2-t1)
            
