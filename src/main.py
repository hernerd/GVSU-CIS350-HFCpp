import os.path
import pygame
import random

from powerUp import MovementPowerUp
from classes import Player, Enemy, Obstacle

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
enemyX_change = 0.3
enemyY_change = 0.1

# player group
player_group = pygame.sprite.Group()
player_group.add(player)

# obstacle group
obstacle_group = pygame.sprite.Group()
obstacle_group.add(crate)

# enemy group
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)


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
powerUpsOnScreen = [MovementPowerUp(random.randint(0, 800), random.randint(0, 600))]
powerUpsInEffect = []


def displayPowerUp(powerUp):
    image = pygame.image.load(os.path.join(filepath, powerUp.imagePath))
    screen.blit(image, (powerUp.x, powerUp.y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "live"
    screen.blit(bulletIcon, (x + 16, y + 10))


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
                    bulletX = playerX
                    direction_shot = "up"
                    fire_bullet(bulletX, bulletY)
                if event.key == pygame.K_DOWN:
                    bulletX = playerX
                    direction_shot = "down"
                    fire_bullet(bulletX, bulletY)
                if event.key == pygame.K_LEFT:
                    bulletX = playerX
                    direction_shot = "left"
                    fire_bullet(bulletX, bulletY)
                if event.key == pygame.K_RIGHT:
                    bulletX = playerX
                    direction_shot = "right"
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 760:
        playerX = 760

    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 560:
        playerY = 560

    if pygame.sprite.collide_mask(player, crate):
        if playerX_change < 0:
            while pygame.sprite.collide_mask(player, crate):
                playerX_change = .1
                playerX += playerX_change
                player.pos(playerX, playerY)
            playerX_change = 0
        elif playerX_change > 0:
            while pygame.sprite.collide_mask(player, crate):
                playerX_change = -.1
                playerX += playerX_change
                player.pos(playerX, playerY)
            playerX_change = 0
        if playerY_change < 0:
            while pygame.sprite.collide_mask(player, crate):
                playerY_change = .1
                playerY += playerY_change
                player.pos(playerX, playerY)
            playerY_change = 0
        elif playerY_change > 0:
            while pygame.sprite.collide_mask(player, crate):
                playerY_change = -.1
                playerY += playerY_change
                player.pos(playerX, playerY)
            playerY_change = 0

    player.pos(playerX, playerY)

    # Enemy Movement
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
    elif enemyX >= 760:
        enemyX_change = -0.3

    enemyY += enemyY_change
    if enemyY <= 0:
        enemyY_change = 0.1
    elif enemyY >= 560:
        enemyY_change = -0.1

    enemy.pos(enemyX, enemyY)

    # Checking Enemy Collisions
    if pygame.sprite.collide_mask(player, enemy):
        pygame.QUIT()

    # Bullet Moving
    if bulletY <= 0 or bulletY >= 600 or bulletX <= 0 or bulletX >= 800:
        bulletY = player.y
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
        if powerUp.x - 24 <= playerX <= powerUp.x + 24 and powerUp.y - 24 <= playerY <= powerUp.y + 24:
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
