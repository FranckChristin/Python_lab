# -*- coding : utf-8 -*-

#programme qui affiche juste les multiples de 7 des 50 premiers multiples de 13


def multiple(c):
    return [i*13 for i in range(1,50) if  i % 7 == 0]
print(multiple(14))


