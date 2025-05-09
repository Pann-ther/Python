import csv
import time
import os
import re

# Fonction d'affichage
def afficher_menu():
    print("------Menu------")
    print("1. Afficher les contacts")
    print("2. Ajouter un contact")
    print("3. Supprimer un contact")
    print("4. Modifier un contact")
    print("5. Quitter le programme")
    return int(input("Votre choix: "))

def afficher_contacts():
    with open("contacts.csv","r") as fichier:
        contenu = csv.DictReader(fichier)
        print("--------Liste contact----------")
        for line in contenu:
            print(f"Prenom : {line['Prenom']}, Nom: {line['Nom']}, Telephone: {line['Telephone']}, Email: {line['Email']}")
              
def choix_champs():
    print("1. Prenom")
    print("2. Nom")
    print("3. Telephone")
    print("4. Mail")
    return int(input("Votre choix: "))   

def retour_menu():
    print("Appuyer sur la touche entrée pour continuer ")
    input()
    clear_console()
    code_principale()
          
# Fonctions utilitaires
def ajouter_contact():
    prenom = valider_prenom()
    nom = valider_nom()
    
    if not existance_utilisateur(prenom, nom):
        telephone = valider_telephone()
        mail = valider_email()
        donnees = [prenom, nom, telephone, mail]
        
        with open("contacts.csv","a", newline="") as fichier:
            ajout = csv.writer(fichier)
            ajout.writerow(donnees)
            print("Le contact a ete ajoute")
        
        print(f"Prenom : {prenom}, Nom: {nom}, Telephone: {telephone}, Email: {mail}")
    else:
        print("Le contact existe deja")

def supprimer_contact():
    prenom = valider_prenom()
    nom = valider_nom()
    
    if existance_utilisateur(prenom, nom):
        with open("contacts.csv","r", newline="") as fichier:
            buffer = list(csv.reader(fichier))
            
        contact_maj = [ligne for ligne in buffer if ligne[0] != prenom and ligne[1] != nom]
        
        with open("contacts.csv","w", newline="") as fichier:
            ecriture = csv.writer(fichier)
            ecriture.writerows(contact_maj)
            
        print(f"{prenom} a bien ete supprime des contacts")
    else:
        print(f"{prenom} n'a pas ete trouve dans les contacts")
  
def modifier_contact():
    prenom = valider_prenom()
    nom = valider_nom()
    
    if existance_utilisateur(prenom, nom):
        champs = choix_champs()
        if champs == 1 or champs == 2:
            valeur = input("Entrez la nouvelle valeur: ").upper().strip()
        else:
            valeur = input("Entrez la nouvelle valeur: ").strip()
        
        with open("contacts.csv","r", newline="") as fichier:
            lecteur = list(csv.reader(fichier))
            
            for line in lecteur:
                if line[0] == prenom and line[1] == nom:
                    line[champs - 1] = valeur
                    print("------Information mise a jour---------")
                    print(f"Prenom : {line[0]}, Nom: {line[1]}, Telephone: {line[2]}, Email: {line[3]}")
                    break
                    
        with open("contacts.csv","w", newline="") as fichier:
            ecriture = csv.writer(fichier)
            ecriture.writerows(lecteur)
    else:
        print("Le contact n'existe pas")
        
def clear_console():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear') 
        
# Fonction de verfication des données
def valider_prenom():
    while True:
        prenom = input("Entrez le prenom du contact: ").strip().upper()
        if not prenom:
            print("Vous devez saisir un prenom")
        else:
            return prenom
        
def valider_nom():
    while True:
        nom = input("Entrez le nom du contact: ").strip().upper()
        if not nom:
            print("Vous devez saisir un nom")
        else:
            return nom
        
def valider_telephone():
    while True:
        telephone = input("Entrez le numero de telephone du contact: ").strip()
        tel_formatee = telephone.replace(" ","")
        if not tel_formatee.isdigit() or len(tel_formatee) != 10:
            print("Entrez un numéro de telephone valide, à 10 chiffres")
        else:
            return telephone

def valider_email():
    while True:
        email = input("Entrez l'email du contact: ")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("L'email n'est pas valide. Entrez un format similaire exemple@domaine.com")
        else:
            return email
        
def existance_utilisateur(prenom, nom):
    with open("contacts.csv","r", newline="") as fichier:
        lecteur = csv.reader(fichier)
        for line in lecteur:
            if line[0] == prenom and line[1] == nom:
                return True
        return False    
        
# Fonction principal  
def code_principale():
    clear_console()
    while True:
        choix = afficher_menu()
        clear_console()
        
        if choix == 1:
            afficher_contacts()
            retour_menu()
                
        elif choix == 2:
            ajouter_contact()
            retour_menu()
            
        elif choix == 3:
            supprimer_contact()
            retour_menu()
            
        elif choix == 4:
            modifier_contact()
            retour_menu()
            
        elif choix == 5:
            print("Vous allez quittez le programme")
            time.sleep(2)
            clear_console()
            exit()
        
        else:
            print("Entrez un entier entre 1 a 5")
            time.sleep(2)
    
code_principale()