# -*- coding utf-8 -*-
import random
import json
quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]
# definition la fonction json

def read_value_from_json():

	value = []

	# ouvrir le fichier json avec mon objet
	with open('characters.json') as f:

		# charger tous les données dans mon dossier
		data = json.load(f)
		for entry in data:
			value.append(entry['characters'])
			return value


characters = [
    "alvin et les Chipmunks", 
    "babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]
 
def get_random_item(my_list):
	ran_numb= []
	new_list = []
	ran_numb = random.randint(0, len(characters) - 1)
	item = my_list[ran_numb]
	for element in my_list:
		new_list.insert(5, "mowgli")                                                                                                                                                                  
		new_list[0] = "la capitale"
		print (new_list) 




def random_characters():
	all_value = read_value_from_json()
	return get_random_item(all_value)

# la fonction permettant de mettre en majuscule la premiere lettre d'une chaine de caractere en majuscule
def capitalize(words):
	for word in words:
		word.capitalize()


#definir la fonction message permettant de mettre les premières lettres de chaque chaine de carcatere des listes  en majiscules

def message(characters, quote):
	capitalize(characters)
	capitalize(quote)
	return "{} a dit : {}".format(characters, quote)


def main():
	user_answer = str(input('tapez entrée pour connaitre une autre citation ou B pour quitter le programme.'))
	while user_answer != "B":
		print(message(get_random_item(characters),get_random_item(quotes)))
		user_answer = str(input('tapez entrée pour connaitre une autre citation ou B pour quitter le programme.'))


if __name__ == "__main__":
	main()