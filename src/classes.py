import pygame
import os.path
from spritesheet import SpriteSheet

filepath = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    idle_right = []
    right_walk = []
    idle_left = []
    left_walk = []
    i_frame = 0
    r_frame = 0
    moving = False
    facing = "right"
    dirX = ""
    dirY = ""

    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.load_images()
        self.name = "player"
        self.image = self.idle_right[0]
        self.x = x_pos
        self.y = y_pos
        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]
        self.mask = pygame.mask.from_surface(self.image)
        self.xSpeed = 5
        self.ySpeed = 5
        self.bullet = "bullet"
        self.x_change = 0
        self.y_change = 0
        self.health = 100
        self.inventory = []
        self.inventorySelected = -1

    def load_images(self):
        img_x = 0
        img_y = 0
        player_sheet = SpriteSheet("assets/player_spritesheet.png")
        player_walk = SpriteSheet("assets/player_walk.png")
        player_left = SpriteSheet("assets/player_left.png")
        player_walk_left = SpriteSheet("assets/player_walk_left.png")
        for i in range(10):
            for j in range(6):
                self.idle_right.append(player_sheet.get_image(img_x, img_y, 50, 37))
                self.idle_left.append(player_left.get_image(img_x, img_y, 50, 37))
            img_x += 50
        img_x = 0
        for i in range(8):
            for j in range(6):
                self.right_walk.append(player_walk.get_image(img_x, img_y, 50, 37))
                self.left_walk.append(player_walk_left.get_image(img_x, img_y, 50, 37))
            img_x += 50

    def pos(self, x_pos, y_pos):
        if not self.moving:
            if self.facing == "right":
                self.image = self.idle_right[self.i_frame]
            if self.facing == "left":
                self.image = self.idle_left[self.i_frame]
            self.mask = pygame.mask.from_surface(self.image)
            # print("Frames: ", self.i_frame)
            self.i_frame += 1
            if self.i_frame >= 60:
                self.i_frame = 0
        if self.moving:
            if self.facing == "right":
                self.image = self.right_walk[self.r_frame]
            if self.facing == "left":
                self.image = self.left_walk[self.r_frame]
            self.mask = pygame.mask.from_surface(self.image)
            # print("Frames: ", self.r_frame)
            self.r_frame += 1
            if self.r_frame >= 48:
                self.r_frame = 0
        self.rect.center = [x_pos, y_pos]
        self.x = x_pos
        self.y = y_pos

    def addToInventory(self, powerUp):
        if self.inventorySelected == -1:
            self.inventorySelected = 0

        self.inventory.append(powerUp)

    def useCurrentItem(self):
        if self.inventorySelected == -1:
            return None
        if self.inventorySelected == 0:
            powerUp = self.inventory[self.inventorySelected]
            self.inventory.remove(powerUp)
            if len(self.inventory) > 0:
                return powerUp
            else:
                self.inventorySelected = -1
        else:
            powerUp = self.inventory[self.inventorySelected]
            self.inventory.remove(powerUp)
            self.inventorySelected = self.inventorySelected - 1
            return powerUp

    def getCurrentInventoryItem(self):
        if self.inventorySelected == -1:
            return None

        return self.inventory[self.inventorySelected]

    def setNextInventoryItem(self):
        inventoryLength = len(self.inventory)

        if self.inventorySelected == -1:
            return
        elif inventoryLength == 1:
            return
        elif self.inventorySelected == inventoryLength - 1:
            self.inventorySelected = 0
        else:
            self.inventorySelected = self.inventorySelected + 1


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
        self.x_change = 10
        self.y_change = 10
        self.health = 10
        self.damage = 10

    def pos(self, x, y):
        self.rect.center = [x, y]
        self.x = x
        self.y = y

class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = "tank"
        self.image = pygame.image.load(os.path.join(filepath, "assets/tank.png")).convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.mask = pygame.mask.from_surface(self.image)
        self.x_change = 1
        self.y_change = 1
        self.health = 20
        self.damage = 20

    def pos(self, x, y):
        self.rect.center = [x, y]
        self.x = x
        self.y = y

