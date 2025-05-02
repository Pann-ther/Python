import csv

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
        print(contenu)

def ajouter_contact():
    pass

def supprimer_contact():
    pass

def modifier_contact():
    pass
