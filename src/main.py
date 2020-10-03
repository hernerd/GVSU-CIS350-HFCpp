import os.path

import pygame

from src.powerUp import MovementPowerUp
from src.types import Player

filepath = os.path.dirname(__file__)

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Dungeon Crawler")

# Player
playerImage = pygame.image.load(os.path.join(filepath, "assets/player.png"))
player = Player(370, 480)
playerX_change = 0
playerY_change = 0

# Bullet
#   Dead - bullet is not shot yet
#   Live - bullet is in motion
bulletIcon = pygame.image.load(os.path.join(filepath, "assets/projectile.png"))
bulletX = 370
bulletY = 480
bulletX_change = 0
bulletY_change = .5
bullet_state = "dead"
direction_shot = ""

# Powerups
powerUpsOnScreen = [MovementPowerUp(200, 200)]
powerUpsInEffect = []


def displayPowerUp(powerUp):
    image = pygame.image.load(os.path.join(filepath, powerUp.imagePath))
    screen.blit(image, (powerUp.x, powerUp.y))


def displayPlayer(x, y):
    screen.blit(playerImage, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "live"
    screen.blit(bulletIcon, (x + 16, y + 10))


# Game running
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            # Player Movement
            if event.key == pygame.K_a:
                playerX_change = -player.xSpeed
            if event.key == pygame.K_d:
                playerX_change = player.xSpeed
            if event.key == pygame.K_w:
                playerY_change = -player.ySpeed
            if event.key == pygame.K_s:
                playerY_change = player.ySpeed

            # Bullet Movement
            if bullet_state is "dead":
                if event.key == pygame.K_UP:
                    bulletX = player.playerX
                    direction_shot = "up"
                    fire_bullet(bulletX, bulletY)
                if event.key == pygame.K_DOWN:
                    bulletX = player.playerX
                    direction_shot = "down"
                    fire_bullet(bulletX, bulletY)
                if event.key == pygame.K_LEFT:
                    bulletX = player.playerX
                    direction_shot = "left"
                    fire_bullet(bulletX, bulletY)
                if event.key == pygame.K_RIGHT:
                    bulletX = player.playerX
                    direction_shot = "right"
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0

    player.playerX += playerX_change
    if player.playerX <= 0:
        player.playerX = 0
    elif player.playerX >= 760:
        player.playerX = 760

    player.playerY += playerY_change
    if player.playerY <= 0:
        player.playerY = 0
    elif player.playerY >= 560:
        player.playerY = 560

    # Bullet Moving
    if bulletY <= 0 or bulletY >= 600 or bulletX <= 0 or bulletX >= 800:
        bulletY = player.playerY
        bullet_state = "dead"
    if bullet_state is "live":
        fire_bullet(bulletX, bulletY)
        if direction_shot is "up":
            bulletY -= bulletY_change
        if direction_shot is "down":
            bulletY += bulletY_change
        if direction_shot is "left":
            bulletX -= bulletY_change
        if direction_shot is "right":
            bulletX += bulletY_change

    # check player contacting powerUp
    for powerUp in powerUpsOnScreen:
        if powerUp.x - 24 <= player.playerX <= powerUp.x + 24 and powerUp.y - 24 <= player.playerY <= powerUp.y + 24:
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

    displayPlayer(player.playerX, player.playerY)
    pygame.display.update()
