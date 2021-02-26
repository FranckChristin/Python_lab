import sqlite3

n=sqlite3.connect('world.sqlite') #connecter a la base de donnee // ######
con=n.cursor()
"""
con.executescript('''

DROP TABLE IF EXISTS etudiant ;##

CREATE TABLE etudiant(
id_etudiant integer NOT NULL PRIMARY KEY AUTOINCREMENT ,
name TEXT 

);

''')
"""#execute plusierus script en meme temsps
while True:
    etudiants=dict()
    con.execute(' SELECT * FROM etudiant')
    ets=con.fetchall()
    print("ETUDIANTS PRESENTEMENTS DANS LA BASE",ets)


    name=input("VEUILLEZ Entrez Votre Nom:\n") #entre les données 
    con.execute(''' INSERT OR IGNORE INTO etudiant (name) VALUES(?)''',(name,)) # execute

    n.commit()
    print("ETUDIANT",name,"A ETE Enregistre")
    

