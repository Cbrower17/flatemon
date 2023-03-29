import pygame
import config
from game_state import GameState

from game import Game

print("Do you want to play a game?")
choice = input("[y/n]")
print(choice)
if choice == 'y':
    pygame.init()

    screen = pygame.display.set_mode((config.HEIGHT, config.WIDTH))

    pygame.display.set_caption("Pokemon Clone")

    clock = pygame.time.Clock()

    game = Game(screen)
    game.set_up()


    while game.game_state == GameState.RUNNING:
        clock.tick(50)
        game.update()
        pygame.display.flip()