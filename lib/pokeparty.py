import pygame
import sqlite3

CONN = sqlite3.connect('Pokemon.db')
CURSOR = CONN.cursor()

class PokeParty:
    all = []

    def __init__(self,party,pokemon):
        self.party = party
        self.pokemon = pokemon
        self.party.partymember.append(self)

    # properties
    def get_party(self):
        return self._party
    
    def set_party(self, party_id):
        from lib.party import Party
        self._party = Party.all[party_id]
    
    party = property(get_party,set_party)

    def get_pokemon(self):
        return self._pokemon
    
    # i want set pokemon to work if you give an id or a valid pokemon object
    def set_pokemon(self, pokemon):
        from lib.pokemon import Pokemon
        if isinstance(pokemon, int):
            self._pokemon = Pokemon.all[pokemon]
        elif isinstance(pokemon,Pokemon):
            self._pokemon = pokemon
        else:
            raise Exception ("neither pokemon object or id")
    pokemon = property(get_pokemon, set_pokemon)

    # time for some databse methods
    def save(self):
        sql = """
            INSERT INTO Poke_Party ()
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.party.id, self.pokemon.id))

        CONN.commit()

        # self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]


    @classmethod
    def add_to_pokeparty(cls,row):
        # getting elements from list all of them 
        pokedex_entry = cls(row[0],row[1])
        pokedex_entry.save()

    
# db methods
    @classmethod
    def new_from_db(cls, row):
        pokeparty = cls(row[1],row[2])
        pokeparty.id = row[0]
        return pokeparty
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM Poke_Party
        """
        all = CURSOR.execute(sql).fetchall()
        # print(all)
        # cls.all = [cls.new_from_db(row) for row in all]
        for row in all:
            # print("row inside loop:",row)
            cls.all.append(cls.new_from_db(row))
        return cls.all




