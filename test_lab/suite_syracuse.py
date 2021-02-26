# -*- coding: utf-8 -*-

try:

    def suite_syracruse(n):

# declarons le paramètre n au quel on soummet une valeur qui va l'itérer jusqu'à ceux qu'il soit egale à 1 en fonction de sa parité
        nombre = [n]
        while nombre[-1] != 1:
            if nombre[-1] % 2 ==0:                              # pour n paire
                nombre.append(nombre[-1]/2)                     # pour n impaire
            else:
                nombre.append(nombre[-1]*3 + 1)
        return nombre


    if __name__ == '__main__':

        n= int(input('veuillez entrer un entier positif: \n'))
        assert n > 0
        print('la suite de syracruse du nombre', n, ' est : \n')
        print(suite_syracruse(n), '\n')
        print('la longeur de cette suite est :\n', len(suite_syracruse(n)))
except ValueError:
    print(" merci d'inserer un nombre entier positif ")
except AssertionError:
    print ("le nombre saisie est inferieur à 0")
