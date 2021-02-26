# -*- coding utf-8 -*-
# importation de la bibliotheque mathematique
def triangle():

    import math
    print('bonjour et bienvenue\n\t')
    try:
        a = int(input('entrer une valeur: '))
        b = int(input('veuillez entrer un second nombre: '))
        c = int(input('veuillez entrer un troisième: '))
        print('soit les longueurs', a, b, c, "d'un triangle ")
    except ValueError:
        print('erreur! veuillez entrer une valeur entière\n')
    except UnboundLocalError:
        print('desolé')

    try:
        if a!=0:
            print('good! ')
        elif b!=0:
            print ('verifions le suivant\n')
        elif c!=0:
            print ('les cotés a,b,c forment un triangle\n')
        else:
            print("je m'excuse!")
        raise TypeError('desolé impossible de continuer\n')
    except ValueError:
        print('il doit être different de 0')


    if (a**2) + (b**2)== (c**2):
            print('le triangle de côtés', a,b,c, 'est: un triangle rectangle\n')
    elif a==b!=c:
                print('le triangle de côtés', a,b,c, 'est: un triangle isocèle\n')
    elif a==b==c:
            print('le triangle de côtés', a,b,c, 'est: un triangle équilateral\n')
    elif a!=b!=c:\
                print('le triangle de côtés', a,b,c, 'est: un triangle quelconque\n')
    else:
            print('bonne journée!')

print('merci pour votre attention\n\t')


triangle()