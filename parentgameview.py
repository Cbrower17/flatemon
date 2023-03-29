import pygame
import config
import math
import utilities
from game_state import GameState
class GameView:
    def __init__(self, screen):
        self.screen = screen

    def load(self):
        pass

    def render(self):
        self.screen.fill(config.BLACK)



        pass

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
    