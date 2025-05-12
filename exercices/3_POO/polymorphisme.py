class Vehicule:
    def __init__(self):
        pass
    def rouler():
        print("Le vehicule roule")
    
class Velo(Vehicule):
    def __init__(self):
          super().__init__()   
          
    def rouler(self):
        print("Le velo roule")
        
class Voiture(Vehicule):
    def __init__(self):
        super().__init__()
        
    def rouler(self):
        print("La voiture roule")
        
        
velo = Velo()
voiture = Voiture()

def faire_rouler(vehicule):
    vehicule.rouler()

faire_rouler(velo)
faire_rouler(voiture)