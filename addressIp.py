from copy import deepcopy
from operator import concat


class AdresseIP:
    def __init__(s, adresse,reseau):
        s.adresse = adresse
        s.reseau = reseau

    def liste_octet(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")]
    def liste_octet_machine(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        return self.liste_octet()[self.reseau:]

    def est_reservee(s):
        """renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        return s.liste_octet()[s.reseau:] in (["255" for _ in range(s.machine)], ["0" for _ in range(s.machine)])

    def adresse_suivante(s):
        """renvoie un objet de AdresseIP avec l'adresse
        IP qui suit l’adresse self
        si elle existe et False sinon"""
        machine = s.liste_octet_machine()
        for i in range(len(machine)-1,-1,-1):
            if machine[i] <= 254:
                machine[i] += 1
                newAIP = ""
                for k in s.liste_octet()[:s.reseau]:
                    newAIP+=str(k)+"."
                for k in machine:
                    newAIP+=str(k)+"."
                newAIP = newAIP[:-1]
                return AdresseIP(newAIP,len(machine))
            machine[i]=0
        return False

    def lstAreInt(s,lstOctet):
        for i in range(len(lstOctet)):
            for k in range(len(lstOctet[i])):
               if "0"<lstOctet[i][k]>"9":
                   return False
        return True

    def est_conforme(s):
        lstOctets = s.liste_octet()
        aipIsInt = s.lstAreInt(lstOctets)
        if aipIsInt:
            octetIsOK = all(int(x) <= 255 and int(x)>=0 for x in lstOctets)
            pointIsOK = s.adresse.count(".")==3  
            return octetIsOK and pointIsOK
        return aipIsInt 

aip = AdresseIP("192.168.0.1",2)
aip2 = AdresseIP("192.168.0.2",2)
aip3 = AdresseIP("192.168.255.255",1)
suiv = aip3.adresse_suivante()
if type(suiv)!= bool:
    print(suiv.adresse)