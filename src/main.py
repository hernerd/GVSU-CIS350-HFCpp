import os.path
import pygame
import random
import math
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
crates = []
crate1 = Obstacle(crateX, crateY)
x = 300
y = 480
# crate2 = Obstacle(300, 300)

# Enemy
num_enemies = 5
enemies = []

for i in range(num_enemies):
    enemyX = random.randint(0, 800)
    enemyY = random.randint(0, 300)
    enemy = Enemy(enemyX, enemyY)
    enemy.x_change = 0.3
    enemy.y_change = 0.1
    enemies.append(enemy)

# player group
player_group = pygame.sprite.Group()
player_group.add(player)

# obstacle group
obstacle_group = pygame.sprite.Group()
obstacle_group.add(crate1)
for i in range(6):
    crate = Obstacle(x, y)
    crates.append(crate)
    obstacle_group.add(crate)
    y -= 16

# enemy group
enemy_group = pygame.sprite.Group()
for e in enemies:
    enemy_group.add(e)

# mobile group (sprites that move)
mobile_group = pygame.sprite.Group()
mobile_group.add(player)
for e in enemies:
    mobile_group.add(e)


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
            self.y_change = 10
            self.x_change = 10


# Bullet
bullets = []
direction_shot = ""
bullet_change = 5
bullet_group = pygame.sprite.Group()

#Bullet Delay
count = 0
bulletDelay = 25
firstShot = True

# Power-ups
powerUpsOnScreen = [MovementPowerUp(random.randint(0, 775), random.randint(0, 575)),
                    MovementPowerUp(random.randint(0, 775), random.randint(0, 575))]
powerUpsInEffect = []


def displayPowerUp(powerUp):
    image = pygame.image.load(os.path.join(filepath, powerUp.imagePath))
    screen.blit(image, (powerUp.x, powerUp.y))


def fire_bullet(x, y):
    screen.blit(bullet.image, (x-7, y-5))

def updateUI():
    # PowerUps in effect
    numPowerUps = len(powerUpsInEffect)
    if numPowerUps > 0:
        pygame.draw.rect(screen, (0, 102, 102), [797 - (numPowerUps * 40), 557, (numPowerUps * 40), 40])

        index = 0
        for currentPowerUp in powerUpsInEffect:
            image = pygame.image.load(os.path.join(filepath, currentPowerUp.imagePath))
            screen.blit(image, (789 - (40 * index) - 24, 565))
            index += 1
            
background = pygame.image.load(os.path.join(filepath, "assets/bg_0.png"))
upper_bound = 70
lower_bound = 525
left_bound = 70
right_bound = 730

FPS = 60
clock = pygame.time.Clock()
# Game running
running = True
while running:
    # screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    clock.tick(FPS)

    count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            player.moving = True
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
            if count > bulletDelay or firstShot:
                count = 0
                firstShot = False
                if event.key == pygame.K_UP:
                    bullet = Bullet(player.x, player.y)
                    bullet.direction = "up"
                    bullet.x = player.x
                    bullet.y = player.y
                    bullets.append(bullet)
                    bullet_group.add(bullet)
                    # fire_bullet(bullet.x, bullet.y)
                if event.key == pygame.K_DOWN:
                    bullet = Bullet(player.x, player.y)
                    bullet.direction = "down"
                    bullet.x = player.x
                    bullet.y = player.y
                    bullets.append(bullet)
                    bullet_group.add(bullet)
                    # fire_bullet(bullet.x, bullet.y)
                if event.key == pygame.K_LEFT:
                    bullet = Bullet(player.x, player.y)
                    bullet.direction = "left"
                    bullet.x = player.x
                    bullet.y = player.y
                    bullets.append(bullet)
                    bullet_group.add(bullet)
                    # fire_bullet(bullet.x, bullet.y)
                if event.key == pygame.K_RIGHT:
                    bullet = Bullet(player.x, player.y)
                    bullet.direction = "right"
                    bullet.x = player.x
                    bullet.y = player.y
                    bullets.append(bullet)
                    bullet_group.add(bullet)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.x_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player.y_change = 0
            if player.x_change == 0 and player.y_change == 0:
                player.moving = False

    player.x += player.x_change
    if player.x <= left_bound:
        player.x = left_bound
    elif player.x >= right_bound:
        player.x = right_bound

    player.y += player.y_change
    if player.y <= upper_bound:
        player.y = upper_bound
    elif player.y >= lower_bound:
        player.y = lower_bound

    # Enemy Movement
    # for e in enemy_group:
    #     e.x += e.x_change
    #     if e.x <= 0:
    #         e.x_change = 7
    #     elif e.x >= 760:
    #         e.x_change = -7

    #     e.y += e.y_change
    #     if e.y <= 0:
    #         e.y_change = 7
    #     elif e.y >= 560:
    #         e.y_change = -7

    for e in enemy_group:
        dx, dy = player.x - e.x, player.y - e.y
        dist = math.hypot(dx, dy)
        dx, dy = dx/dist, dy/dist
        e.x += dx
        e.y += dy

    # Bullet Moving
    for b in bullets:
        # fire_bullet(b.x, b.y)
        if b.direction == "up":
            b.y -= bullet_change
        if b.direction == "down":
            b.y += bullet_change
        if b.direction == "left":
            b.x -= bullet_change
        if b.direction == "right":
            b.x += bullet_change
        b.pos(b.x, b.y)
        if b.y <= upper_bound or b.y >= lower_bound or b.x <= left_bound or b.x >= right_bound:
            bullets.remove(b)
            bullet_group.remove(b)

    for mob in mobile_group:
        for obstacle in obstacle_group:
            check_object_collision(mob, obstacle)
        mob.pos(mob.x, mob.y)

    # Checking Enemy Collisions
    for e in enemy_group:
        if pygame.sprite.collide_mask(player, e):
            player.health -= e.damage
            if player.health <= 0:
                running = False

    # problem child
    for e in enemy_group:
        for b in bullet_group:
            if pygame.sprite.collide_rect(b, e):
                e.health -= b.damage
                if e.health <= 0:
                    enemy_group.remove(e)
                    enemies.remove(e)
                bullet_group.remove(b)
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
    bullet_group.draw(screen)
    updateUI()
    pygame.display.update()
