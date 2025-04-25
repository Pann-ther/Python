import os
import time

# Fonctions d'affichage des menus
def afficher_menu_principal():
    print("--------Menu Principal--------")
    print("1. Calculatrice")
    print("2. Convertisseur d'unité")
    print("3. Quitter le programme")
    return int(input("Votre choix: "))
 
def afficher_menu_calculatrice():
    print("--------Calculatrice--------")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Retour au menu principal")
    return int(input("Choisissez l'operation: "))
    
def afficher_menu_conversion():
    print("--------Convertisseur d'unites--------")
    print("1. Kilometre en metre")
    print("2. Celsuis en Fehrenheit")
    print("3. Retour au menu principal")
    return int(input("Choisissez le type de conversion: "))

# Fonctions utilitaires
def clear_console():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def saisieValeur(msg):
    return float(input(f"{msg}: "))

# Fonctions de calculs
def addition(a,b):
    return a+b

def soustraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b == 0:
        print(f"Vous ne pouvez pas diviser {a} par {b}")
    else:
        return a/b

#Fonctions de conversion
def conversion_kilometre_metre(a):
    return a*1000

def conversion_celsuis_fehrenheit(a):
    return (a * (9/5))+32


# Fonction gestion des calculs
def calculette():
    choix = afficher_menu_calculatrice()
    
    if choix == 1:
        a = saisieValeur("Entrez la valeur 1")
        b = saisieValeur("Entrez la valeur 2")
        print(f"{a} + {b} = {addition(a,b)}")
        
    elif choix == 2:
        a = saisieValeur("Entrez la valeur 1")
        b = saisieValeur("Entrez la valeur 2")
        print(f"{a} - {b} = {soustraction(a,b)}")
        
    elif choix == 3:
        a = saisieValeur("Entrez la valeur 1")
        b = saisieValeur("Entrez la valeur 2")
        print(f"{a} * {b} = {multiplication(a,b)}")
        
    elif choix == 4:
        a = saisieValeur("Entrez la valeur 1")
        b = saisieValeur("Entrez la valeur 2")
        if b == 0:
            print(f"Vous ne pouvez pas diviser {a} par {b}")
        else:
            print(f"{a} / {b} = {division(a,b)}")
        
    elif choix == 5:
        clear_console()
        code_principal()
        
    else:
        print("Entrez un choix valide (compris entre 1 et 5)") 

# Fonction gestion des conversions        
def convertisseur():
    choix = afficher_menu_conversion()
    
    if choix == 1:
       a = saisieValeur("Entrez la valeur a convertir") 
       print(f"{a} km vaut {conversion_kilometre_metre(a)} m")
       
    elif choix == 2:
        a = saisieValeur("Entrez la valeur a convertir")
        print(f"{a} C vaut {conversion_celsuis_fehrenheit(a)} F")
        
    elif choix == 3:
        clear_console()
        code_principal()
        
    else:
        print("Entrez un choix valide (compris entre 1 et 3)")

# Fonction principal
def code_principal():
    choix = afficher_menu_principal()
    
    if choix == 1:
        clear_console()
        while True:
            calculette()
            time.sleep(2)
            clear_console()
        
    elif choix == 2:
        clear_console()
        while True:
            convertisseur()
            time.sleep(2)
            clear_console()
    
    elif choix == 3:
        clear_console()
        print("Vous allez quitter le programme")
        time.sleep(2)
        clear_console()
        exit
        
    else:
        print("Entrez un choix valide (compris entre 1 et 3)")   

# Execution
code_principal()
    
        



    
        
        
    




