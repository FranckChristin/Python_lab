#-*- coding: utf-8 -*-
chaine = str()
while chaine.lower() != "q":
    print("Tapez 'Q' pour quitter...")
    chaine = input()

print("Merci !")

prenom = "Paul"
nom = "Dupont"
age = 21
print("Je m'appelle {0} {1} et j'ai {2} ans.".format(prenom, nom, age))

dict = {"douala":"cmr", "toronto": "canada"}
for value in dict.values():
    print(value)
