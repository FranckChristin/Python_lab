#-*-coding: utf-8 -*-

#introduction à la librairie pandas

import numpy as np
import matplotlib . pyplot as plt

temps = [1 , 2, 3, 4, 6, 7, 9]
concentration = [5.5 , 7.2 , 11.8 , 13.6 , 19.1 , 21.7 , 29.4]
plt . scatter ( temps , concentration , marker ='o', color = 'red')
plt . xlabel (" Temps ( h )")
plt . ylabel (" Concentration ( mg /L )")
plt . title (" Concentration de produit en fonction du temps ")
x = np . linspace ( min ( temps ), max ( temps ), 50)
y = 2 + 3 * x
plt . plot (x , y , color ='green ', ls =" - -")
plt . grid ()
plt . savefig (' concentration_vs_temps . png ', bbox_inches ='tight ', dpi =200)
