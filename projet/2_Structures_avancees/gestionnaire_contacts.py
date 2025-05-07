import csv

# Fonction d'affichage
def afficher_menu():
    print("------Menu------")
    print("1. Afficher les contacts")
    print("2. Ajouter un contact")
    print("3. Supprimer un contact")
    print("4. Modifier un contact")
    print("5. Quitter le programme")
    int(input("Votre choix: "))


def afficher_contacts():
    with open("contacts.csv","r") as fichier:
        contenu = csv.DictReader(fichier)
        for line in contenu:
            print(f"Prenom : {line["Prenom"]}, Nom: {line["Nom"]}, Telephone: {line["Telephone"]}, Email: {line["Email"]}")
            
def choix_champs():
    print("1. Prenom")
    print("2. Nom")
    print("3. Telephone")
    print("4. Mail")
    return (input("Votre choix: "))   
        
# Fonctions utilitaires
def ajouter_contact():
    prenom = input("Entrez le prenom du contact")
    nom = input("Entrez le nom du contact")
    telephone = input("Entrez le numero de telephone du contact")
    mail = input("Entrez le mail du contact")
    donnees = [prenom, nom, telephone, mail]
    
    with open("contact.csv","w", newline="") as fichier:
        ajout = csv.writer(fichier)
        ajout.writerow(donnees)

def supprimer_contact():
    prenom = input("Entrez le prenom du contact que vous souhaitez supprimer ")
    
    if not existance_utilisateur(prenom):
        with open("contacts.csv","r") as fichier:
            buffer = list(csv.reader(fichier))
            
        contact_maj = [ligne for ligne in buffer if buffer[0] != prenom]
        
        with open("contacts.csv","w") as fichier:
            ecriture = csv.writer(fichier)
            ecriture.writerows(contact_maj)
            
        print(f"{prenom} a bien ete supprime des contacts")
    else:
        print(f"{prenom} n'a pas ete trouve dans les contacts")
  
def modifier_contact():
    prenom = input("Entrez le prenom du contact que duquel vous souhaitez modifier les valeurs")
    nom = input("Entrez le nom du contact que duquel vous souhaitez modifier les valeurs")
    champs = choix_champs()
    valeur = input("Entrez la nouvelle valeur ")
    
    with open("contrats.csv","r") as fichier:
        lecteur = list(csv.reader(fichier))
        
        for line in lecteur:
            if line[0] == prenom & line[1] == nom:
                line[champs] = valeur
                print(line)
                
    with open("contacts.csv","w") as fichier:
        ecriture = csv.writer(fichier)
        ecriture.writerows(lecteur)
        
def existance_utilisateur(prenom):
    with open("contacts.csv","r") as fichier:
        lecteur = csv.reader(fichier)
        for line in lecteur:
            if line[0] == prenom:
                return True
        return False     
  
# Fonction principal  
def code_principale():
                  
    
