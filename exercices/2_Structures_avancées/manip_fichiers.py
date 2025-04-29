import os
import csv

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
fichier = open("test.txt", "w")
lignes = []

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

with open("test.csv","r") as fichier:
    contenu = csv.reader(fichier)
    for line in contenu:
        print(line)