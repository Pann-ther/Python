# Donne  la generation de l'utilisateur sur base de son année de naissance
"""
def generation_utilisateur():
    annee_naissance = int(input("Entrez votre année de naissance: "))
    message = "Vous etes de la génération "

    if (annee_naissance < 1883) or (annee_naissance > 2025):
        print(message+"n'est pas representée")
    elif annee_naissance < 1901:
        print(message+"Perdue")
    elif annee_naissance < 1928:
        print(message+"Grandiose")
    elif annee_naissance < 1946:
        print(message+"Silencieuse")
    elif annee_naissance < 1965:
        print(message+"Boomers")
    elif annee_naissance < 1981:
        print(message+"X")
    elif annee_naissance <1997:
        print(message+"Y")
    elif annee_naissance < 2013:
        print(message+"Z")
    elif annee_naissance < 2026:
        print(message+"Alpha")


generation_utilisateur()

# Affiche les nombres d'une fourchette definis par l'utilisateur

def enumeration():
    min_fourchette = int(input("Entrez un entier pour le minimum de votre fourchette: "))
    max_fourchette = int(input("Entrez un entier pour le maximum de votre fourchette: "))

    for i in range(min_fourchette,max_fourchette+1):
        print(i)

enumeration()
"""

def affichageListe(liste,exclusion):
    for fruit in liste:
        if(fruit.lower() == exclusion.lower()):
            continue
        print(fruit)

liste=["Pommme","Fraise","Banane","Orange"]
affichageListe(liste,"banane")



