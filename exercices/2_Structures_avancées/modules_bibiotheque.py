import math
import os
import platform as pf
import datetime as dt

# Calcul la valeur de sin(x) et cos(x) pour x= pi /4
x = math.pi / 4
sin_x = math.sin(x)
cos_x = math.cos(x)

print(sin_x)
print(cos_x)

# Liste les fichiers du repertoire courant
def repertoire_courant():
    if pf.system() == "Windows":
        os.system('dir')
    else:
        os.system('ls')

repertoire_courant()

# Affiche la date et l'heure
date_du_jour = dt.datetime.now()
date_jour_form = date_du_jour.strftime("%d-%m-%Y %H:%M")
print(date_jour_form)



