import random

import pygame
import config
import math
import utilities

from player import Player
from game_state import GameState, CurrentGameState
from monsterfactory import MonsterFactory
from game_view.map import Map
from game_view.battle import Battle

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.current_game_state = CurrentGameState.MAP
        self.player_has_moved = False
        self.monster_factory = MonsterFactory()
        self.map = Map(screen)
        self.battle = None

    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        print("do set up")
        self.game_state = GameState.RUNNING
        self.map.load("01")

    def update(self):
        if self.current_game_state == CurrentGameState.MAP:
            self.player_has_moved = False
            self.screen.fill(config.BLACK)
            # print("update")
            self.handle_events()

            self.map.render(self.screen, self.player, self.objects)

            if self.player_has_moved:
                self.determine_game_events()
        elif self.current_game_state == CurrentGameState.BATTLE:
            self.battle.update()
            self.battle.render()

            if self.battle.pokemon.remaining_hp <= 0:
                self.current_game_state = CurrentGameState.MAP

        # self.player_has_moved = False
        # self.screen.fill(config.BLACK)
        # self.handle_events()
        # self.render_map(self.screen)
        # for object in self.objects:
        #     object.render(self.screen, self.camera)
        #     if self.player_has_moved:
        #         self.determine_game_events()

    def determine_game_events(self):
        map_tile = self.map.map_array[self.player.position[1]][self.player.position[0]]
        print(map_tile)

        if map_tile == config.MAP_TILE_LONG_GRASS:
            self.determine_pokemon_found(map_tile)
            print("in the tall grass")
        else:
            return

    def determine_pokemon_found(self, map_tile):
        random_number = utilities.generate_random_number(1, 10)
        
        # 20 percent chance of hitting pokemon
        if random_number <= 2:
            found_monster = self.monster_factory.find_pokemon()
            # print("you found a monster!")
            # print("Monster Type: " + found_monster.type)
            # print("Attack: " + str(found_monster.attack))
            # print("Health: " + str(found_monster.health))
            self.battle = Battle(self.screen, found_monster, self.player)
            self.current_game_state = CurrentGameState.BATTLE


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED
                elif event.key == pygame.K_w: # up
                    self.move_unit(self.player, [0, -1])
                elif event.key == pygame.K_s: # down
                    self.move_unit(self.player, [0, 1])
                elif event.key == pygame.K_a: # up
                    self.move_unit(self.player, [-1, 0])
                elif event.key == pygame.K_d: # up
                    self.move_unit(self.player, [1, 0])

    # def load_map(self, file_name):
    #     with open('lib/maps/' + file_name + ".txt") as map_file:
    #         for line in map_file:
    #             tiles = []
    #             for i in range(0, len(line) - 1,2):
    #                 tiles.append(line[i])
    #             self.map_array.append(tiles)
    #         print(self.map_array)

    # def render_map(self, screen):
    #     self.determine_camera()

    #     y_pos = 0
    #     for line in self.map_array:
    #         x_pos = 0
    #         for tile in line:
    #             image = map_tile_image[tile]
    #             rect = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE - (self.camera[1] * config.SCALE), config.SCALE, config.SCALE)
    #             screen.blit(image, rect)
    #             x_pos = x_pos + 1

    #         y_pos = y_pos + 1

    def move_unit(self, unit, position_change):
            new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]
            if new_position[0] < 0 or new_position[0] > (len(self.map.map_array[0]) - 1):
                return
            if new_position[1] < 0 or new_position[1] > (len(self.map.map_array) - 1):
                return
            if self.map.map_array[new_position[1]][new_position[0]] == config.MAP_TILE_WATER:
                return
            
            self.player_has_moved = True

            unit.update_position(new_position)

    # def determine_camera(self):
    #     max_y_position = len(self.map_array)
    #     y_postion = self.player.position[1] - math.ceil(round(config.HEIGHT/config.SCALE/2))
    #     # print("max y pos : ",max_y_position)
    #     if y_postion <0:
    #         self.camera[1]= 0
    #     elif y_postion<9:
    #         self.camera[1] = y_postion
    #     else:
    #         self.camera[1] = 9
            

        

map_tile_image = {
    config.MAP_TILE_GRASS : pygame.transform.scale(pygame.image.load("lib/img/grass1.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_WATER : pygame.transform.scale(pygame.image.load("lib/img/water.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_LONG_GRASS : pygame.transform.scale(pygame.image.load("lib/img/tallgrass.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_ROAD : pygame.transform.scale(pygame.image.load("lib/img/road.png"),(config.SCALE, config.SCALE)),
}


# if 0 < y_postion and y_postion  <= max_y_position:
#             self.camera[1] = y_postion
#         elif y_postion <0:
#             self.camera[1]= 0
#         else:
#             self.camera[1]= max_y_position + 2