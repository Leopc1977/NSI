class Maillon:
    def __init__(s,v):
        s.value = v
        s.suivant = None

class File: 
    def __init__(s):
        s.dernier_file = None

    def enfile(s,element):
        nouveau_maillon = Maillon(element)
        nouveau_maillon.suivant = s.dernier_file
        s.dernier_file = nouveau_maillon

    def est_vide(s):
        return s.dernier_file == None

    def affiche(s):
        maillon = s.dernier_file
        while maillon != None:
            print(maillon.value,end=", ")
            maillon = maillon.suivant
        print()

    def defile(s):
        if not s.est_vide():
            if s.dernier_file.suivant == None:
                resultat = s.dernier_file.value
                s.dernier_file = None
                return resultat
            maillon = s.dernier_file
            while maillon.suivant.suivant != None:
                maillon = maillon.suivant
            resultat = maillon.suivant.value
            maillon.suivant = None
            return resultat
        return None

F = File()
F.enfile(2)
F.enfile(5)
F.enfile(7)
print(F.defile())
print(F.defile())
print(F.defile())