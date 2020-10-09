import os.path
import pygame
import random

from powerUp import MovementPowerUp
from classes import Player, Enemy, Obstacle, Bullet

filepath = os.path.dirname(__file__)

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Dungeon Crawler")

# Player
playerX = 400
playerY = 480
player = Player(playerX, playerY)
playerX_change = 0
playerY_change = 0

# crate
crateX = 400
crateY = 300
crate = Obstacle(crateX, crateY)

# Enemy
enemyX = random.randint(0, 800)
enemyY = random.randint(0, 600)
enemy = Enemy(enemyX, enemyY)
enemy.x_change = 0.3
enemy.y_change = 0.1

# player group
player_group = pygame.sprite.Group()
player_group.add(player)

# obstacle group
obstacle_group = pygame.sprite.Group()
obstacle_group.add(crate)

# enemy group
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)

# mobile group (sprites that move)
mobile_group = pygame.sprite.Group()
mobile_group.add(player)
mobile_group.add(enemy)


def check_object_collision(self, obstacle):
    if pygame.sprite.collide_mask(self, obstacle):
        if self.x_change < 0:
            while pygame.sprite.collide_mask(self, obstacle):
                self.x_change = .1
                self.x += self.x_change
                self.pos(self.x, self.y)
            self.x_change = 0
        elif self.x_change > 0:
            while pygame.sprite.collide_mask(self, obstacle):
                self.x_change = -.1
                self.x += self.x_change
                self.pos(self.x, self.y)
            self.x_change = 0
        if self.y_change < 0:
            while pygame.sprite.collide_mask(self, obstacle):
                self.y_change = .1
                self.y += self.y_change
                self.pos(self.x, self.y)
            self.y_change = 0
        elif self.y_change > 0:
            while pygame.sprite.collide_mask(self, obstacle):
                self.y_change = -.1
                self.y += self.y_change
                self.pos(self.x, self.y)
            self.y_change = 0
        if self.name == "enemy":
            self.y_change = .3
            self.x_change = .3

# Bullets
bullets = []
direction_shot = ""
bullet_change = .5

# Power-ups
powerUpsOnScreen = [MovementPowerUp(random.randint(0, 800), random.randint(0, 600))]
powerUpsInEffect = []


def displayPowerUp(powerUp):
    image = pygame.image.load(os.path.join(filepath, powerUp.imagePath))
    screen.blit(image, (powerUp.x, powerUp.y))


def fire_bullet(x, y):
    screen.blit(bullet.image, (x-7, y-5))


# Game running
running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Player Movement
            if event.key == pygame.K_a:
                player.x_change = -player.xSpeed
            if event.key == pygame.K_d:
                player.x_change = player.xSpeed
            if event.key == pygame.K_w:
                player.y_change = -player.ySpeed
            if event.key == pygame.K_s:
                player.y_change = player.ySpeed

            # Bullet Movement
            # if bullet_state is "dead":
            if event.key == pygame.K_UP:
                bullet = Bullet(player.x, player.y)
                bullet.direction = "up"
                bullet.x = player.x
                bullet.y = player.y
                bullets.append(bullet)
                # fire_bullet(bullet.x, bullet.y)
            if event.key == pygame.K_DOWN:
                bullet = Bullet(player.x, player.y)
                bullet.direction = "down"
                bullet.x = player.x
                bullet.y = player.y
                bullets.append(bullet)
                # fire_bullet(bullet.x, bullet.y)
            if event.key == pygame.K_LEFT:
                bullet = Bullet(player.x, player.y)
                bullet.direction = "left"
                bullet.x = player.x
                bullet.y = player.y
                bullets.append(bullet)
                # fire_bullet(bullet.x, bullet.y)
            if event.key == pygame.K_RIGHT:
                bullet = Bullet(player.x, player.y)
                bullet.direction = "right"
                bullet.x = player.x
                bullet.y = player.y
                bullets.append(bullet)
                # fire_bullet(bullet.x, bullet.y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.x_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player.y_change = 0

    player.x += player.x_change
    if player.x <= 0:
        player.x = 0
    elif player.x >= 800:
        player.x = 800

    player.y += player.y_change
    if player.y <= 0:
        player.y = 0
    elif player.y >= 600:
        player.y = 600

    # Enemy Movement
    enemy.x += enemy.x_change
    if enemy.x <= 0:
        enemy.x_change = 0.3
    elif enemy.x >= 760:
        enemy.x_change = -0.3

    enemy.y += enemy.y_change
    if enemy.y <= 0:
        enemy.y_change = 0.1
    elif enemy.y >= 560:
        enemy.y_change = -0.1

    for mob in mobile_group:
        check_object_collision(mob, crate)

    enemy.pos(enemy.x, enemy.y)
    player.pos(player.x, player.y)

    # Checking Enemy Collisions
    if pygame.sprite.collide_mask(player, enemy):
        running = False

    # Bullet Moving
    for b in bullets:
        fire_bullet(b.x, b.y)
        if b.direction is "up":
            b.y -= bullet_change
        if b.direction is "down":
            b.y += bullet_change
        if b.direction is "left":
            b.x -= bullet_change
        if b.direction is "right":
            b.x += bullet_change
        if b.y <= 0 or b.y >= 600 or b.x <= 0 or b.x >= 800:
            bullets.remove(b)

    # check player contacting powerUp
    for powerUp in powerUpsOnScreen:
        if powerUp.x - 24 <= player.x <= powerUp.x + 24 and powerUp.y - 24 <= player.y <= powerUp.y + 24:
            powerUp.applyPlayerEffect(player)
            powerUpsOnScreen.remove(powerUp)
            powerUpsInEffect.append(powerUp)

    # display powerUps
    for powerUp in powerUpsOnScreen:
        displayPowerUp(powerUp)

    # check for expired powerUps
    for powerUp in powerUpsInEffect:
        if powerUp.removePlayerEffectIfExpired(player):
            powerUpsInEffect.remove(powerUp)

    enemy_group.draw(screen)
    obstacle_group.draw(screen)
    player_group.draw(screen)

    pygame.display.update()
