
import pygame
import config
import math
import utilities
import mixer

pygame.mixer.init()
pygame.mixer.music.load("lib/audio/[INSTRUMENTAL] Justin Timberlake - SexyBack.mp3")

class Map:
    def __init__(self, screen):
        self.screen = screen
        self.map_array = []
        self.camera = [0,0]
    
    def load(self, file_name):
        
        with open('lib/maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1,2):
                    tiles.append(line[i])
                self.map_array.append(tiles)
            print(self.map_array)
            # pygame.mixer.music.play(-1)

    def render(self, screen, player, objects):
        self.determine_camera(player)

        y_pos = 0
        for line in self.map_array:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE - (self.camera[1] * config.SCALE), config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1

            y_pos = y_pos + 1

        for object in objects:
            object.render(self.screen, self.camera)
    
    def determine_camera(self,player):
        max_y_position = len(self.map_array)
        y_postion = player.position[1] - math.ceil(round(config.HEIGHT/config.SCALE/2))
        # print("max y pos : ",max_y_position)
        if y_postion <0:
            self.camera[1]= 0
        elif y_postion<9:
            self.camera[1] = y_postion
        else:
            self.camera[1] = 9

map_tile_image = {
    config.MAP_TILE_GRASS : pygame.transform.scale(pygame.image.load("lib/img/grass1.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_WATER : pygame.transform.scale(pygame.image.load("lib/img/water.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_LONG_GRASS : pygame.transform.scale(pygame.image.load("lib/img/tallgrass.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_ROAD : pygame.transform.scale(pygame.image.load("lib/img/road.png"),(config.SCALE, config.SCALE)),
    }