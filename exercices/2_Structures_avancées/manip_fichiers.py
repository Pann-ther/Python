import os
import csv

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
fichier = open("test.txt", "w")
lignes = []

"""
while True:
    nom = input("Nom: ")
    prenom = input("Prenom: ")
    age = input("Age: ")
    lignes = [f"Nom: {nom}\nPrenom: {prenom}\nAge: {age}"]
    clear_console()
    break

fichier.writelines(lignes)
fichier.close()
fichier = open("test.txt", "r")
print(fichier.read())
nouvelle_ligne = ["John","Donneese","jdoe","P@ssw0rd","IT"]
nouvelle_ligne_2 = ["Jane","Doe","jadoe","P@ssw0rd","RH"]
nouvelles_lignes = [nouvelle_ligne, nouvelle_ligne_2]

with open("test.csv", "a+", newline="") as fichier:
    ajout_fichier = csv.writer(fichier)
    ajout_fichier.writerows(nouvelles_lignes)
    fichier.seek(0)
    print(fichier.read())
    
with open("test.csv","r") as fichier:
    contenu = csv.reader(fichier)
    for line in contenu:
        print(line)
        
with open("test.csv", "a+", newline="") as fichier:
    ajout_fichier = csv.writer(fichier)
    ajout_fichier.writerows(nouvelles_lignes)
    fichier.seek(0)
    print(fichier.read())
nouvelle_ligne = ["John","Doe","jdoe","P@ssw0rd","IT"]
nouvelle_ligne_2 = ["Jane","Doe","jadoe","P@ssw0rd","RH"]
nouvelles_lignes = [nouvelle_ligne, nouvelle_ligne_2]

nom = ["Prenom","Nom","Login","Password","Service"]
donnees = [
    {"Nom": "Jane", "Prenom":"Doe", "Login":"jdoe", "Password":"P@ssw0rd", "Service":"RH"}
]


with open("test2.csv","a+",newline="") as fichier:
    contenu = csv.DictWriter(fichier, fieldnames=nom)
    contenu.writerows(donnees)
    fichier.seek(0)
    print(fichier.read())
    
# Ajout d'un eleve au fichier csv et lecture
nouvel_eleve = ["Heloise",21,19]
with open("notesEleves.csv", "a", newline="") as fichier:
    ajout = csv.writer(fichier)
    ajout.writerow(nouvel_eleve)
    
with open("notesEleves.csv","r") as fichier:
    contenu = csv.reader(fichier)
    for line in contenu:
        print(line)
 # Affichage des informations specifiques d'un éléve
with open("notesEleves.csv","r") as fichier:
    contenu = csv.DictReader(fichier)
    for ligne in contenu:
        if ligne["Nom"]=="Vero":
            print(ligne)
            
# Lecture du fichier csv ligne par ligne
with open("test.csv", "r", newline='') as fichier:
    contenu = csv.reader(fichier)
    for ligne in contenu:
        print(ligne)  

"""
   

            
# Modification de l'age d'un éléve
with open("notesEleves.csv", "r") as fichier:
    contenu = list(csv.reader(fichier))
    
    for ligne in contenu:
        if ligne[0] == "Heloise":
            ligne[1] = "18"
        print(ligne)
                   
with open ("notesEleves.csv","w", newline="") as fichier:
    ecriture = csv.writer(fichier)
    ecriture.writerows(contenu)

    
    
        
    

    