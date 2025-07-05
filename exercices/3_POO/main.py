import entreprise
import employe as Employe
import utilitaire as u
import time

if __name__ == "__main__":
    entreprise1 = entreprise.Entreprise()
    
    while True:
        choix = entreprise1.afficher_menu()
        
        if choix == 1:
            u.clear_console()
            entreprise1.ajouter_employe()
            time.sleep(2)
            u.clear_console()
        elif choix == 2:
            u.clear_console()
            entreprise1.supprimer_employe()
            time.sleep(2)
            u.clear_console()
        elif choix == 3:
            u.clear_console()
            entreprise1.afficher_employes()
            u.retour_menu()
            
        elif choix == 4:
            u.clear_console()
            print("Vous allez quittez le gestionnaire de personnel")
            time.sleep(2)
            u.clear_console()
            exit()
        else:
            print("Entrez une valeur comprise entree 1 à 4")
    