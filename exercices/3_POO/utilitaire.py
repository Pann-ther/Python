import os

def clear_console():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear') 
        
def retour_menu():
    print("Appuyer sur la touche entrée pour continuer ")
    input()
    clear_console()