# -*- coding utf-8 -*-
# creation d'une classe et déclaration de ses  differents objets
import json
import math

class Agent():
# attribut et instance de la classe agent
    def __init__(self, position, **agent_attribute):
        self.position = position
        for attr_name, attr_value in agent_attribute.items():
           setattr(self, attr_name, attr_value)

    def say_hello(self, first_name):
        return "bien le bonjour " + first_name + " !"


class Position:
#attribut et instance de la classe position
    def __init__(self, longitude_degree, country_name, latitude_degree):
        self.country_name = country_name
        self.longitude = longitude_degree
        self.latitude = latitude_degree

        # retourne la valeur longitude_degrees en radian
        @property
        def longitude(self):
            return self.longitude_degree * math.pi / 180
        @property
        def latitude(self):
            return self.latitude_degree * math.pi / 180


# utiliser l'agent attributes du fichier json televersé de agents-100k.json
def main():
    with open("agents-100k.json") as fp:
        agent_attribute = list(json.load(fp))
        print(agent_attribute)

    for agent_attributes in agent_attribute:
        country_name = agent_attributes.pop('country_name')
        longitude = agent_attributes.pop('longitude')
        latitude = agent_attributes.pop('latitude')

        position = Position(longitude, country_name, latitude)
        agent = Agent(position, **agent_attributes)

        # afficher le resultat de l'attribut de la class position

        print("country_name", agent.position.country_name)
        print("longitude",agent.position.longitude)
        print("latitude", agent.position.latitude)
main()

