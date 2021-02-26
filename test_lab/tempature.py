# -*- coding : utf-8 -*-
# ce programme affiche le resultat journalier de temperature d'un invidu

from random import randint

jour_client =['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
temp = randint(25, 40)

try:
    jour = input('veuillez inserer votre jour enfin de connaitre votre temperature : \n')
    assert jour in jour_client
except AssertionError:
    print('veuillez inserez un jour de la semaine valide')

# condition permettant à un cient de savoir sa temperature journalière

for j in jour_client:
    if j == jour :
        print('le jour souhaiter est : ', j, '\n la temperature obtenu ce jour est: ', temp)




