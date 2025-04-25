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

def saisieValeur(msg):
    return float(input(f"Entrez {msg}: "))

def addition(a,b):
    return a+b

def soustraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b