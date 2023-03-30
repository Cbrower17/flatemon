import pygame
import sqlite3
from lib.pokedex import Pokedex
from lib.move_set import MoveSet


CONN = sqlite3.connect('Pokemon.db')
CURSOR = CONN.cursor()

class Pokemon:
    all = []
    def __init__(self, nickname, p_id, remaining_hp, trainer_id, move_set_id):
        
        if len(Pokemon.all)>0:
            self.id = Pokemon.all[-1].id +1
        else:
            self.id =1
        self.nickname = nickname
        self.pokedex_id = Pokedex.all[p_id]
        self.remaining_hp = remaining_hp
        self.trainer_id = trainer_id
        # print("movesetId in pokemon init:",move_set_id)
        # oswalk
        self.move_set_id = MoveSet.all[move_set_id]
        self.image_front = pygame.image.load("lib/pokemon/front/" + f"{p_id}" + ".png")
        self.image_back = pygame.image.load("lib/pokemon/back/" + f"{p_id}" + ".png")
        Pokemon.all.append(self)

    def get_remaining_hp(self):
        return self._remaining_hp
    def set_remaining_hp(self, hp):
        sql = '''
        UPDATE Pokemon
        SET remaining_hp = ?
        WHERE id = ?;   
        '''
        CURSOR.execute(sql, (hp,self.id))
        CONN.commit()
        self._remaining_hp = hp
    remaining_hp = property(get_remaining_hp, set_remaining_hp)

    # crud methods
    def save(self):
        sql = """
            INSERT INTO Pokemon (nickname, p_id, remaining_hp, trainer_id, move_set_id)
            VALUES (?, ?,?,?,?)
        """

        CURSOR.execute(sql, (self.nickname, self.pokedex_id.id, self.remaining_hp, self.trainer_id ,self.move_set_id.id))

        CONN.commit()
    def change_name(self,new_name):
        sql = '''
        UPDATE Pokemon
        SET nickname = ?
        WHERE id = 1;   
        '''
        CURSOR.execute(sql, (new_name))
        CONN.commit()
    # this would be better to make this a property so that it updates 
    # whenever you change the hp without having to call a function
    def change_hp(self,health):
        sql = '''
        UPDATE Pokemon
        SET remaining_hp = ?
        WHERE id = ?;   
        '''
        CURSOR.execute(sql, (health,self.id))
        CONN.commit()
    def delete_from_table(self):
        sql = '''
        DELETE FROM Pokemon WHERE id =? ;'''
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
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
        # print(all)
        
        # cls.all = [cls.new_from_db(row) for row in all]
        for row in all:
            # print("row inside loop:",row)
            cls.new_from_db(row)
        return cls.all
    
    
if __name__ == "__main__":
    MoveSet.get_all()
    Pokedex.get_all()
    Pokemon.get_all()
    
    print(Pokemon.all)