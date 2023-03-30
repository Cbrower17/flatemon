import pygame
import sqlite3

CONN = sqlite3.connect('Pokemon.db')
CURSOR = CONN.cursor()
class Pokedex:
    all = []
    def __init__(self, name, maxhp,attack,defence,speed,type_):
        self.name = name
        self.maxhp = maxhp
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.type = type_
        Pokedex.all.append(self)
    
    def save(self):
        sql = """
            INSERT INTO Pokedex (name, maxhp, attack, defence, speed, type)
            VALUES (?, ?,?,?,?,?)
        """

        CURSOR.execute(sql, (self.name, self.maxhp, self.attack, self.defence, self.speed,self.type))

        CONN.commit()

        # self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]


    @classmethod
    def add_to_pokedex(cls,row):
        # getting elements from list all of them 
        pokedex_entry = cls(row[0],row[1],row[2],row[3],row[4],row[5])
        pokedex_entry.save()

    
# db methods
    @classmethod
    def new_from_db(cls, row):
        pokedex_entry = cls(row[1],row[2],row[3],row[4],row[5],row[6])
        pokedex_entry.id = row[0]
        return pokedex_entry
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM Pokedex
        """

        all = CURSOR.execute(sql).fetchall()
        print(all)
        # cls.all = [cls.new_from_db(row) for row in all]
        for row in all:
            # print("row inside loop:",row)
            cls.all.append(cls.new_from_db(row))
        return cls.all
    
if __name__ == "__main__":
    Pokedex.get_all()
    print(Pokedex.all)
    
    # all_of_them = [
    # ['Caterpie',45,30,35,45,'Bug'],
    # ['Metapod',50,20,55,30,'Bug'],
    # ['Butterfree',60,45,50,70,'Bug'],
    # ['Weedle',40,35,30,50,'Bug'],
    # ['Kakuna',45,25,50,35,'Bug'],
    # ['Beedrill',65,80,40,75,'Bug'],
    # ['Pidgey',40,45,40,56,'Normal'],
    # ['Pidgeotto',63,60,55,71,'Normal'],
    # ['Pidgeot',83,80,75,91,'Normal'],
    # ['Rattata',30,56,35,72,'Normal'],
    # ['Raticate',55,81,60,97,'Normal'],
    # ['Spearow',40,60,30,70,'Normal'],
    # ['Fearow',65,90,65,100,'Normal'],
    # ['Ekans',30,60,44,55,'Poison'],
    # ['Arbok',60,85,69,80,'Poison'],
    # ['Pikachu',35,55,30,90,'Electric'],
    # ['Raichu',60,90,55,100,'Electric'],
    # ['Sandshrew',50,75,85,40,'Ground'],
    # ['Sandslash',75,100,110,65,'Ground'],
    # ['Nidoran ♀',55,47,52,41,'Poison'],
    # ['Nidorina',70,62,67,56,'Poison'],
    # ['Nidoqueen',90,82,87,76,'Poison'],
    # ['Nidoran ♂',46,57,40,50,'Poison'],
    # ['Nidorino',61,72,57,65,'Poison'],
    # ['Nidoking',81,92,77,85,'Poison'],
    # ['Clefairy',70,45,48,35,'Normal'],
    # ['Clefable',95,70,73,60,'Normal'],
    # ['Vulpix',38,41,40,65,'Fire'],
    # ['Ninetales',73,76,75,100,'Fire'],
    # ['Jigglypuff',115,45,20,20,'Normal'],
    # ['Wigglytuff',140,70,45,45,'Normal'],
    # ['Zubat',40,45,35,55,'Poison'],
    # ['Golbat',75,80,70,90,'Poison'],
    # ['Oddish',45,50,55,30,'Grass'],
    # ['Gloom',60,65,70,40,'Grass'],
    # ['Vileplume',75,80,85,50,'Grass'],
    # ['Paras',35,70,55,25,'Bug'],
    # ['Parasect',60,95,80,30,'Bug'],
    # ['Venonat',60,55,50,45,'Bug'],
    # ['Venomoth',70,65,60,90,'Bug'],
    # ['Diglett',10,55,25,95,'Ground'],
    # ['Dugtrio',35,80,50,120,'Ground'],
    # ['Meowth',40,45,35,90,'Normal'],
    # ['Persian',65,70,60,115,'Normal'],
    # ['Psyduck',50,52,48,55,'Water'],
    # ['Golduck',80,82,78,85,'Water'],
    # ['Mankey',40,80,35,70,'Fighting'],
    # ['Primeape',65,105,60,95,'Fighting'],
    # ['Growlithe',55,70,45,60,'Fire'],
    # ['Arcanine',90,110,80,95,'Fire'],
    # ['Poliwag',40,50,40,90,'Water'],
    # ['Poliwhirl',65,65,65,90,'Water'],
    # ['Poliwrath',90,85,95,70,'Water'],
    # ['Abra',25,20,15,90,'Psychic'],
    # ['Kadabra',40,35,30,105,'Psychic'],
    # ['Alakazam',55,50,45,120,'Psychic'],
    # ['Machop',70,80,50,35,'Fighting'],
    # ['Machoke',80,100,70,45,'Fighting'],
    # ['Machamp',90,130,80,55,'Fighting'],
    # ['Bellsprout',50,75,35,40,'Grass'],
    # ['Weepinbell',65,90,50,55,'Grass'],
    # ['Victreebel',80,105,65,70,'Grass'],
    # ['Tentacool',40,40,35,70,'Water'],
    # ['Tentacruel',80,70,65,100,'Water'],
    # ['Geodude',40,80,100,20,'Rock'],
    # ['Graveler',55,95,115,35,'Rock'],
    # ['Golem',80,110,130,45,'Rock'],
    # ['Ponyta',50,85,55,90,'Fire'],
    # ['Rapidash',65,100,70,105,'Fire'],
    # ['Slowpoke',90,65,65,15,'Water'],
    # ['Slowbro',95,75,110,30,'Water'],
    # ['Magnemite',25,35,70,45,'Electric'],
    # ['Magneton',50,60,95,70,'Electric'],
    # ['Farfetch\'d',52,65,55,60,'Normal'],
    # ['Doduo',35,85,45,75,'Normal'],
    # ['Dodrio',60,110,70,100,'Normal'],
    # ['Seel',65,45,55,45,'Water'],
    # ['Dewgong',90,70,80,70,'Water'],
    # ['Grimer',80,80,50,25,'Poison'],
    # ['Muk',105,105,75,50,'Poison'],
    # ['Shellder',30,65,100,40,'Water'],
    # ['Cloyster',50,90,180,70,'Water'],
    # ['Gastly',30,35,30,80,'Ghost'],
    # ['Haunter',45,50,45,95,'Ghost'],
    # ['Gengar',60,65,60,110,'Ghost'],
    # ['Onix',35,45,160,70,'Rock'],
    # ['Drowzee',60,48,45,42,'Psychic'],
    # ['Hypno',85,73,70,67,'Psychic'],
    # ['Krabby',30,105,90,50,'Water'],
    # ['Kingler',55,130,115,75,'Water'],
    # ['Voltorb',40,30,50,100,'Electric'],
    # ['Electrode',60,50,70,140,'Electric'],
    # ['Exeggcute',60,40,80,40,'Grass'],
    # ['Exeggutor',95,95,85,55,'Grass'],
    # ['Cubone',50,50,95,35,'Ground'],
    # ['Marowak',60,80,110,45,'Ground'],
    # ['Hitmonlee',50,120,53,87,'Fighting'],
    # ['Hitmonchan',50,105,79,76,'Fighting'],
    # ['Lickitung',90,55,75,30,'Normal'],
    # ['Koffing',40,65,95,35,'Poison'],
    # ['Weezing',65,90,120,60,'Poison'],
    # ['Rhyhorn',80,85,95,25,'Ground'],
    # ['Rhydon',105,130,120,40,'Ground'],
    # ['Chansey',250,5,5,50,'Normal'],
    # ['Tangela',65,55,115,60,'Grass'],
    # ['Kangaskhan',105,95,80,90,'Normal'],
    # ['Horsea',30,40,70,60,'Water'],
    # ['Seadra',55,65,95,85,'Water'],
    # ['Goldeen',45,67,60,63,'Water'],
    # ['Seaking',80,92,65,68,'Water'],
    # ['Staryu',30,45,55,85,'Water'],
    # ['Starmie',60,75,85,115,'Water'],
    # ['Mr. Mime',40,45,65,90,'Psychic'],
    # ['Scyther',70,110,80,105,'Bug'],
    # ['Jynx',65,50,35,95,'Ice'],
    # ['Electabuzz',65,83,57,105,'Electric'],
    # ['Magmar',65,95,57,93,'Fire'],
    # ['Pinsir',65,125,100,85,'Bug'],
    # ['Tauros',75,100,95,110,'Normal'],
    # ['Magikarp',20,10,55,80,'Water'],
    # ['Gyarados',95,125,79,81,'Water'],
    # ['Lapras',130,85,80,60,'Water'],
    # ['Ditto',48,48,48,48,'Normal'],
    # ['Eevee',55,55,50,55,'Normal'],
    # ['Vaporeon',130,65,60,65,'Water'],
    # ['Jolteon',65,65,60,130,'Electric'],
    # ['Flareon',65,130,60,65,'Fire'],
    # ['Porygon',65,60,70,40,'Normal'],
    # ['Omanyte',35,40,100,35,'Rock'],
    # ['Omastar',70,60,125,55,'Rock'],
    # ['Kabuto',30,80,90,55,'Rock'],
    # ['Kabutops',60,115,105,80,'Rock'],
    # ['Aerodactyl',80,105,65,130,'Rock'],
    # ['Snorlax',160,110,65,30,'Normal'],
    # ['Articuno',90,85,100,85,'Ice'],
    # ['Zapdos',90,90,85,100,'Electric'],
    # ['Moltres',90,100,90,90,'Fire'],
    # ['Dratini',41,64,45,50,'Dragon'],
    # ['Dragonair',61,84,65,70,'Dragon'],
    # ['Dragonite',91,134,95,80,'Dragon'],
    # ['Mewtwo',106,110,90,130,'Psychic'],
    # ['Mew',100,100,100,100,'Psychic']]

    # for pokemon in all_of_them:
    #     Pokedex.add_to_pokedex(pokemon)