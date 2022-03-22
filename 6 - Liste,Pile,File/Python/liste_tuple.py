def ajouter_en_tete(v,lst): #cons
    if lst==None:
        return ((v,None))
    return (v,lst)

def creer_liste_videe():
    return None

def count(lst,n):
    if lst[0]==None:
        return 0
    if lst[1]==None:
        return n+1
    return count(lst[1],n+1)

def est_vide(lst):
    return lst==None

def supprimer_en_tete(lst):
    lst = lst[1]
    #return lst[1]

lst = creer_liste_videe()
lst = ajouter_en_tete(1,lst)
lst = ajouter_en_tete(2,lst)
lst = ajouter_en_tete(3,lst)
print(lst)
print(supprimer_en_tete(lst))
print(lst)