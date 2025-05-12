class Voiture:
    
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        
    def demarrer():
        print("La voiture a demarré")
        
class VoitureElectrique(Voiture):
    
    def __init__(self, marque, modele, autonomie):
        super().__init__(marque, modele)
        self.autonomie = autonomie
        
    def demarrer(self):
        print(f"La voiture a démarré, l'autonomie est de {self.autonomie} km")
        
teslaY = VoitureElectrique("Tesla","Y",600)
teslaY.demarrer()