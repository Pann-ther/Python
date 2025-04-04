# Calcul du perimetre d'un rectangle
def calc_perimetre_rectangle():
    l = float(input("Entrez la longueur de votre rectangle: "))
    la = float(input("Entrez la largueur de votre rectangle: "))
    return l*2+la*2

resultat = calc_perimetre_rectangle()

print(f"Permetre du rectangle: {resultat}")


# Verifie si un nombre est compris entre 10 et 20
def verif_plage():
    nombre = int(input("Entrez un entier entre 10 et 20: "))
    if (nombre>=10) and (nombre<=20):
        print("Votre entrée est bien dans la plage")
    else:
        print("Votre entrée est hors plage")

verif_plage()

# Calcule la moyenne des notes
def calc_moyenne():
    nb_notes = int(input("Entrez le nombre de notes a calculer: "))
    somme = 0

    for i in range(nb_notes):
        somme += float(input(f"Entrez la note {i+1}: "))

    moyenne = somme/nb_notes
    return moyenne

print(f"Moyenne des notes: {calc_moyenne()}")

# Verifie si l'utilisateur est majeur ou mineur
def verif_age():
    age=int(input("Entrez votre age: "))

    if (age >= 18):
        print("Vous etes majeur")
    else:
        print("Vous etes mineur")

verif_age()