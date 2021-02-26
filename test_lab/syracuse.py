# -*- coding: utf-8 -*-
# importation de la bibliotheque math
import math
# fonction capturant des erreurs de type different
try:

# declaration de la variable nombre par l'utilisateur
    nombre = int(input('entrez un nombre entier positif: '))

# declaration du bloc d'instruction permettant d'afficher de manière itérative une suite de nombre décroissante
    for n in range(1, nombre):

        while (n) <= (math.sqrt(nombre)) ** 2 and nombre % n != 0:  # condition pour identifier un nombre impaire
            n = n + 1
        if n % nombre == 0 and nombre % 1 == 0:
            print(n, 'est un nombre premier')
        else:
            print(n, "n'est pas premier")

        if n % 2 == 0:
            print(n, 'le nombre est paire')
        else:
            print(n, 'le nombre est impaire')

    n = int(nombre)

except ValueError:
    print('veuillez saisir un entier positif')
except TypeError:
    print('veuillez saisir un entier et non des caractères')


