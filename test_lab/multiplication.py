# -*- coding : utf-8 -*-

"""ce programme calcule les 55 premiers nombres (exclu 0) de la table de 7 et
émet une separation lorsque celui est divisible par 3"""

import os

a, b, c = 0, 1, 0
while c<55:
    a = a+1
    a, b, c = a, a*7, c+1
    if b % 3 == 0:
        print(c, b)
        print('*')
    else:
        print(c, b)
os.system('good bye')