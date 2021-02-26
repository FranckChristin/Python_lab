import turtle

def carre(taille, couleur):
    "fonction qui dessine un carré de taille et de couleur determiné" 
    color = couleur
    c=0
    while c < 4:
        c = c+1

        turtle.right(90)
        turtle. up()
        turtle.goto(-150, 50)
    i = 0
    while i < 10:
        i = i + 1


        turtle.down()
        carre(25, 'red')
        turtle.up()
        turtle.forward(30)


        a = input()

carre(4,7)

raise ()

__doc__

