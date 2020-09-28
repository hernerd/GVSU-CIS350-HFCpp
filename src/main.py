import pygame
import os.path
filepath = os.path.dirname(__file__)

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Dungeon Crawler")


#Player
playerImage  = pygame.image.load(os.path.join(filepath, "assets/player.png"))
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

#Bullet
#   Dead - bullet is not shot yet
#   Live - bullet is in motion
bulletIcon = pygame.image.load(os.path.join(filepath,"assets/projectile.png"))
bulletX = 370
bulletY = 480
bulletX_change = 0
bulletY_change = .5
bullet_state = "dead"
direction_shot = ""

def player(x, y):
    screen.blit(playerImage, (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "live"
    screen. blit(bulletIcon, (x + 16,y + 10))
#Game running
running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            #Player Movement
            if event.key == pygame.K_a:
                playerX_change = -0.1
            if event.key == pygame.K_d:
                playerX_change = 0.1
            if event.key == pygame.K_w:
                playerY_change = -0.1
            if event.key == pygame.K_s:
                playerY_change = 0.1

            #Bullet Movement
            if bullet_state is "dead" :
                if event.key == pygame.K_UP:
                    bulletX = playerX
                    direction_shot = "up"
                    fire_bullet(bulletX,bulletY)
                if event.key == pygame.K_DOWN:
                    bulletX = playerX
                    direction_shot = "down"
                    fire_bullet(bulletX,bulletY)
                if event.key == pygame.K_LEFT:
                    bulletX = playerX
                    direction_shot = "left"
                    fire_bullet(bulletX,bulletY)
                if event.key == pygame.K_RIGHT:
                    bulletX = playerX
                    direction_shot = "right"
                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0
    
    
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >=760:
        playerX = 760

    #Bullet Moving
    if bulletY <= 0 or bulletY >= 600 or bulletX <= 0 or bulletX >= 800:
        bulletY = playerY
        bullet_state = "dead"
    if bullet_state is "live":
        fire_bullet(bulletX, bulletY)
        if direction_shot is "up" :
            bulletY -= bulletY_change
        if direction_shot is "down" :
            bulletY += bulletY_change
        if direction_shot is "left" :
            bulletX -= bulletY_change
        if direction_shot is "right" :
            bulletX += bulletY_change

    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >=560:
        playerY = 560
        
    player(playerX, playerY)
    pygame.display.update()