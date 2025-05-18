import employe as em
class app:

    def __init__(self):
        self.__employes = []
        self.__compteur = 0

    def afficher_menu():
        print("-------Gestion des employés--------")
        print("1. Ajouter un employé")
        print("2. Supprimer un employé")
        print("3. Afficher les employés")
        print("4. Quitter le gestionnaire")
        return int(input("Votre choix: "))
    
    def id_existant(self,id):
        for employe in self.__employes:
            if employe.get_id() == id:
                return True
        return False
    
    def ajouter_technicien(self):
        prenom = input("Entrer le prenom du technicien: ").upper
        nom = input("Entrer le nom du technicien: ").upper
        self.__compteur += 1
        id = self.__compteur

        salaire = input("Entrer le salaire du technicien: ").strip()
        sf = salaire.replace(" ","")
        astreinte = None

        while True:
            astreinte = input("Le Technicien est-il d'asteinte? (o/n) ").lower
            if astreinte == "o":
                astreinte = True
                break
            elif astreinte == "n":
                astreinte = False
                break
            else:
                print("Saisir une entrée valide")

        tech = em.Employe(prenom,nom,id,salaire,astreinte)
        self.__employes.append(tech)

    
    def ajouter_employe(self):
        reponse = None

        while True:
            reponse = input("L'employé est un technicien ou un manageur? (t/m) ").lower
            if reponse == "t" or reponse == "m":
                break
            else:
                print("Saisir une entrée valide")

        if reponse == "t":
            self.ajouter_technicien()
        elif:
            self.ajouter_manageur()