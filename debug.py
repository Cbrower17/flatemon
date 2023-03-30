import pygame
import sqlite3
import utilities
from lib.move import Move
from lib.pokedex import Pokedex
from lib.move_set import MoveSet
from lib.party import Party
from lib.trainer import Trainer
from lib.pokemon import Pokemon
from lib.pokeparty import PokeParty

if __name__ == "__main__":
    Move.get_all()
    MoveSet.get_all()
    Trainer.get_all()
    Pokedex.get_all()
    Pokemon.get_all()
    Party.get_all()
    PokeParty.get_all()
    print(Trainer.get_all())

    random_number = -1

    random_number = utilities.generate_random_number(1, 9)
    all_dex = Pokedex.get_all()
    # name = all_dex[random_number].name
    # hp = all_dex[random_number].maxhp
    
    # pokemon = Pokemon(name,random_number,hp,3,1)
    # pokemon.save()
    # print("pokeid",pokemon.id)
    # pokemon.delete_from_table()
    testchangehealth = Pokemon.all[19]
    for pokemon in Pokemon.all:
        print("pokeid",pokemon.id,"|", "pokename", pokemon.nickname,"|","pokedex", pokemon.pokedex_id.id)
    print(testchangehealth.nickname)
    testchangehealth.remaining_hp = 17
    

    
    print(Pokemon.all)