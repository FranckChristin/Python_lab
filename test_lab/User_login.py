# -*- coding : utf-8 -*-
"""
ecrit par : franck nguekam
exemple de code python qui entre un user et definit aleatoirement
son login et son mot de passe
"""
from random import randint
import sys
import random
import string

try:
    # fonction qui defini un mot de passe aleatoire
    def get_password_length(length=8):
        letters = string.ascii_letters
        nb = string.digits
        Hexdigit = string.hexdigits
        # convert deux from string to list and shuffle
        imp = f'{letters}{nb}{Hexdigit}'
        imp = list(imp)
        random.shuffle(imp)
        #generate random password and convert to string
        random_password = random.choices(imp, k=length)
        random_password =''.join(random_password)
        return random_password

    p=0
    n=int(input("enter a number: "))
    while p<n:
        name=input("enter your name: ")
        login = randint(1000, 3000)
        password = get_password_length()     # appel de la fonction
        if name == 'your name':
            break
        print(name, "your login is ", login, "and your password is ", password)
        p=p+1

    # script de fin
    while True:
        print("please enter exit to exit")
        response=input()
        if response=="exit":
            sys.exit()
        print("you typed", response,'.')
except ValueError:
    print("please, enter a string")
