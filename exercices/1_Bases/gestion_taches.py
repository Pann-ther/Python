import time 
import os #Permet l'execution des commandes systemes en fonction de l'OS

def affficher_menu():
    print("----- Menu ------")
    print("1. Afficher les taches")
    print("2. Ajouter une tache")
    print("3. Suprprimer une tache")
    print("4. Quitter")
    
def choix_utilisateur():
    rep = int(input("Votre choix: "))
    return rep
    
def afficher_taches(liste):
    i = 1
    for tache in liste:
        print(f"{i}: {tache}")
        i +=1
        
def ajouter_tache(liste,tache):
    liste.append(tache)
    
def supprimer_tache(liste,tache):
    liste.pop(tache-1)

#Fonction pour executer la commande en fonction de l'os  
def clear_console():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
        
# Programme de gestion des taches avec menu
def programme(liste):
    
    while True:
        affficher_menu()
        choix = choix_utilisateur()
        
        if choix == 1:
            clear_console()
            if len(liste) == 0:
                print("La liste est vide")
                afficher_taches(liste)
                time.sleep(2)
                clear_console()
            else:
                afficher_taches(liste)
                time.sleep(2)
                clear_console()
        elif choix == 2:
            clear_console()
            afficher_taches(liste)
            tache = input("Entrez la tache à ajouter: ")
            ajouter_tache(liste,tache)
            print("La tache à été ajouté")
            time.sleep(2)
            clear_console()
        elif choix == 3:
            clear_console()
            afficher_taches(liste)
            tache = int(input("Entrez la tache à supprimer: "))
            supprimer_tache(liste,tache)
            print("La tache à été supprimé")
            time.sleep(2)
            clear_console()
        elif choix == 4:
            clear_console()
            print("Vous allez quitter le programme")
            time.sleep(2)
            clear_console()
            break
        else:
            print("Entrez un nombre entre 1 à 4")
            
            
taches = []

programme(taches)
        

    
        
        
        
        