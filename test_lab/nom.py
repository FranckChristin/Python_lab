 # -*- coding: utf-8 -*-
 #creation de la fonction
def create_message(character: str, quote:str):
    sentence = "{} a dit :{}".format(character, quote)
    print(sentence)
#excution de la fonction
create_message(character="Wilson Churchill", quote= "la premiere merveille au monde est ta perseverance.")

