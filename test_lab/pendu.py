#-*- coding : utf-8 -*-

from random import choice
import sys
import os
import pickle

from donnée_pendu import *


"""recupère les score enregistrés si le fichier existe"""

def recup_score():
    if os.path.exists(n_fichier_scores):    # fichier exite et o le recupère
        fichier_score = open(n_fichier_scores, "rb")
        mon_depickler = pickle.Unpickler(fichier_score)
        score = mon_depickler.load()
        fichier_score.close()
    else : #le fichier n'existe pas
        score = {}      # se charge dans un dictionnaire
    return score

# enregistrer les scores ou resultat des joueurs

def save_score(score):

    fichier_score =open(n_fichier_scores, "wb") # efface les anciens score
    mon_pickler = pickle.Pickler(fichier_score)
    mon_pickler.dump(score)
    fichier_score.close()

""" recuperer les noms d'utilisateur telque il doit être composé
de 4 caratères minimun, chiffres et lettres exclusivement"""

def nom_recup():
    nom = str(input("veuillez insérer votre nom afin de commencer la partie: "))
    nom = nom.capitalize()          # première lettre en majuscule
    if not nom.isalnum() or len(nom)<4:
        print("nom invalide.")
#appelez à  nouveau la fonction pour avoir un nouveau nom
        return nom_recup()
    else:
        return nom

# choisir un mot de la liste (liste_mots)

def mot_aleatoire():
    return choice(liste_mots)

""" cette fonction recupère une lettre saisie par l'utilisateur. si la chaine
récupérée n'est pas une lettre, on appelle récursivement la fonction jusqu'à
obtenir une lettre """

def recup_lettre():
    lettre = input("tapez une lettre: ")
    lettre = lettre.lower()
    if len(lettre)>1 or not lettre.isalpha():
        print("vous n'avez pas saisi une lettre valide")
        return recup_lettre()
    else :
        return recup_lettre()                           # a coriger -----------------------


"""cette fonction renvoie un mot masqué tout ou en partie, en fonction:
    -mot de depart
    -de lettres dejà trouvées(type list)
on renvoie par la suite le mot d'origine avec des * remplaçant les lettres
que l'on n'a pas encore trouvées. """

def recup_mt_mask(mot_complet,lettres_trouvees):
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque