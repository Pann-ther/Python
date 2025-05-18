import encapsulation

class Employe:

    def __init__(self, prenom, nom, id, salaire_base):
        self.__prenom = prenom
        self.__nom = nom
        self.__id = id
        self.__salaire_base = salaire_base

    def get_prenom(self):
        return self.__prenom
    
    def get_nom(self):
        return self.__nom
    
    def get_id(self):
        return self.__id
    
    def get_salaire_base(self):
        return self.__salaire_base
    
    def set_salaire_base(self,sb):
        self.__salaire_base = sb

    def afficher_infos(self):
        return "Prenom: "+self.__prenom+", Nom: "+self.__nom+", ID: "+str(self.__id)+", Salaire: "+str(self.__salaire_base)+"€"
    
class Manager(Employe):

    def __init__(self, prenom, nom, id, salaire_base, prime):
        super().__init__(prenom,nom,id,salaire_base)
        self.__prime =  prime
        self.__salaire_total = self.calcul_salaire_total()

    def get_prime(self):
        return self.__prime
    
    def get_salaire_total(self):
        return self.__salaire_total
    
    def set_prime(self,np):
        self.__prime = np

    def calcul_salaire_total(self):
        return self.__prime + self.get_salaire_base()

    def afficher_infos(self):
        return super().afficher_infos() + ", Prime: "+str(self.__prime)+"€, Salaire total: "+str(self.__salaire_total)+"€"
    
class Technicien(Employe):

    def __init__(self, prenom, nom, id, salaire_base,astreinte):
        super().__init__(prenom, nom, id, salaire_base)
        self.__astreinte = astreinte
        self.__salaire_total = self.calcul_salaire_total()

    def get_astreinte(self):
        return self.__astreinte
    
    def get_salaire_total(self):
        return self.__salaire_total
    
    def set_astreinte(self,a):
        self.__astreinte = a

    def calcul_salaire_total(self):
        if self.__astreinte: 
            return self.get_salaire_base() * 1.25
        else:
            return self.get_salaire_base()

    def afficher_infos(self):
        return super().afficher_infos() + ", Astreinte: "+ str(self.__astreinte)+", Salaire total: "+str(self.__salaire_total)+"€"
    

tech1 = Technicien("John","Doe", 112, 28000, True)
print(tech1.afficher_infos())

man1 = Manager("Jane","Doe",12,34000,5000)
print(man1.afficher_infos())

r1 = encapsulation.Rectangle(10,20)
r1.mesures()
