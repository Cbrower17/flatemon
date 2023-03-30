import pygame
import sqlite3
from lib.move import Move

CONN = sqlite3.connect('Pokemon.db')
CURSOR = CONN.cursor()
class MoveSet:
    all = []
    def __init__(self,move_1_id,move_2_id,move_3_id,move_4_id):
        self.move_1 = Move.all[move_1_id]
        self.move_2 =  Move.all[move_2_id]
        self.move_3 =  Move.all[move_3_id]
        self.move_4 =  Move.all[move_4_id]
        MoveSet.all.append(self)
    
# db methods
    @classmethod
    def new_from_db(cls, row):
        move_set = cls(row[1],row[2],row[3],row[4])
        move_set.id = row[0]
        return move_set
    
    @classmethod
    def get_all(cls):
        Move.get_all()
        sql = """
            SELECT *
            FROM MoveSet
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
    MoveSet.get_all()
    print(MoveSet.all)