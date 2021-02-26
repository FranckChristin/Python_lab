# -*- coding : utf-8 -*-

import io
import sys
import os
import classes_formation

"""
lecture d'un fichier en python : 
"""
try:                                    # bloc de gestion des erreurs

    ep = classes_formation.Capitale("Douala")
    ep.economique()
    ep.population()
    def open_file():
        with open("info.txt") as f:     # appel et ouverture du fichier dans un bloc
            read_data = f.read()        # lecture du fichier
        return read_data          # affichage du resultat



except IOError as err:                           # bloc de gestion des exeptions
    print("error !", err)


# 2eme fichier de type json
with open("characters.json") as f:  # appel et ouverture du fichier dans un bloc
    read_data = f.read()
print(read_data)
