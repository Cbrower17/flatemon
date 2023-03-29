import pygame
import sqlite3

CONN = sqlite3.connect('Pokemon.db')
CURSOR = CONN.cursor()
class Move:
    all = []
    def __init__(self,name,damage,type_,max_pp):
        self.name = name
        self.damage = damage
        self.type_ = type_
        self.max_pp = max_pp
    
# db methods
    @classmethod
    def new_from_db(cls, row):
        move = cls(row[1],row[2],row[3],row[4])
        move.id = row[0]
        return move
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM move
        """

        all = CURSOR.execute(sql).fetchall()
        print(all)
        # cls.all = [cls.new_from_db(row) for row in all]
        for row in all:
            print("row inside loop:",row)
            cls.all.append(cls.new_from_db(row))
        return cls.all
    
if __name__ == "__main__":
    Move.get_all()
    print(Move.all)