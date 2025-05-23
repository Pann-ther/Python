import employe as em
class Entreprise:

    def __init__(self):
        self.__employes = []
        self.__compteur = 0

    def afficher_menu(self):
        print("-------Gestion des employés--------")
        print("1. Ajouter un employé")
        print("2. Supprimer un employé")
        print("3. Afficher les employés")
        print("4. Quitter le gestionnaire")
        return int(input("Votre choix: "))
    
    def afficher_employes(self):
        print("------Liste des employés ")
        print("Techniciens")
        self.afficher_poste("Technicien")
        print("Managers")
        self.afficher_poste("Manager")
        
    
    def afficher_poste(self,poste):
        for employe in self.__employes:
            if employe.get_poste() == poste:
                print(employe.afficher_infos())      
                
    def id_existant(self,id):
        for employe in self.__employes:
            if employe.get_id() == id:
                return True
        return False
    
    def prenom_verifie():
        prenom = None
        while True:
            inp = input("Entrer le prenom").strip().upper()
            if not inp:
                print("Vous devez entrer un prenom")
            else:
                prenom = inp
                return prenom
            
    def nom_verifie():
        nom = None
        while True:
            inp = input("Entrer le nom").strip().upper()
            if not inp:
                print("Vous devez entrer un nom")
            else:
                nom = inp
                return nom
            
    def salaire_verifie():
        salaire = None
        while True:
            try:
                inp = int(input("Entrer le salaire"))
                if inp <=0:
                    print("Le salire doit etre superieur à 0")
                else:
                    salaire = inp
                    return salaire
            except ValueError:
                print("Le salaire doit etre un entier valide")
    
    def ajouter_technicien(self):
        prenom = self.prenom_verifie()
        nom = self.nom_verifie()
        self.__compteur += 1
        id = self.__compteur
        salaire = self.salaire_verifie()
        astreinte = None

        while True:
            astreinte = input("Le Technicien est-il d'asteinte? (o/n) ").lower()
            if astreinte == "o":
                astreinte = True
                break
            elif astreinte == "n":
                astreinte = False
                break
            else:
                print("Saisir une entrée valide")

        tech = em.Technicien(prenom,nom,id,salaire,astreinte)
        self.__employes.append(tech)
        
    def ajouter_manager(self):
        prenom = input("Entrer le prenom du manager: ").upper()
        nom = input("Entrer le nom du manager: ").upper()
        self.__compteur += 1
        id = self.__compteur
        salaire = int(input("Entrer le salaire du manager: "))
        prime = int(input("Entrez le montant de la prime: "))
        man = em.Manager(prenom,nom,id,salaire,prime)
        self.__employes.append(man)
        
    def ajouter_employe(self):
        reponse = None

        while True:
            reponse = input("L'employé est un technicien ou un manager? (t/m) ").lower()
            if reponse == "t" or reponse == "m":
                break
            else:
                print("Saisir une entrée valide")

        if reponse == "t":
            self.ajouter_technicien()
            print("Le technicien à bien été ajouté à la liste")
        elif reponse == "m":
            self.ajouter_manager()
            print("Le manager à bien été ajouté à la liste")
        else:
            print("Vous n'avez pas selctionner le bon poste")
            
    def supprimer_employe(self):
        self.afficher_employes()
        print()
        id = int(input("Entrer l'id de l'employé à supprimer"))
        trouve = False
        
        for employe in self.__employes:
            if employe.get_id() == id:
                self.__employes.remove(employe)
                print(f"{employe.get_prenom()} {employe.get_nom()} à bien été supprimé")
                trouve = True
                break
        if not trouve:
            print("L'employé n'a pas été trouvé")
    