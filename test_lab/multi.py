# -*- coding: utf-8 --*-
import math

def tab(nb):

    nb = int(input('entrez un nombre positif: '))

    print("la table de multiplication de", nb, "donne: ")
    i = 0
    while i<10:
        i= i+1
        print(nb, "*", i*1, "=",nb*(i*1))



tab(4)





