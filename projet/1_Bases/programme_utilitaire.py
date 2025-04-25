import os
import time

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

def clear_console():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
    

def saisieValeur(msg):
    return float(input(f"{msg}: "))

def addition(a,b):
    return a+b

def soustraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

def conversion_kilometre_metre(a):
    return a*1000

def conversion_celsuis_fehrenheit(a):
    return (a * (9/5))+32

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
        print(f"{a} / {b} = {division(a,b)}")
        
    elif choix == 5:
        afficher_menu_principal()
        
    else:
        print("Entrez un choix valide (compris entre 1 et 5)") 
        
def convertisseur():
    choix = afficher_menu_conversion()
    
    if choix == 1:
       a = saisieValeur("Entrez la valeur a convertir") 
       print(f"{a} km vaut {conversion_kilometre_metre(a)} m")
       
    elif choix == 2:
        a = saisieValeur("Entrez la valeur a convertir")
        print(f"{a} C vaut {conversion_celsuis_fehrenheit(a)} F")
        
    elif choix == 3:
        afficher_menu_principal()
        
    else:
        print("Entrez un choix valide (compris entre 1 et 3)")
        



    
        
        
    




