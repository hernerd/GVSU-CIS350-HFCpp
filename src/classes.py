import pygame
import os.path
from spritesheet import SpriteSheet

filepath = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    images = []
    moving = False

    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.load_images()
        self.name = "player"
        self.image = self.images[0]
        self.frame = 0
        self.x = x_pos
        self.y = y_pos
        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]
        self.mask = pygame.mask.from_surface(self.image)
        self.xSpeed = 5
        self.ySpeed = 5
        self.x_change = 0
        self.y_change = 0

    def load_images(self):
        i = 0
        img_x = 0
        img_y = 0
        player_sheet = SpriteSheet("assets/player_spritesheet.png")
        for i in range(9):
            for j in range(5):
                self.images.append(player_sheet.get_image(img_x, img_y, 50, 37))
            img_x += 50
            i += 1

    def pos(self, x_pos, y_pos):
        if not self.moving:
            self.image = self.images[self.frame]
            self.mask = pygame.mask.from_surface(self.image)
            # print("Frames: ", self.frame)
            self.frame += 1
            if self.frame >= 45:
                self.frame = 0
        if self.moving:
            self.image = self.images[0]
            self.frame = 0
            self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = [x_pos, y_pos]
        self.x = x_pos
        self.y = y_pos

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

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = "bullet"
        self.image = pygame.image.load(os.path.join(filepath, "assets/projectile.png")).convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = ""

    def pos(self, x, y):
        self.rect.center = [x, y]
        self.x = x
        self.y = y
