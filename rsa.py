from random import randint

def divisible(a,b): #Retourne True si a est divisible par b, False sinon
    return a%b==0
def coprime(a): #Retourne un entier naturel premier avec a et strictement inférieur à a
    liste_nombres_premiers = [3,5]
    for i in range(2,a):
        if not divisible(i,2) and not divisible(i,3) and not divisible(i,5) and not divisible(i,9): 
            liste_nombres_premiers.append(i)
    return liste_nombres_premiers[randint(0,len(liste_nombres_premiers)-1)]
def euclideEtendu(a,b): #Retourne v du coefficients de Bézou u et v de l'équation ax + by = PGCD(a,b)"""
    #(r1 entier naturel et u1, v1 entiers relatifs)
    r1 = b
    r2 = a
    u1 = 0
    v1 = 1
    u2 = 1
    v2 = 0
    while r2 != 0:
        q = int(r1/r2) #(division entiere)
        r3 = r1
        u3 = u1
        v3 = v1

        r1 = r2
        u1 = u2
        v1 = v2
        r2 = r3 - q*r2
        u2 = u3 - q*u2
        v2 = v3 - q*v2
    return abs(u1) 
def keysRSA(p,q):#Retourne un couple (a,b) de clés RSA
    #Choisir p et q, deux nombres premiers distincts ;
    #calculer leur produit n = pq, appelé module de chiffrement ;
    n = p*q
    print("module de chiffrement = %i"%(n))

    #calculer φ(n) = (p - 1)(q - 1) (c'est la valeur de l'indicatrice d'Euler en n) ;
    phi_n = (p-1)*(q-1)
    print("indicatrice d'Euler en n = %i"%(phi_n))

    #choisir un entier naturel e premier avec φ(n) et strictement inférieur à φ(n), appelé exposant de chiffrement ;
    e = coprime(phi_n)
    print("exposant de chiffrement = %i"%(e))

    #calculer l'entier naturel d, inverse de e modulo φ(n), et strictement inférieur à φ(n), appelé exposant de déchiffrement ; 
    #d peut se calculer efficacement par l'algorithme d'Euclide étendu.
    #au+bv = PGDC(a,b)  
    d = euclideEtendu(e,phi_n)
    print("exposant de déchiffrement = %i"%(d))

    privateKey = (n,d)
    publicKey = (n,e)

    return [publicKey,privateKey]
def codeRSA(mes,a,b): #Retourne le message chiffré par la clé publique (n,e)
    liste_charactere_chiffre=[]
    for i in range(len(mes)):
        ascii_char = ord(mes[i])
        liste_charactere_chiffre.append((ascii_char**a)%b)
    return liste_charactere_chiffre
def decodeRSA(liste_charactere_chiffre,a,b): #Retourne le message déchiffré par la clé privée (n,d)
    liste_charactere_dechiffre=[]
    for i in range(len(liste_charactere_chiffre)):
        liste_charactere_dechiffre.append(chr((liste_charactere_chiffre[i]**a)%b))
    return "".join(liste_charactere_dechiffre)
	
#génération de clés
rsa = keysRSA(227,229)
publicKey = rsa[0]
privateKey = rsa[1]
"""
print("La clé publique :",publicKey)
print("La clé privée :",privateKey)
"""
print("---------------------------------------")
#message à chiffrer
message = "Bonjour"
#print("Message :",message)

print("---------------------------------------")
#chiffrer le message
chiffreMessage = codeRSA(message,publicKey[1],publicKey[0])
print("Chiffre Message :", "".join([chr(chiffreMessage[i]) for i in range(len(chiffreMessage))]))

print("---------------------------------------")
#déchiffrer le message
dechiffreMessage = decodeRSA(chiffreMessage,privateKey[1],privateKey[0])
print("Dechiffre Message :", dechiffreMessage)
