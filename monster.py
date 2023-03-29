import pygame
import sqlite3

CONN = sqlite3.connect('Pokemon.db')
CURSOR = CONN.cursor()
class Monster:
    all = []
    def __init__(self, monster_type, id):
        print("player created")
        self.type = monster_type
        self.health = 10
        self.attack = 10
        self.id = id
        self.image = pygame.image.load("lib/pokemon/front/" + f"{self.id}" + ".png")
    
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
        # cls.all = [cls.new_from_db(row) for row in all]
        for row in all:
            print("row inside loop:",row)
            cls.all.append(cls.new_from_db(row))
        return cls.all
    
if __name__ == "__main__":
    Monster.get_all()
    print(Monster.all)