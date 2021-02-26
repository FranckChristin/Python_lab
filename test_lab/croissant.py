# -*- coding : utf-8 -*-

import math


def search_small(arr):

    petite_valeur = arr[0]
    petit_index = 0

    for i in range(len(arr)):
        if arr[i] < petite_valeur:
            petite_valeur = arr[i]
            petit_index = i

    return (petit_index)

def selectionsort(arr):
    newarr = []

    for i in range(len(arr)):
        petite_valeur = search_small(arr)
        newarr.append(arr.pop(petite_valeur))

    return(newarr)

print(input(selectionsort([2,45,0,5,4,87])))