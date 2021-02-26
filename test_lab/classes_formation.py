# -*-coding : utf-8 -*-
import io

# class parente
class pays:

    #methode(fonction) definit au sein de la class
    def population(self):
       print("De ce fait parlons un peu de sa demographie et son contexte geographique : \n")         # methode population de la class pays

class Capitale(pays):
    """
    classe déclarée
    """
    def __init__(self,nom):         # definition de la fonction constructeur permettant d'instancer des objects plus-tard
        self.nom = nom              #variable nom

    def economique(self):
        print("La capitale economique du cameroun est : \n\t", self.nom)


# appelle les differentes méthodes ou fonctions


