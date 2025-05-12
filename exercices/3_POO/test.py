class Personne:
    def __init__(self,prenom,nom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    
    def se_presenter(self):
        print(f"Je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans")
        
personne1 = Personne("John","Doe",25)
personne2 = Personne("Jane","Doe",30)
personne3 = Personne("Char","Doe",20)
        
personne1.se_presenter()
personne2.se_presenter()
personne3.se_presenter()