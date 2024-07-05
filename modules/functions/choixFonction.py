from modules.functions import euro, dollarUS, livre, fcfa, yuan, yen

def choixFonction(choix1, choix2, montant):
    if([choix1, choix2] == [1, 2]):
        return euro.dollar(montant)
    elif([choix1, choix2] == [1, 3]):
        return euro.livre(montant)
    elif([choix1, choix2] == [1, 4]):
        return euro.yuan(montant)
    elif([choix1, choix2] == [1, 5]):
        return euro.fcfa(montant)
    elif([choix1, choix2] == [1, 6]):
        return euro.yen(montant)
    
    if([choix1, choix2] == [2, 1]):
        return dollarUS.euro(montant)
    elif([choix1, choix2] == [2, 3]):
        return dollarUS.livre(montant)
    elif([choix1, choix2] == [2, 4]):
        return dollarUS.yuan(montant)
    elif([choix1, choix2] == [2, 5]):
        return dollarUS.fcfa(montant)
    elif([choix1, choix2] == [2, 6]):
        return dollarUS.yen(montant)
    
    if([choix1, choix2] == [3, 1]):
        return livre.euro(montant)
    elif([choix1, choix2] == [3, 2]):
        return livre.dollar(montant)
    elif([choix1, choix2] == [3, 4]):
        return livre.yuan(montant)
    elif([choix1, choix2] == [3, 5]):
        return livre.fcfa(montant)
    elif([choix1, choix2] == [3, 6]):
        return livre.yen(montant)
    
    if([choix1, choix2] == [4, 1]):
        return yuan.euro(montant)
    elif([choix1, choix2] == [4, 2]):
        return yuan.dollar(montant)
    elif([choix1, choix2] == [4, 3]):
        return yuan.livre(montant)
    elif([choix1, choix2] == [4, 5]):
        return yuan.fcfa(montant)
    elif([choix1, choix2] == [4, 6]):
        return yuan.yen(montant)
    
    if([choix1, choix2] == [5, 1]):
        return fcfa.euro(montant)
    elif([choix1, choix2] == [5, 2]):
        return fcfa.dollar(montant)
    elif([choix1, choix2] == [5, 3]):
        return fcfa.livre(montant)
    elif([choix1, choix2] == [5, 4]):
        return fcfa.yuan(montant)
    elif([choix1, choix2] == [5, 6]):
        return fcfa.yen(montant)

    if([choix1, choix2] == [6, 1]):
        return yen.euro(montant)
    elif([choix1, choix2] == [6, 2]):
        return yen.dollar(montant)
    elif([choix1, choix2] == [6, 3]):
        return yen.livre(montant)
    elif([choix1, choix2] == [6, 4]):
        return yen.yuan(montant)
    elif([choix1, choix2] == [6, 5]):
        return yen.fcfa(montant)
