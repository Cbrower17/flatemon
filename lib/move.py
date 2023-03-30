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
        Move.all.append(self)
    
# db methods

    def save(self):
        sql = """
            INSERT INTO Move (move_name, damage, move_type, max_pp)
            VALUES (?, ?,?,?)
        """

        CURSOR.execute(sql, (self.name, self.damage, self.type_, self.max_pp))

        CONN.commit()

        # self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]


    @classmethod
    def add_to_moves(cls,row):
        # getting elements from list all of them 
        move = cls(row[0],row[1],row[2],row[3])
        move.save()
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
        # print(all)
        # cls.all = [cls.new_from_db(row) for row in all]
        for row in all:
            # print("row inside loop:",row)
            cls.all.append(cls.new_from_db(row))
        return cls.all
    
if __name__ == "__main__":
    Move.get_all()
    print(Move.all)

    all_gen_1_moves = [['Constrict',10,'NORMAL',35],
        ['Barrage',15,'NORMAL',20],
        ['Bind',15,'NORMAL',20],
        ['Double Slap',15,'NORMAL',10],
        ['Fury Attack',15,'NORMAL',20],
        ['Poison Sting',15,'POISON',35],
        ['Wrap',15,'NORMAL',20],
        ['Comet Punch',18,'NORMAL',15],
        ['Fury Swipes',18,'NORMAL',15],
        ['Absorb',20,'GRASS',25],
        ['Rage',20,'NORMAL',20],
        ['Spike Cannon',20,'NORMAL',15],
        ['Pin Missile',25,'BUG',20],
        ['Twineedle',25,'BUG',20],
        ['Double Kick',30,'FIGHTING',30],
        ['Lick',30,'GHOST',30],
        ['Smog',30,'POISON',20],
        ['Clamp',35,'WATER',15],
        ['Fire Spin',35,'FIRE',15],
        ['Peck',35,'FLYING',35],
        ['Acid',40,'POISON',30],
        ['Bubble',40,'WATER',30],
        ['Ember',40,'FIRE',25],
        ['Gust',40,'FLYING',35],
        ['Mega Drain',40,'GRASS',15],
        ['Pay Day',40,'NORMAL',20],
        ['Pound',40,'NORMAL',35],
        ['Quick Attack',40,'NORMAL',30],
        ['Scratch',40,'NORMAL',35],
        ['Tackle',40,'NORMAL',35],
        ['Thunder Shock',40,'ELECTRIC',30],
        ['Water Gun',40,'WATER',25],
        ['Vine Whip',45,'GRASS',25],
        ['Bonemerang',50,'GROUND',10],
        ['Confusion',50,'PSYCHIC',25],
        ['Cut',50,'NORMAL',30],
        ['Karate Chop',50,'FIGHTING',25],
        ['Rock Throw',50,'ROCK',15],
        ['Struggle',50,'NORMAL',100],
        ['Razor Leaf',55,'GRASS',25],
        ['Vise Grip',55,'NORMAL',30],
        ['Bite',60,'DARK',25],
        ['Rolling Kick',60,'FIGHTING',15],
        ['Swift',60,'NORMAL',20],
        ['Wing Attack',60,'FLYING',35],
        ['Aurora Beam',65,'ICE',20],
        ['Bone Club',65,'GROUND',20],
        ['Bubble Beam',65,'WATER',20],
        ['Horn Attack',65,'NORMAL',25],
        ['Psybeam',65,'PSYCHIC',20],
        ['Sludge',65,'POISON',20],
        ['Stomp',65,'NORMAL',20],
        ['Dizzy Punch',70,'NORMAL',10],
        ['Headbutt',70,'NORMAL',15],
        ['Slash',70,'NORMAL',20],
        ['Fire Punch',75,'FIRE',15],
        ['Ice Punch',75,'ICE',15],
        ['Rock Slide',75,'ROCK',10],
        ['Thunder Punch',75,'ELECTRIC',15],
        ['Dig',80,'GROUND',10],
        ['Drill Peck',80,'FLYING',20],
        ['Hyper Fang',80,'NORMAL',15],
        ['Leech Life',80,'BUG',10],
        ['Mega Punch',80,'NORMAL',20],
        ['Razor Wind',80,'NORMAL',10],
        ['Slam',80,'NORMAL',20],
        ['Strength',80,'NORMAL',15],
        ['Submission',80,'FIGHTING',20],
        ['Tri Attack',80,'NORMAL',10],
        ['Waterfall',80,'WATER',15],
        ['Body Slam',85,'NORMAL',15],
        ['Flamethrower',90,'FIRE',15],
        ['Fly',90,'FLYING',15],
        ['Ice Beam',90,'ICE',10],
        ['Psychic',90,'PSYCHIC',10],
        ['Surf',90,'WATER',15],
        ['Take Down',90,'NORMAL',20],
        ['Thunderbolt',90,'ELECTRIC',15],
        ['Crabhammer',100,'WATER',10],
        ['Dream Eater',100,'PSYCHIC',15],
        ['Earthquake',100,'GROUND',10],
        ['Egg Bomb',100,'NORMAL',10],
        ['Jump Kick',100,'FIGHTING',10],
        ['Blizzard',110,'ICE',5],
        ['Fire Blast',110,'FIRE',5],
        ['Hydro Pump',110,'WATER',5],
        ['Thunder',110,'ELECTRIC',10],
        ['Double-Edge',120,'NORMAL',15],
        ['Mega Kick',120,'NORMAL',5],
        ['Petal Dance',120,'GRASS',10],
        ['Solar Beam',120,'GRASS',10],
        ['Thrash',120,'NORMAL',10],
        ['High Jump Kick',130,'FIGHTING',10],
        ['Skull Bash',130,'NORMAL',10],
        ['Sky Attack',140,'FLYING',5],
        ['Hyper Beam',150,'NORMAL',5],
        ['Self-Destruct',200,'NORMAL',5],
        ['Explosion',250,'NORMAL',5],]
    
    # for move in all_gen_1_moves:
    #     Move.add_to_moves(move)

