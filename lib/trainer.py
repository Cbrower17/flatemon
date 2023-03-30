import pygame
import sqlite3

CONN = sqlite3.connect('Pokemon.db')
CURSOR = CONN.cursor()

class Trainer:
    all = []
    def __init__(self,name):
        self.name = name
        self.party = []
        Trainer.all.append(self)

    #db methods
    def save(self):
        sql = '''
            INSERT INTO trainer (name)
            VALUES (?)
        '''
        CURSOR .execute(sql,(self.name))
        CONN.commit()
    @classmethod
    def new_from_db(cls, row):
        trainer = cls(row[1])
        trainer.id = row[0]
        return trainer
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM Trainer
        """
        all = CURSOR.execute(sql).fetchall()
        print(all)
        for row in all:
            print("row inside loop:",row)
            cls.all.append(cls.new_from_db(row))
        return cls.all
    

if __name__ == "__main__":
    Trainer.get_all()
    print(Trainer.all)
