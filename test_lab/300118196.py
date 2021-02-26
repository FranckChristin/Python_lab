# -*- coding: utf-8 -*-

def reduce (callback, liste, valeur_initiale):
        if liste == []:
                return valeur_initiale
        else:
                return callback(liste[0], reduce(callback, liste[1:], valeur_initiale))

def addition(x,y):
        return x+y
def produit (x,y):
        return x*y
def appcarre(element, liste):
        return liste + [element **2]

print (reduce(addition, [1,2,3,4], 0))
print(reduce(produit, [1,2,3,4], 1))

#list comprehension

print ([x*2 for x in range(1,11) if x % 2 != 0])
print( ",".join(["Douala "," Ville du Cameroun"]))

joueurs = [(15,"delroth"),(0,"zozor"),(10,"vous")]
joueurs.sort()
print('\n'.join(["%s a %d points" % (joueurs,score) for score, joueur in joueurs]))


