a = int(input('veuillez entrer un entier positif: '))
b = int(input('veuillez entrer un deuxième svp: '))
c = int(input('veuillez entrer un troisième svp: '))

if a<b or b<c or c>a:
    print('le minimum est:', a)
    
elif b<a or a<c or b<c:
    print ('le minimun est:', b)
else:
    b<a or c<a or c<b
    print("le minimun c'est:", c)
