import random

import pygame
import config
import math
import utilities

from player import Player
from game_state import GameState
from monsterfactory import MonsterFactory

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.map = []
        self.camera = [0, 0]
        self.player_has_moved = False
        self.monster_factory = MonsterFactory()

    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        print("do set up")
        self.game_state = GameState.RUNNING

        self.load_map("01")

    def update(self):
        self.player_has_moved = False
        self.screen.fill(config.BLACK)
        # print("update")
        self.handle_events()

        self.render_map(self.screen)

        for object in self.objects:
            object.render(self.screen, self.camera)

        if self.player_has_moved:
            self.determine_game_events()

    def determine_game_events(self):
        map_tile = self.map[self.player.position[1]][self.player.position[0]]
        print(map_tile)

        if map_tile == config.MAP_TILE_ROAD:
            return

        self.determine_pokemon_found(map_tile)

    def determine_pokemon_found(self, map_tile):
        random_number = utilities.generate_random_number(1, 10)

        # 20% sjanse for å finne en kubenmon
        if random_number <= 2:
            found_monster = self.monster_factory.create_monster(map_tile)
            print("Du fant en Kubenmon!")
            print("Kubenmon Type: " + found_monster.type)
            print("Angrep: " + str(found_monster.attack))
            print("Liv: " + str(found_monster.health))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED
                elif event.key == pygame.K_w: #opp
                    self.move_unit(self.player, [0, -1])
                elif event.key == pygame.K_s : #ned
                    self.move_unit(self.player, [0, 1])
                elif event.key == pygame.K_a: #venstre
                    self.move_unit(self.player, [-1, 0])
                elif event.key == pygame.K_d: # høyre
                    self.move_unit(self.player, [1, 0])

    def load_map(self, file_name):
        with open('Kubenmon/maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map.append(tiles)
            print(self.map)

    def render_map(self, screen):
        self.determine_camera()

        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE - (self.camera[1] * config.SCALE), config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1

            y_pos = y_pos + 1


    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        # check if off map
        if new_position[0] < 0 or new_position[0] > (len(self.map[0]) - 1):
            return

        if new_position[1] < 0 or new_position[1] > (len(self.map) - 1):
            return

        # check for valid movement
        if self.map[new_position[1]][new_position[0]] == config.MAP_TILE_WATER:
            return

        self.player_has_moved = True
        

        unit.update_position(new_position)

    def determine_camera(self):
        max_y_position = len(self.map) - config.SCREEN_HEIGHT / config.SCALE
        y_position = self.player.position[1] - math.ceil(round(config.SCREEN_HEIGHT/ config.SCALE / 2))

        if y_position <= max_y_position and y_position >= 0:
            self.camera[1] = y_position
        elif y_position < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = max_y_position


map_tile_image = {
    config.MAP_TILE_GRASS : pygame.transform.scale(pygame.image.load("Kubenmon/imgs/grass1.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_WATER: pygame.transform.scale(pygame.image.load("Kubenmon/imgs/water.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_ROAD: pygame.transform.scale(pygame.image.load("Kubenmon/imgs/road.png"), (config.SCALE, config.SCALE)),
}