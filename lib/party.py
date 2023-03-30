import pygame
import sqlite3
from lib.trainer import Trainer

CONN = sqlite3.connect('Pokemon.db')
CURSOR = CONN.cursor()

class Party:
    all = []
    def __init__(self, trainer_id):
        self.trainer = Trainer.all[trainer_id]
        self.partymember = []
        self.trainer.party.append(self)
        Party.all.append(self)

    def add_to_party(self, pokemon_id):
        pass

    # db methods
    @classmethod
    def new_from_db(cls, row):
        party = cls(row[1])
        party.id = row[0]
        return party
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM Party
        """
        all = CURSOR.execute(sql).fetchall()
        print(all)
        
        # cls.all = [cls.new_from_db(row) for row in all]
        for row in all:
            print("row inside loop:",row)
            cls.all.append(cls.new_from_db(row))
        return cls.all
    
