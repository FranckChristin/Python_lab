# -*- coding : utf-8 -*-

import math
import random

def rightTriangle(max):
    x = [ (a, b, c)
    for a in range (11)
    for b in range (11)
    for c in range (11)

    if a**2 + b**2 == c**2 and a + b + c == 24]
    print(x)

rightTriangle(24)

def f(x):

    for l in range (1):
        i = random.randint(1,11)
        j = random.randint(1,11)
        k = random.randint(1,11)
        x = (i, j, k)
        if i**2 + j**2 == k**2 and i + j + k == 24:
            return x
    return x

print (f(5))
