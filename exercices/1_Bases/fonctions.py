# Demande les infotmations a l'utilisateur est lui demande son age pour le renvoyer à la fonction qui va traiter l'information
def recupertaion_identité():
    prenom = interaction_utilisateur("Entrez votre prenom : ")
    nom = interaction_utilisateur("Entrez votre nom : ")
    return int(interaction_utilisateur(f"Bonjour {prenom} {nom}, quel age as-tu? : "))

# Recupere l'age de l'utilisateur et lui affiche un message personnaliser en fonction de celui-ci
def recuperation_age():
    age = recupertaion_identité()
    if(age <= 12 ):
        print("Amuse toi bien et decouvre le monde !")
    elif(age <= 13) and (age <= 19):
        print("Crois en toi, tout commence maintenant !")
    elif(age >= 20) and (age <= 59):
        print("Continue d'avancer, tu construis ton avenir !")
    elif(age >= 60):
        print("Porfit de chaque instant, tu l'as bien mérité !")

def interaction_utilisateur(message):
    return input(message)

recuperation_age()