

import utilities
import configmonster

from monster import Monster
from lib.pokemon import Pokemon
from lib.pokedex import Pokedex

class MonsterFactory:
    def __init__(self):
        self.count = 0

    def find_pokemon(self):
        random_number = -1

        random_number = utilities.generate_random_number(1, 9)
        all_dex = Pokedex.get_all()
        name = all_dex[random_number].name
        hp = all_dex[random_number].maxhp
        
        pokemon = Pokemon(name,random_number,hp,3,1)
        pokemon.save()
        
        return pokemon

    def create_monster(self, monster_type):
        random_number = -1

        random_number = utilities.generate_random_number(1, 9)

        monster = Monster(monster_type, random_number)
        self.count = self.count + 1

        return monster