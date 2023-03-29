import pygame
import config
import math
import utilities
from game_state import GameState

class Battle:
    def __init__(self, screen, pokemon, player):
        self.screen = screen
        self.pokemon = pokemon
        self.player = player

    def load(self):
        pass

    def render(self):
        self.screen.fill(config.WHITE)
        print("inside render in battle, pokemon: " , self.pokemon)

        rect = pygame.Rect(1, 1, 2, 2)
        self.screen.blit(self.pokemon.image, rect)

        self.screen.blit(self.player.image, (320, 40))

        font = pygame.font.SysFont(None, 24)
        img = font.render("health: " + str(self.pokemon.remaining_hp) + " Attack: " + str(self.pokemon.pokedex_id.attack), True, config.BLACK)
        self.screen.blit(img, (20, 120))

        img = font.render("press enter to attack!", True, config.BLACK)
        self.screen.blit(img, (20, 220))


        pass

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                if event.key == pygame.K_RETURN:
                    self.pokemon.remaining_hp = self.pokemon.remaining_hp - 1