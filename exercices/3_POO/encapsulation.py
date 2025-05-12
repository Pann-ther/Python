import os
import time
class ErreurValeur(Exception):
    pass

class Rectangle:
    def __init__(self,longueur, largueur):
        self.__longueur = None
        self.__largueur = None
        self.set_longueur(longueur)
        self.set_largueur(largueur)
        
    def get_longueur(self):
        return self.__longueur
    
    def get_largueur(self):
        return self.__largueur
    
    def set_longueur(self, l):
        if l <= 0:
            raise ErreurValeur("La longueur doit etre positive")
        else:
            self.__longueur = l
            
    def set_largueur(self,la):
        if la <= 0:
            raise ErreurValeur("La largueur doit etre positive")
        else:
            self.__largueur = la
            
    def calculer_surface(self):
        return self.__largueur* self.__longueur
    
    def mesures(self):
        print(f"Longueur: {self.__longueur}, Largueur: {self.__largueur}, Surface: {self.calculer_surface()}")
        
def clear_console():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

while True:   
    try:
        clear_console()
        long = int(input("Entrez la longueur du rectangle: "))
        larg = int(input("Entrez la largueur du rectangle: "))
        r1 = Rectangle(long,larg)
        r1.mesures()
        
        break
    except ErreurValeur as e:
        print(f"Error: {e}")
        time.sleep(2)     
