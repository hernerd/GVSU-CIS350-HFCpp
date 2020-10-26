import math
import os.path
import pygame
import random
from powerUp import MovementPowerUp, HealthPowerUp, PortalPowerUp
from classes import Player, Enemy, Obstacle, Bullet, Trap, Fire, Tank, Ninja, Door

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
spikes = Trap(80, 80, "spikes")
x = 300
y = 480

# Enemy
num_enemies = 3
enemies = []

for i in range(num_enemies):
    enemyX = random.randint(0, 800)
    enemyY = random.randint(0, 300)
    enemy = Enemy(enemyX, enemyY)
    enemy.x_change = 0.3
    enemy.y_change = 0.1
    enemies.append(enemy)

num_tanks = 2

for i in range(num_tanks):
    tankX = random.randint(0, 800)
    tankY = random.randint(0, 300)
    tank = Tank(tankX, tankY)
    tank.x_change = 0.2
    tank.y_change = 0.05
    enemies.append(tank)

num_ninjas = 2

for i in range(num_ninjas):
    ninjaX = random.randint(0, 800)
    ninjaY = random.randint(0, 300)
    ninja = Ninja(ninjaX, ninjaY)
    ninja.x_change = 0.4
    ninja.y_change = 0.2
    enemies.append(ninja)

# player group
player_group = pygame.sprite.Group()
player_group.add(player)

# obstacle group
obstacle_group = pygame.sprite.Group()
obstacle_group.add(crate1)
obstacle_group.add(spikes)
for i in range(6):
    crate = Obstacle(x, y)
    crates.append(crate)
    obstacle_group.add(crate)
    y -= 16
    
door = Door(342, 60)
door_group = pygame.sprite.Group()
door_group.add(door)
dframe = 0    
    
# trap group
traps = pygame.sprite.Group()
traps.add(spikes)

# lingering image group
lingering_image = pygame.sprite.Group()

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
    if pygame.sprite.collide_mask(self, obstacle) and obstacle.name == "obstacle":
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
        if self.name == "tank":
            self.y_change = 10
            self.x_change = 10
        if self.name == "ninja":
            self.y_change = 10
            self.x_change = 10

def check_enemy_collision(self, enemy):
    if pygame.sprite.collide_mask(self, enemy):
        if self.x_change < 0:
            while pygame.sprite.collide_mask(self, enemy):
                self.x_change = .1
                self.x += self.x_change
                self.pos(self.x, self.y)
            self.x_change = 0
        elif self.x_change > 0:
            while pygame.sprite.collide_mask(self, enemy):
                self.x_change = -.1
                self.x += self.x_change
                self.pos(self.x, self.y)
            self.x_change = 0
        if self.y_change < 0:
            while pygame.sprite.collide_mask(self, enemy):
                self.y_change = .1
                self.y += self.y_change
                self.pos(self.x, self.y)
            self.y_change = 0
        elif self.y_change > 0:
            while pygame.sprite.collide_mask(self, enemy):
                self.y_change = -.1
                self.y += self.y_change
                self.pos(self.x, self.y)
            self.y_change = 0
        if self.name == "enemy":
            self.y_change = 10
            self.x_change = 10
        if self.name == "tank":
            self.y_change = 10
            self.x_change = 10
        if self.name == "ninja":
            self.y_change = 10
            self.x_change = 10


# Bullet
bullets = []
direction_shot = ""
bullet_change = 5
bullet_group = pygame.sprite.Group()
bullet_type = "bullet"

#Bullet Delay
bulletDelay = 25
count = bulletDelay

# Power-ups
powerUpsOnScreen = [MovementPowerUp(random.randint(70, 730), random.randint(70, 525)),
                    MovementPowerUp(random.randint(70, 730), random.randint(70, 525)),
                    HealthPowerUp(random.randint(70, 730), random.randint(70, 525)),
                    HealthPowerUp(random.randint(70, 730), random.randint(70, 525)),
                    HealthPowerUp(random.randint(70, 730), random.randint(70, 525)),
                    PortalPowerUp(random.randint(70, 730), random.randint(70, 525))]
powerUpsInEffect = []


def displayPowerUp(powerUp):
    image = pygame.image.load(os.path.join(filepath, powerUp.imagePath))
    screen.blit(image, (powerUp.x, powerUp.y))


def fire_bullet(x, y):
    screen.blit(bullet.image, (x-7, y-5))

