# -*- coding utf-8 -*-

# le projet portera sur l'initiation à la librairie pandas
import pandas as pd

# soit les listes suivantes

nom = ["franck", "christin", "herman", "eric", "abraham", "oscar"]
math = [15, 20, 10, 14, 20, 18]
français = [14, 16, 18, 19, 10, 6]
anglais = [12, 6, 14, 15, 13, 8]

resultat = pd.DataFrame({"Nom": nom,"Math": math,"Français": français,"Anglais": anglais})
print(resultat)
