import pygame
import config
from game_state import GameState

from game import Game

from lib.move import Move
from lib.pokedex import Pokedex
from lib.move_set import MoveSet
from lib.party import Party
from lib.trainer import Trainer
from lib.pokemon import Pokemon
from lib.pokeparty import PokeParty

print("Do you want to play a game?")
choice = input("[y/n]")
print(choice)
if choice == 'y':
    Move.get_all()
    MoveSet.get_all()
    Trainer.get_all()
    Pokedex.get_all()
    Pokemon.get_all()
    Party.get_all()
    PokeParty.get_all()

    pygame.init()

    screen = pygame.display.set_mode((config.HEIGHT, config.WIDTH))

    pygame.display.set_caption("Pokemon Clone")

    clock = pygame.time.Clock()

    game = Game(screen,Trainer.all[0])
    game.set_up()


    while game.game_state == GameState.RUNNING:
        clock.tick(50)
        game.update()
        pygame.display.flip()