import os.path
import pygame
import random
import math

from classes import Enemy, Ninja, Tank, Obstacle, Trap

filepath = os.path.dirname(__file__)

# level = 0
# mobile_group = pygame.sprite.Group()


class Room:
    difficulty = "normal"
    enemy_types = 3
    active_enemies = 0
    num_enemies = 0
    level = 0
    forward = 0
    backward = 0
    status = "progressing"
    enemy_group = pygame.sprite.Group()
    obstacle_group = pygame.sprite.Group()

    def __init__(self, level):
        self.level = level
        self.prepare_obstacles(level)
        self.determine_enemies(level)
        self.prepare_enemies(self.active_enemies)

    def determine_enemies(self, level):
        self.num_enemies = random.randint(level+2, level+5)
        if level < 3:
            self.active_enemies = 1
        elif 3 <= level < 5:
            self.active_enemies = 2
        elif level >= 5:
            self.active_enemies = 3

    def prepare_enemies(self, enem_types):
        bees, ninjas, tanks = 0, 0, 0
        if enem_types == 1:
            bees = self.num_enemies
        elif enem_types == 2:
            bees = math.floor(self.num_enemies * .7)
            ninjas = math.ceil(self.num_enemies * .3)
        elif enem_types == 3:
            bees = math.floor(self.num_enemies * .5)
            ninjas = math.ceil(self.num_enemies * .3)
            tanks = math.floor(self.num_enemies * .2)

        for i in range(self.num_enemies):
            x_pos = random.randint(70, 730)
            y_pos = random.randint(70, 525)
            if bees > 0:
                e = Enemy(x_pos, y_pos)
                self.enemy_group.add(e)
                bees -= 1
            elif bees == 0 and ninjas > 0:
                e = Ninja(x_pos, y_pos)
                self.enemy_group.add(e)
                ninjas -= 1
            elif bees == 0 and ninjas == 0 and tanks > 0:
                e = Tank(x_pos, y_pos)
                self.enemy_group.add(e)
                tanks -= 1

    def determine_obstacles(self, level):
        pattern = 0
        if level == 0:
            pattern = 0
        elif level < 3:
            pattern = 1
        elif 3 <= level <= 5:
            pattern = 2
        elif 5 <= level <= 7:
            pattern = 3
        return pattern

    def prepare_obstacles(self, level):
        pattern = self.determine_obstacles(level)
        x = 0
        y = 0

        if pattern == 1:
            x = 370
            y = 396
            for i in range(13):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                y -= 16
            x = 430
            y = 396
            for i in range(13):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                y -= 16
            x = 370
            y = 300
            for i in range(7):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                x -= 16
            x = 430
            y = 300
            for i in range(7):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                x += 16
