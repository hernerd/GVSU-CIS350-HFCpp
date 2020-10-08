import pygame
import os.path

filepath = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.name = "player"
        self.image = pygame.image.load(os.path.join(filepath, "assets/player.png")).convert_alpha()
        self.x = x_pos
        self.y = y_pos
        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]
        self.mask = pygame.mask.from_surface(self.image)
        self.xSpeed = 0.2
        self.ySpeed = 0.2
        self.x_change = 0
        self.y_change = 0

    def pos(self, x_pos, y_pos):
        self.rect.center = [x_pos, y_pos]
        self.x = x_pos
        self.y = y_pos


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = "enemy"
        self.image = pygame.image.load(os.path.join(filepath, "assets/bee.png")).convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.mask = pygame.mask.from_surface(self.image)
        self.x_change = .3
        self.y_change = .3

    def pos(self, x, y):
        self.rect.center = [x, y]
        self.x = x
        self.y = y


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(filepath, "assets/crate.png")).convert_alpha()
        self.x = pos_x
        self.y = pos_y
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.mask = pygame.mask.from_surface(self.image)
