#Levé et capture d'exception si une valeur autre qu'un entier est saisie
while True:
    try:
        nb=int(input("Entrez un entier: "))
        print(f"L'entier saisie: {nb}")
        break
    except ValueError as e:
        print(f"Erreur: Vous n'avez pas entré un entier")
        
#Une fonction qui verifie si l'utilisateur est majeur pour acceder au contenu si il ne l'ai pas l'acces lui sera refusé
class AccesRefuse(Exception):
    pass

def controle_acces():
    
    while True:
        try:
            age = int(input("Entrez votre age: "))
            if age < 18:
                raise AccesRefuse("Accès refusé: vous devez etre majeur pour acceder à ce contenu")
            else:
                print("Accès autorisé")
            break
        except ValueError as e:
            print("Erreur: Vous n'avez pas entré un entier")
        
try:
    controle_acces()
except AccesRefuse as e:
    print(e)
