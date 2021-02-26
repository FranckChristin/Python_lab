# -*- coding : utf-8 -*-

# determination de manière aleatoire d'un mot de passe

import random
import string

def mot_de_passe(longeur):

   b= string.ascii_lowercase + string.ascii_uppercase                   # variable contenant à la fois des lettres miniscules et majuscules

# retourne aleatoirement un mot de 8 caractères composées des lettres de la variable b

   return "".join(random.choice(b) for i in range (longeur))
print("votre mot passe choisi est: ", mot_de_passe(8))

# comparaisons de 02 entiers

x = int(input('enter a number x: '))
y = float(input('enter a number y: '))
if x == y :
    print ('x and y are equal')
elif x<y :
    print('x is smaller')
else:
    print('y is smaller')