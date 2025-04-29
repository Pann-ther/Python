# Crée une liste qui donne le cube des nombres du range
cube = [x*x*x for x in range(9)]
print(cube)

# Crée une liste qui extrait uniquement les nombres impairs
listes = [2, 4, 5, 8, 9, 12, 15, 20]
listes_impair = [x for x in listes if x % 2 != 0]
print(listes_impair)

# Crée une liste qui ajoute la longueur du mot 
fruits = ["apple", "banana", "cherry", "date"]
fruits_longueur = [(fruit, len(fruit)) for fruit in fruits]
print(fruits_longueur)

# Crée une liste qui extrait uniquement les mots commençant par b 
mots = ["ball", "bat", "cat", "batman", "apple"]
mots_b = [mot for mot in mots if mot[0] == "b" ]
print(mots_b)