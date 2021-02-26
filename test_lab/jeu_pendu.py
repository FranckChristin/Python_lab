import random
import sys
import os
import pickle

from donnée_pendu import *
from pendu import *

# on recupère les scores de la partie
score = recup_score()

# on recupère un nom d'utilisateur
utilisateur = nom_recup()

# si il n'a pas de score on l'ajoute
if utilisateur not in score.keys():
    score[utilisateur]= 0   # 0 pour un début

continuer_partie = 'oui'

while continuer_partie != 'non':
    print("joueur {0}: {1} point(s)".format(utilisateur,score[utilisateur]))
    mot_a_trouvee = mot_aleatoire()
    lettres_trouvees = []
    mot_trouve= recup_mt_mask(mot_a_trouvee, lettres_trouvees)
    nb_chances = nb_tentative
    while mot_a_trouvee != mot_trouve and nb_chances>0:
        print("mot à trouver {0} (encore {1} chances)".format(mot_trouve,nb_chances))
        lettre = recup_lettre()
        if lettre in lettres_trouvees: #lettre a déjà été choisie
            print("vous avez déjà choisi cette lettre.")
        elif lettre in mot_a_trouvee: # lettre dans le mot à trouver
            lettres_trouvees.append(lettre)
            print("beau travail ! ")
        else:
            nb_chances -= 1
            print("dommage, cette lettre ne se trouve pas dans le mot en question")
        mot_trouve = recup_mt_mask(mot_a_trouvee,lettres_trouvees)

    if mot_a_trouvee== mot_trouve:
        print("felicitations ! vous avez trouvé le mot {0}.".format(mot_a_trouvee))
    else:
        print("desolé ! vous avez perdu.")

# on remet à jour le score de l'utilisateur
score[utilisateur] += nb_chances
continuer_partie = input("souhaiter-vous reprendre la partie (O/N) ?")
continuer_partie = continuer_partie.lower()

# la partie est finie, on enregistre les scores
recup_score(score)

# on afiche les scores de l'utisateur

print("vous finissez la partie avec {0} points.".format(score[utilisateur]))


