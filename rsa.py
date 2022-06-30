from random import randint, randrange

def isPrime(n:int): #Test de primalité
    assert n>=0
    if n%2==0:
        return (False,2)
    p=3
    while p**2<=n:
        if n%p==0:
            #Trouvé le plus petit diviseur propre de n
            return (False,p)
        p+=2
    return True

def genPrimeNumber(a:int,b:int):
    if a>b:
        return genPrimeNumber(b,a)
    cnt=0
    go = True
    while go : 
        cnt+=1
        n = randint(a,b)
        if isPrime(n)==True:
            go=False
    return n

def mod_inverse(x,m):
    for n in range(m):
        if (x * n) % m == 1:
            return n
        elif n == m - 1:
            return "Null"
        else:
            continue

def pgcd(a:int,b:int): #Retourne le PGCD de a et b
    while b != 0:
        a,b = b,a%b
    return a
def keysRSA(a:int,b:int):#Retourne un couple (a,b) de clés RSA
    #Choisir p et q, deux nombres premiers distincts ;
    p,q = genPrimeNumber(a,b),genPrimeNumber(a,b)
    assert isPrime(p) and isPrime(q)

    #calculer leur produit n = pq, appelé module de chiffrement ;
    n = p*q
    print("module de chiffrement = %i"%(n))
    #calculer φ(n) = (p - 1)(q - 1) (c'est la valeur de l'indicatrice d'Euler en n) ;
    phi_n = (p-1)*(q-1)
    print("indicatrice d'Euler en n = %i"%(phi_n))
 
    #choisir un entier naturel e premier avec φ(n) et strictement inférieur à φ(n), appelé exposant de chiffrement ;
    e = randrange(2, phi_n)    
    g = pgcd(e, phi_n)
    while g != 1:
        e = randrange(1, phi_n)
        g = pgcd(e, phi_n)
    assert pgcd(e,phi_n)==1

    print("exposant de chiffrement = %i"%(e))
 
    #calculer l'entier naturel d, inverse de e modulo φ(n), et strictement inférieur à φ(n), appelé exposant de déchiffrement ; 
    #d peut se calculer efficacement par l'algorithme d'Euclide étendu.
    #au+bv = PGDC(a,b)  
    d =abs(mod_inverse(e,phi_n))
    print((d*e)%phi_n)
    print("exposant de déchiffrement = %i"%(d))

    publicKey = (n,e)
    privateKey = (n,d)

    return [publicKey,privateKey]

def codeRSA(mes,n,e): #Retourne le message chiffré par la clé publique (n,e)
    chiffreMes=[]
    for i in range(len(mes)):
        ascii_char = ord(mes[i])
        chiffreMes.append((ascii_char**e)%n)
    return chiffreMes
def decodeRSA(mes,n,d): #Retourne le message déchiffré par la clé privée (n,d)
    dechiffreMes=[]
    for i in range(len(mes)):
        dechiffreAscii = (mes[i]**d)%n
        dechiffreMes.append(chr(dechiffreAscii))
    return "".join(dechiffreMes)

for i in range(4):
    print("---------------------------------------")
    #génération de clés
    rsa = keysRSA(200,300)
    publicKey = rsa[0]
    privateKey = rsa[1]
    
    print("---------------------------------------")
    print("La clé publique :",publicKey)
    print("La clé privée :",privateKey)
    

    print("---------------------------------------")
    #message à chiffrer
    message = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    print("Message :",message)
    
    print("---------------------------------------")
    #chiffrer le message
    chiffreMessage = codeRSA(message,publicKey[0],publicKey[1])
    print("Chiffre Message :", chiffreMessage)

    print("---------------------------------------")
    #déchiffrer le message
    dechiffreMessage = decodeRSA(chiffreMessage,privateKey[0],privateKey[1])
    print("Dechiffre Message :", dechiffreMessage)
    assert dechiffreMessage==message
