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
    def __init__(self, longitude_degree, latitude_degree):
        self.latitude = latitude_degree
        self.longitude = longitude_degree

        # retourne la valeur longitude_degrees en radian
        @property
        def longitude(self):
            return self.longitude_degree * math.pi / 180
        @property
        def lalitude(self):
            return self.latitude_degree * math.pi / 180


# utiliser l'agent attributes du fichier json televersé de agents-100k.json
def main():
    for agent_attributes in json.loads(open("agents-100k.json")):
        latitude = agent_attributes.pop('latitude')
        longitude = agent_attributes.pop('longitude')
        Position = Position(longitude, latitude)
        agent = Agent(Position, **agent_attributes)
# afficher le resultat de l'attribut de la class position
        print(agent.position.longitude)
        print(agent.position.latitude)
main()