class Ranger(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = "ranger"
        self.image = pygame.image.load(os.path.join(filepath, "assets/ranger.png")).convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.mask = pygame.mask.from_surface(self.image)
        self.x_change = 1
        self.y_change = 1
        self.health = 10
        self.damage = 10

    def pos(self, x, y):
        self.rect.center = [x, y]
        self.x = x
        self.y = y

class Ninja(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = "ninja"
        self.image = pygame.image.load(os.path.join(filepath, "assets/ninja.png")).convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.mask = pygame.mask.from_surface(self.image)
        self.x_change = 15
        self.y_change = 15
        self.health = 5
        self.damage = 5

    def pos(self, x, y):
        self.rect.center = [x, y]
        self.x = x
        self.y = y

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = "boss"
        self.image = pygame.image.load(os.path.join(filepath, "assets/boss.png")).convert_alpha()
        #400
        self.x = x
        #290
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.mask = pygame.mask.from_surface(self.image)
        self.x_change = 15
        self.y_change = 15
        self.health = 500
        self.damage = 20

    def pos(self, x, y):
        self.rect.center = [x, y]
        self.x = x
        self.y = y


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(filepath, "assets/crate.png")).convert_alpha()
        self.name = "obstacle"
        self.type = "obstacle"
        self.x = pos_x
        self.y = pos_y
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.mask = pygame.mask.from_surface(self.image)
        self.damage = 0

        
class Trap(Obstacle):
    def __init__(self, pos_x, pos_y, obst_type):
        super().__init__(pos_x, pos_y)
        if obst_type == "spikes":
            self.image = pygame.image.load(os.path.join(filepath, "assets/spikes.png")).convert_alpha()
            self.name = "spikes"
            self.damage = 2
        self.type = "trap"
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.mask = pygame.mask.from_surface(self.image)
        
        
class Door(pygame.sprite.Sprite):
    images = []
    frame = 0

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.load_images()
        self.image = self.images[0]
        self.x = pos_x
        self.y = pos_y
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.mask = pygame.mask.from_surface(self.image)

    def load_images(self):
        door = SpriteSheet("assets/door.png")
        dx = 0
        for i in range(3):
            self.images.append(door.get_image(dx, 0, 116, 60))
            dx += 116

    def updateImage(self):
        self.frame += 1
        self.image = self.images[self.frame]
        self.rect.center = [self.x, self.y]
        self.mask = pygame.mask.from_surface(self.image)

    def reset_image(self):
        self.frame = 0
        self.image = self.images[self.frame]
        self.rect.center = [self.x, self.y]
        self.mask = pygame.mask.from_surface(self.image)

            
class Bullet(pygame.sprite.Sprite):
    images = []
    moving = True

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.load_images()
        self.name = "bullet"
        # self.image = pygame.image.load(os.path.join(filepath, "assets/projectile.png")).convert_alpha()
        self.image = self.images[0]
        self.frame = 0
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = ""
        self.damage = 5

    def load_images(self):
        img_x = 0
        img_y = 0
        bullet_sheet = SpriteSheet("assets/projectile_spritesheet.png")
        for i in range(2):
            for j in range(10):
                self.images.append(bullet_sheet.get_image(img_x, img_y, 16, 16))
            img_x += 16
        for i in range(20):
            self.images[i] = pygame.transform.smoothscale(self.images[i], (8, 8))

    def pos(self, x, y):
        if self.frame >= 20:
            self.frame = 0
        if self.moving:
            self.image = self.images[self.frame]
            self.frame += 1
        self.rect.center = [x, y]
        self.x = x
        self.y = y

class Fire(pygame.sprite.Sprite):
    images = []
    moving = True

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.load_images()
        self.name = "fire"
        # self.image = pygame.image.load(os.path.join(filepath, "assets/projectile.png")).convert_alpha()
        self.image = self.images[0]
        self.frame = 0
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = ""
        self.damage = 5

    def load_images(self):
        img_x = 0
        img_y = 0
        bullet_sheet = SpriteSheet("assets/fire_spritesheet.png")
        for i in range(2):
            for j in range(10):
                self.images.append(bullet_sheet.get_image(img_x, img_y, 16, 16))
            img_x += 16
        for i in range(20):
            self.images[i] = pygame.transform.smoothscale(self.images[i], (8, 8))

    def pos(self, x, y):
        if self.frame >= 20:
            self.frame = 0
        if self.moving:
            self.image = self.images[self.frame]
            self.frame += 1
        self.rect.center = [x, y]
        self.x = x
        self.y = y
