"""
  ______ _   _ _____ _____ __  __          
 |  ____| \ | |_   _/ ____|  \/  |   /\    
 | |__  |  \| | | || |  __| \  / |  /  \   
 |  __| | . ` | | || | |_ | |\/| | / /\ \  
 | |____| |\  |_| || |__| | |  | |/ ____ \ 
 |______|_| \_|_____\_____|_|  |_/_/    \_\
     
Some links : 

https://www.bibmath.net/crypto/index.php?action=affiche&quoi=debvingt/enigmafonc
http://mathweb.free.fr/crypto/debvingt/enigmafonc.php3     
     
"""

from random import randint
#le tableau de connexions (Plugboard) : il permet d'échanger des paires de l'alphabet, deux à deux, au moyen de fiches. (Il y a 6 fiches qui permettent donc d'échanger 12 lettres.)
# Un tableau de connections est donc une permutation (très particulière où on a échangé au plus 6 paires.) 
def getPlugboard(nb_charactere_possible):
    plugboard = []
    liste_charactere = [i for i in range(nb_charactere_possible)]
    for _ in range(len(liste_charactere)):
        plugboard.append(liste_charactere.pop(randint(0,len(liste_charactere)-1)))
    return plugboard

#Retourne un nombre au moyen du plugboard dans le sens normal
def chiffrePlugboard(i,plugboard):
    return plugboard[i]

#Retourne un nombre au moyen du plugboard dans le sens inverse
def dechiffrePlugboard(i,plugboard):
    for j in range(len(plugboard)):
        if i == plugboard[j]:
            return j          

#les rotors : un rotor est également une permutation, mais cette fois quelconque. 
#A chaque lettre en entrée correspond une autre lettre.
def getRotor(nb_charactere_possible):
    rotor = []
    liste_charactere = [i for i in range(nb_charactere_possible)]
    for i in range(nb_charactere_possible):
        rotor.append([i,liste_charactere.pop(randint(0,len(liste_charactere)-1))])
    return rotor

#Tourner le rotor d'un cran
def turnRotor(rotor,nb_charactere_possible):
    return [[(rotor[i][0]+1)%nb_charactere_possible,(rotor[i][1]+1)%nb_charactere_possible] for i in range(len(rotor))]

#Retourne un nombre au moyen du rotor dans le sens normal
def chiffreRotor(i,rotor):
    for j in range(len(rotor)):
        if i == rotor[j][0]:
            return rotor[j][1]

#Retourne un nombre au moyen du rotor dans le sens inverse
def dechiffreRotor(i,rotor):
    for j in range(len(rotor)):
        if i == rotor[j][1]:
            return rotor[j][0]

#Le réflecteur : Permutation qui permet de revenir en arrière. 
#On permute une dernière fois les lettres 2 par 2, et on les fait retraverser les rotors, et le tableau de connexion.
def getReflecteur(nb_charactere_possible):
    reflecteur = []
    liste_charactere = [i for i in range(nb_charactere_possible)]
    while len(liste_charactere)>1:
        reflecteur.append([liste_charactere.pop(randint(0,len(liste_charactere)-1)),liste_charactere.pop(randint(0,len(liste_charactere)-1))])
    return reflecteur

#Retourne un nombre au moyen du reflecteur
def chiffreReflecteur(i,reflecteur):
    for j in range(len(reflecteur)):
        if i == reflecteur[j][0]:
            return reflecteur[j][1]
        elif i == reflecteur[j][1]:
            return reflecteur[j][0]

#Simulateur Enigma
def enigma(number,lstRotors,plugboard,reflecteur,alphabet):    
    nombre_charactere_possible = len(alphabet)
    #doit être un nombre pair 
    assert nombre_charactere_possible%2 == 0

    #On applique le tableau de connnexion 
    charCoded = chiffrePlugboard(number,plugboard)
    #print("Tableau de connexions  :",charCoded,"aka",alphabet[charCoded])

    #Premier passage dans les rotors
    for rotor in lstRotors:
        charCoded = chiffreRotor(charCoded,rotor)
        #print("Premier passage rotor :",charCoded,"aka",alphabet[charCoded])

    #On applique le reflecteur
    charCoded = chiffreReflecteur(charCoded,reflecteur)
    #print("Reflecteur :",charCoded,"aka",alphabet[charCoded])

    #Deuxième passage dans les rotors mais en sens inverse
    for rotor in reversed(lstRotors):
        charCoded = dechiffreRotor(charCoded,rotor)
        #print("Deuxième passage rotor :",charCoded,"aka",alphabet[charCoded])

    #On applique le tableau de connexion en sens inverse
    charCoded = dechiffrePlugboard(charCoded,plugboard)
    #print("Tableau de connexions  :",charCoded,"aka",alphabet[charCoded])

    return charCoded

#Chiffre une chaine de caractère avec la fonction enigma 
def encodeEnigma(message,lstRotors,plugboard,reflecteur,alphabet):
    chiffreMessage = ""
    i=0 #nombre de charactere codé (à i=len(alphabet) on change de rotor)
    rotor_a_tourner = 0 #le rotor qu'on fait tourner
    
    for letter in message:
        #Convertit le charactere en nombre
        chiffreLetter = alphabet.index(letter)
        #Applique le chiffrement Enigma
        chiffreLetter = enigma(chiffreLetter,lstRotors,plugboard,reflecteur,alphabet)
        chiffreMessage+=alphabet[chiffreLetter]

        #On met à jour le prochain rotor à tourner et tourne le rotor 
        if rotor_a_tourner>len(lstRotors)-1:
            rotor_a_tourner = (rotor_a_tourner+1)%len(lstRotors)
        turnRotor(lstRotors[rotor_a_tourner],len(alphabet))
        i+=1

    return chiffreMessage

#alphabet des charactères possibles
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,;:!?.\\/'()[]{}+-_=*&^%$#@~`<>\" 1234567890"
nb_charactere_possible = len(alphabet)

plugboard = getPlugboard(nb_charactere_possible) 
lstRotors = [getRotor(nb_charactere_possible),getRotor(nb_charactere_possible)]
reflecteur = getReflecteur(nb_charactere_possible)

message = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

#encode le message
chiffreMessage = encodeEnigma(message,lstRotors,plugboard,reflecteur,alphabet)
print("Message chiffré :",chiffreMessage)

#decode le message 
dechiffreMessage = encodeEnigma(chiffreMessage,lstRotors,plugboard,reflecteur,alphabet)
print("Message déchiffré :",dechiffreMessage)
