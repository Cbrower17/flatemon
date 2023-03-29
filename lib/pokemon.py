import pygame
import sqlite3
from lib.pokedex import Pokedex

CONN = sqlite3.connect('Pokemon.db')
CURSOR = CONN.cursor()
class Pokemon:
    all = []
    def __init__(self, nickname, pokedex_id, remaining_hp, trainer_id, move_set_id):
        self.nickname = nickname
        self.pokedex_id = Pokedex.all[pokedex_id]
        self.remaining_hp = remaining_hp
        self.trainer_id = trainer_id
        self.move_set_id = move_set_id
        self.image = pygame.image.load("lib/pokemon/front/" + f"{pokedex_id}" + ".png")
    
# db methods
    @classmethod
    def new_from_db(cls, row):
        pokemon = cls(row[1],row[2],row[3],row[4],row[5])
        pokemon.id = row[0]
        return pokemon
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM Pokemon
        """

        all = CURSOR.execute(sql).fetchall()
        print(all)
        return all
        # cls.all = [cls.new_from_db(row) for row in all]
        for row in all:
            print("row inside loop:",row)
            cls.all.append(cls.new_from_db(row))
        return cls.all
    
if __name__ == "__main__":
    Pokemon.get_all()
    print(Pokemon.all)