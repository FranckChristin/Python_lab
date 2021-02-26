try:
    i = 0
    while i<=20:
        number = int(input("entrez un nombre superieur a 20: "))
        i = int(number)
        print('le nombre obtenue est',i)
except ValueError:
    print("veuillez recommencer et entez un nombre entier: ")
