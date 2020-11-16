import os.path
import pygame
import random
import math

from classes import Enemy, Ninja, Tank, Obstacle, Trap, Ranger, Boss

filepath = os.path.dirname(__file__)


class Room:
    difficulty = "normal"
    enemy_types = 3
    active_enemies = 0
    num_enemies = 0
    level = 0
    status = "progressing"
    patterns = []
    # enemy_group = pygame.sprite.Group()
    # obstacle_group = pygame.sprite.Group()

    def __init__(self, level):
        self.patterns = []
        self.enemy_group = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        self.level = level
        self.index = 0
        self.forward = None
        self.backward = None
        self.determine_obstacles(level)
        self.prepare_obstacles(level)
        self.determine_enemies(level)
        self.prepare_enemies(self.active_enemies)
        # print(self.obstacle_group, self.enemy_group, self.patterns)

    def determine_enemies(self, level):
        if level != 10:
            self.num_enemies = random.randint(level+1, level+3)
        else:
            self.num_enemies = 1
        if level < 3:
            self.active_enemies = 1
        elif 3 <= level < 5:
            self.active_enemies = 2
        elif level == 10:
            self.active_enemies = 4
        elif level >= 5:
            self.active_enemies = 3

    def prepare_enemies(self, enem_types):
        bees, ninjas, tanks, rangers, boss = 0, 0, 0, 0, 0
        if enem_types == 1:
            bees = self.num_enemies
        elif enem_types == 2:
            bees = math.floor(self.num_enemies * .5)
            ninjas = math.floor(self.num_enemies * .2)
            rangers = math.ceil(self.num_enemies *.3)

        elif enem_types == 3:
            bees = math.floor(self.num_enemies * .5)
            ninjas = math.ceil(self.num_enemies * .3)
            tanks = math.floor(self.num_enemies * .2)
        
        elif enem_types == 4:
            boss = self.num_enemies

            

        for i in range(self.num_enemies):
            x_pos = random.randint(70, 730)
            y_pos = random.randint(70, 525)
            if bees > 0:
                e = Enemy(x_pos, y_pos)
                self.enemy_group.add(e)
                bees -= 1
            elif boss == 1:
                e = Boss(400,290)
                self.enemy_group.add(e)
                boss -= 1
            elif bees == 0 and ninjas > 0:
                e = Ninja(x_pos, y_pos)
                self.enemy_group.add(e)
                ninjas -= 1
            elif bees == 0 and ninjas == 0 and rangers > 0:
                e = Ranger(x_pos, y_pos)
                self.enemy_group.add(e)
                rangers -= 1
            elif bees == 0 and ninjas == 0 and rangers == 0 and tanks > 0:
                e = Tank(x_pos, y_pos)
                self.enemy_group.add(e)
                tanks -= 1
            

    def determine_obstacles(self, level):
        if level == 0:
            return
        else:
            for i in range(4):
                self.patterns.append(random.randint(0, 1))

            # print(self.patterns)

    def prepare_obstacles(self, level):
        patterns = self.patterns
        x = 0
        y = 0
        if len(patterns) == 0:
            return

        if patterns[0] == 1:
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
                x -= 16
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
            x = 430
            y = 300
            for i in range(7):
                x += 16
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
        if patterns[1] == 1:
            x = 274
            y = 316
            for i in range(3):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                y += 16
            x = 526
            y = 284
            for i in range(3):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                y -= 16
            x = 490
            y = 348
            for i in range(8):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                x += 16
            x = 310
            y = 252
            for i in range(8):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                x -= 16
            x = 262
            for i in range(7):
                y -= 16
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
            x = 538
            y = 348
            for i in range(7):
                y += 16
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
        if patterns[2] == 1:
            x = 384
            y = 464
            for i in range(3):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                x += 16
            x = 602
            y = 412
            for i in range(4):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                x += 16
            o = Obstacle(x-16, y+16)
            self.obstacle_group.add(o)
            x = 198
            y = 172
            for i in range(4):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                x -= 16
            o = Obstacle(x+16, y-16)
            self.obstacle_group.add(o)
            x = 640
            y = 284
            for i in range(3):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                y += 16
            x = 592
            y = 236
            for i in range(4):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                y -= 16
            x = 544
            y = 172
            for i in range(6):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                x += 16
            x = 160
            y = 284
            for i in range(3):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                y += 16
            x = 208
            y = 348
            for i in range(4):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                y += 16
            x = 176
            y = 412
            for i in range(6):
                o = Obstacle(x, y)
                self.obstacle_group.add(o)
                x += 16
