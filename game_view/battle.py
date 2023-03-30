import pygame
import config
import math
import utilities
from game_state import GameState

class Battle:
    def __init__(self, screen, wildpokemon, player):
        self.screen = screen
        self.pokemon = wildpokemon
        self.player = player
        self.party =self.player.trainer.party[0]
        print("nickanme:",self.pokemon.nickname,"|","p_id:",self.pokemon.pokedex_id.id,"|","pokemon should be:",self.pokemon.pokedex_id.name)
        

    def load(self):
        pass

    def render(self):
        self.screen.fill(config.WHITE)
        font = pygame.font.Font("fonts/PokemonGb.ttf", 14)
        
        # draw wild pokemon
        


        # draw health bar and styling boxes
        self.screen.blit(battle_images["monster_pad"], (0, 300))
        self.screen.blit(battle_images["name_card"], (310, 300))
        self.screen.blit(battle_images["hp_bar"], (340, 335))
        self.screen.blit(battle_images["monster_pad"], (300, 100))
        self.screen.blit(self.pokemon.image_front, (425,100))
        # draw active pokemon
        self.screen.blit(battle_images["name_card"], (15, 50))
        self.screen.blit(battle_images["hp_bar"], (50, 85))
        self.screen.blit(battle_images["menu"], (0, 388))
        self.screen.blit(self.party.partymember[0].pokemon.image_back, (100, 300))

        # font = pygame.font.SysFont("fonts/PokemonGb.ttf", 30)
        img = font.render("health: " + str(self.pokemon.remaining_hp), True, config.BLACK)
        self.screen.blit(img, (25, 65))
        img = font.render(" 1: " + str(self.party.partymember[0].pokemon.move_set_id.move_1.name), True, config.BLACK)
        self.screen.blit(img, (315, 410))
        img = font.render(" 2: " + str(self.party.partymember[0].pokemon.move_set_id.move_2.name), True, config.BLACK)
        self.screen.blit(img, (455, 410))
        img = font.render(" 3: " + str(self.party.partymember[0].pokemon.move_set_id.move_3.name), True, config.BLACK)
        self.screen.blit(img, (315, 450))
        img = font.render(" 4: " + str(self.party.partymember[0].pokemon.move_set_id.move_4.name), True, config.BLACK)
        self.screen.blit(img, (455, 450))

        img = font.render("press a key to", True, config.BLACK)
        self.screen.blit(img, (20, 410))
        img = font.render("attack!", True, config.BLACK)
        self.screen.blit(img, (20, 450))


        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                if event.key == pygame.K_1:
                    self.pokemon.remaining_hp = self.pokemon.remaining_hp - self.party.partymember[0].pokemon.move_set_id.move_1.damage
                    # self.pokemon.change_hp(self.pokemon.remaining_hp)
                if event.key == pygame.K_2:
                    self.pokemon.remaining_hp = self.pokemon.remaining_hp - self.party.partymember[0].pokemon.move_set_id.move_2.damage
                    # self.pokemon.change_hp(self.pokemon.remaining_hp)
                if event.key == pygame.K_3:
                    self.pokemon.remaining_hp = self.pokemon.remaining_hp - self.party.partymember[0].pokemon.move_set_id.move_3.damage
                    # self.pokemon.change_hp(self.pokemon.remaining_hp)
                if event.key == pygame.K_4:
                    self.pokemon.remaining_hp = self.pokemon.remaining_hp - self.party.partymember[0].pokemon.move_set_id.move_4.damage
                    # self.pokemon.change_hp(self.pokemon.remaining_hp)


battle_images = {
    "monster_pad": pygame.transform.scale(pygame.image.load("lib/img/battleimg/monster_pad.png"), (300, 88)),
    "name_card": pygame.transform.scale(pygame.image.load("lib/img/battleimg/name_card.png"), (300, 80)),
    "hp_bar": pygame.transform.scale(pygame.image.load("lib/img/battleimg/hp_bar.png"), (250, 20)),
    "menu": pygame.image.load("lib/img/battleimg/menu.png"),
}