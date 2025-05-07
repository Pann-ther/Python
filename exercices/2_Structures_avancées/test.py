class Voiture:
    
    def __init__(self,marque, modele, puissance):
        self.marque = marque
        self.modele = modele
        self.puissance = puissance
    
    def afficher(self):
        print(f"Marque: {self.marque}, Modele: {self.modele}, Puissance: {self.puissance} cv")
        
Voiture1 = Voiture("Audi","A1",135)
Voiture1.afficher()