etudiant = {
    "nom" : "Jog",
    "nom" : 25,
    "matieres" : ["Francais","Maths","Anglais"],
    "moyenne" : 12
}
del etudiant["matieres"]
etudiant["adresse"] = "Paris"
for cle, val in etudiant.items():
    print(f"{cle}: {val}")
    
ens1 = {1,2,3,4}
ens2 = {3,4,5,6}

union_ens = ens1 | ens2
intersection_ens = ens1 & ens2
difference_ens = ens1 ^ ens2
print(union_ens)
print(intersection_ens)
print(difference_ens)

chiffres = {1,2,3,4,5,6,7,8,9,10}
chiffres.remove(5)
print(chiffres)