def updateUI():
    # current health
    numHearts = math.ceil(player.health / 10.0)
    pygame.draw.rect(screen, (92, 64, 51), [3, 557, numHearts * 40, 40])

    for index in range(0, numHearts):
        heartImage = pygame.image.load(os.path.join(filepath, "assets/heart.png"))
        screen.blit(heartImage, (11 + (40 * index), 565))

    # PowerUps in effect
    numPowerUps = len(powerUpsInEffect)
    if numPowerUps > 0:
        pygame.draw.rect(screen, (92, 64, 51), [797 - (numPowerUps * 40), 557, (numPowerUps * 40), 40])

        index = 0
        for currentPowerUp in powerUpsInEffect:
            image = pygame.image.load(os.path.join(filepath, currentPowerUp.imagePath))
            screen.blit(image, (789 - (40 * index) - 24, 565))
            index += 1
         
def start():
    begin = True
    while begin:
        screen.blit(starting_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                begin = False
        pygame.display.update()        
        
background = pygame.image.load(os.path.join(filepath, "assets/bg_0.png"))
upper_bound = 70
lower_bound = 525
left_bound = 70
right_bound = 730

FPS = 60
clock = pygame.time.Clock()
# Game running
start()
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

            #Change Bullet Type
            if event.key == pygame.K_b:
                if bullet_type == "bullet":
                    bullet_type = "fire"
                elif bullet_type == "fire":
                    bullet_type = "bullet"
            # Bullet Movement
            if count > bulletDelay or bullet_type == "fire":
                count = 0
                if bullet_type == "fire":
                    bullet = Fire(player.x, player.y)
                else:
                    bullet = Bullet(player.x, player.y)
                bullet.x = player.x
                bullet.y = player.y
                if event.key == pygame.K_UP:
                    bullet.direction = "up"
                    bullets.append(bullet)
                    bullet_group.add(bullet)
                if event.key == pygame.K_DOWN:
                    bullet.direction = "down"
                    bullets.append(bullet)
                    bullet_group.add(bullet)
                if event.key == pygame.K_LEFT:
                    bullet.direction = "left"
                    bullets.append(bullet)
                    bullet_group.add(bullet)
                if event.key == pygame.K_RIGHT:
                    bullet.direction = "right"
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
        if e.name == "enemy":
            e.x += dx
            e.y += dy
        if e.name == "tank":
            e.x += dx * 0.5
            e.y += dy * 0.5
        if e.name == "ninja":
            e.x += dx * 1.5
            e.y += dy * 1.5
            tp = random.randint(0, 500)
            if tp % 500 == 0:
                e.x = random.randint(70, 730)
                e.y = random.randint(70, 525)
            

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
            
    for b in bullet_group:
        for o in obstacle_group:
            if pygame.sprite.collide_rect(b, o):
                bullet_group.remove(b)
                lingering_image.add(b)
                b.direction = ""
                b.moving = False
                b.damage = 0
                
    for e1 in enemy_group:
        for e2 in enemy_group:
            if e1 != e2:
                check_enemy_collision(e1, e2)
                e1.pos(e1.x, e1.y)
                e2.pos(e2.x, e2.y)
    for mob in mobile_group:
        for obstacle in obstacle_group:
            check_object_collision(mob, obstacle)
            if pygame.sprite.collide_mask(mob, obstacle) and obstacle.type == "trap":
                mob.health -= obstacle.damage
                if mob.health <= 0:
                    mobile_group.remove(mob)
                    if mob.name == "player":
                        player_group.remove(mob)
                    elif mob.name == "enemy":
                        enemy_group.remove(mob)
                    elif mob.name == "tank":
                        enemy_group.remove(mob)
                    elif mob.name == "ninja":
                        enemy_group.remove(mob)                       
        mob.pos(mob.x, mob.y)

    # Checking Enemy Collisions
    for e in enemy_group:
        if pygame.sprite.collide_mask(player, e):
            player.health -= e.damage
            if player.health <= 0:
                running = False
                
    # lingering images
    lingering_count = 0
    for image in lingering_image:
        if lingering_count < 6 and len(lingering_image) > 6:
            lingering_image.remove(image)
        lingering_count += 1
        
    # Killing Enemies 
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
            
    screen.blit(door.images[dframe], (342, 0))
    if len(enemy_group) == 0 and dframe == 0:
        screen.blit(door.images[dframe], (342, 0))
        dframe += 1
    elif dframe == 1:
        screen.blit(door.images[dframe], (342, 0))
        dframe += 1
    elif dframe == 2:
        screen.blit(door.images[dframe], (342, 0))

    enemy_group.draw(screen)
    obstacle_group.draw(screen)
    player_group.draw(screen)
    bullet_group.draw(screen)
    updateUI()
    pygame.display.update()
