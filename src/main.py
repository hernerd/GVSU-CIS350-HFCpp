import math
import os.path
import pygame
import random
from powerUp import MovementPowerUp, HealthPowerUp, PortalPowerUp, FirePowerUp
from classes import Player, Enemy, Obstacle, Bullet, Trap, Fire, Tank, Ninja, Door
from rooms import Room

filepath = os.path.dirname(__file__)

pygame.init()

screen = pygame.display.set_mode((800, 600), flags=pygame.SCALED | pygame.RESIZABLE)


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
enemies = []
"""
num_enemies = 5
enemies = []

for i in range(num_enemies):
    enemyX = random.randint(0, 800)
    enemyY = random.randint(0, 600)
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
"""
# player group
player_group = pygame.sprite.Group()
player_group.add(player)

# obstacle group
"""
spikes = Trap(80, 80, "spikes")
for i in range(6):
    crate = Obstacle(x, y)
    crates.append(crate)
    obstacle_group.add(crate)
    y -= 16

traps = pygame.sprite.Group()
traps.add(spikes)
obstacle_group.add(spikes)
"""
door = Door(400, 30)
door_group = pygame.sprite.Group()
door_group.add(door)
dframe = 0

# lingering image group
lingering_image = pygame.sprite.Group()

# enemy group
"""
# enemy group
enemy_group = pygame.sprite.Group()
for e in enemies:
    enemy_group.add(e)
"""
enemy_group = pygame.sprite.Group()

# mobile group (sprites that move)
mobile_group = pygame.sprite.Group()
mobile_group.add(player)
"""
for e in enemies:
    mobile_group.add(e)
"""


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
            
            
def collide(self, obst):
    if pygame.sprite.collide_mask(self, obst):
        x_offset = obst.x - self.x
        y_offset = obst.y - self.y
        if self.dirX != "":
            if x_offset < 0:
                self.x_change = .1
            if x_offset > 0:
                self.x_change = -.1
        if self.dirY != "":
            if y_offset < 0:
                self.y_change = .1
            if y_offset > 0:
                self.y_change = -.1
        while pygame.sprite.collide_mask(self, obst):
            self.x += self.x_change
            self.y += self.y_change
            self.pos(self.x, self.y)
        self.x_change = 0
        self.y_change = 0


# Bullet
bullets = []
direction_shot = ""
bullet_change = 5
bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
enemy_bullets = []

#Bullet Delay
bulletDelay = 25
count = bulletDelay

# Power-ups
powerUpsOnScreen = [MovementPowerUp(random.randint(70, 730), random.randint(70, 525)),
                    MovementPowerUp(random.randint(70, 730), random.randint(70, 525)),
                    HealthPowerUp(random.randint(70, 730), random.randint(70, 525)),
                    HealthPowerUp(random.randint(70, 730), random.randint(70, 525)),
                    HealthPowerUp(random.randint(70, 730), random.randint(70, 525)),
                    PortalPowerUp(random.randint(70, 730), random.randint(70, 525)),
                    FirePowerUp(random.randint(70, 730), random.randint(70, 525)),
                    FirePowerUp(random.randint(70, 730), random.randint(70, 525)),]
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
     
def make_room(lvl):
    r = Room(lvl)
    return r


starting_image = pygame.image.load(os.path.join(filepath, "assets/bg_s0.png"))    
background = pygame.image.load(os.path.join(filepath, "assets/bg_0.png"))
upper_bound = 54
lower_bound = 525
left_bound = 70
right_bound = 730

coolDownTime = 0
FPS = 60
clock = pygame.time.Clock()
level = 0
room = None
rooms = []
roomIndex = 0
backdoor = None
# Game running
start()
running = True
while running:
    clock.tick(FPS)

    if (coolDownTime > 0):
        coolDownTime = coolDownTime - 1
    # screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    if room is None:
        room = make_room(level)
        rooms.append(room)
        enemy_group = room.enemy_group
        for e in enemy_group:
            if e.name == "boss":
                boss_group.add(e)
                enemy_group.remove(e)

        obstacle_group = room.obstacle_group
        for e in enemy_group:
            enemies.append(e)
            mobile_group.add(e)
        player.x = playerX
        player.y = playerY
    if room.status == "complete" and pygame.sprite.collide_mask(player, door):
        if room.forward:
            room = room.forward
        else:
            roomIndex += 1
            room = make_room(level)
            rooms.append(room)
            rooms[roomIndex].backward = rooms[roomIndex-1]
            rooms[roomIndex-1].forward = rooms[roomIndex]
            backdoor = Door(400, 570)
            backdoor.image = pygame.image.load(os.path.join(filepath, "assets/door clone.png"))
            door_group.add(backdoor)
        enemy_group = room.enemy_group
        obstacle_group = room.obstacle_group
        player.x = playerX
        player.y = playerY
        if len(lingering_image) > 0:
            lingering_image.empty()
            lingering_count = 0
        # print(level)
        for e in enemy_group:
            enemies.append(e)
            mobile_group.add(e)
    if room.backward and pygame.sprite.collide_mask(player, backdoor):
        room = room.backward
        enemy_group = room.enemy_group
        obstacle_group = room.obstacle_group
        player.x = 400
        player.y = upper_bound + 30

    count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            player.moving = True
            # Player Movement
            if event.key == pygame.K_a:
                player.x_change = -player.xSpeed
                player.moving = True
                player.dirX = "left"
                player.facing = "left"
            if event.key == pygame.K_d:
                player.x_change = player.xSpeed
                player.moving = True
                player.dirX = "right"
                player.facing = "right"
            if event.key == pygame.K_w:
                player.y_change = -player.ySpeed
                player.moving = True
                player.dirY = "up"
            if event.key == pygame.K_s:
                player.y_change = player.ySpeed
                player.moving = True
                player.dirY = "down"


            # Bullet Movement
            if count > bulletDelay or player.bullet == "fire":
                count = 0
                if player.bullet == "fire":
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
                
    if player.x_change != 0 and player.y_change == 0:
        player.dirY = ""
    elif player.x_change == 0 and player.y_change != 0:
        player.dirX = ""

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

    for e in enemy_group:
        dx, dy = player.x - e.x, player.y - e.y
        dist = math.hypot(dx, dy)
        dx, dy = dx/dist, dy/dist
        if dx > 0:
            e.dirX = "right"
        if dx < 0:
            e.dirX = "left"
        if dy > 0:
            e.dirY = "down"
        if dy < 0:
            e.dirY = "up"
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
        if e.name == "ranger":
             e.x += dx
             e.y += dy
             shoot = random.randint(0, 500)
             if shoot % 500 == 0:
                    enemy_shot = Bullet(e.x, e.y)
                    enemy_shot.x = e.x
                    enemy_shot.y = e.y
                    enemy_shot.direction = e.dirX
                    enemy_bullets.append(enemy_shot)
                    enemy_bullet_group.add(enemy_shot)


    for e in boss_group:
        shoot = random.randint(0, 500)
        if shoot % 500 == 0:
            enemy_up = Bullet(e.x, e.y)
            enemy_up.x = e.x
            enemy_up.y = e.y
            enemy_up.direction = "up"
            enemy_bullets.append(enemy_up)
            enemy_bullet_group.add(enemy_up)
            enemy_down = Bullet(e.x, e.y)
            enemy_down.x = e.x
            enemy_down.y = e.y
            enemy_down.direction = "down"
            enemy_bullets.append(enemy_down)
            enemy_bullet_group.add(enemy_down)
            enemy_right = Bullet(e.x, e.y)
            enemy_right.x = e.x
            enemy_right.y = e.y
            enemy_right.direction = "right"
            enemy_bullets.append(enemy_right)
            enemy_bullet_group.add(enemy_right)
            enemy_left = Bullet(e.x, e.y)
            enemy_left.x = e.x
            enemy_left.y = e.y
            enemy_left.direction = "left"
            enemy_bullets.append(enemy_left)
            enemy_bullet_group.add(enemy_left)

    for b in enemy_bullets:
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
            enemy_bullets.remove(b)
            enemy_bullet_group.remove(b)
            
    for b in enemy_bullet_group:
         if pygame.sprite.collide_rect(b, player):
             player.health -= b.damage
             enemy_bullets.remove(b)
             enemy_bullet_group.remove(b)
             if player.health <= 0:
                 running = False

                
    # Bullet Moving
    for b in bullets:
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
                if b.name != "fire":
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
            # check_object_collision(mob, obstacle)
            collide(mob, obstacle)
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
        if pygame.sprite.collide_mask(player, e) and coolDownTime == 0:
            coolDownTime = 20
            player.health -= e.damage
            if player.health <= 0:
                running = False
    
    for e in boss_group:
        if pygame.sprite.collide_mask(player, e) and coolDownTime == 0:
            coolDownTime = 20
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
            if pygame.sprite.collide_mask(b, e):
                e.health -= b.damage
                if e.health <= 0:
                    enemy_group.remove(e)
                    enemies.remove(e)
                bullet_group.remove(b)
                bullets.remove(b)
    
    for e in boss_group:
        for b in bullet_group:
            if pygame.sprite.collide_mask(b, e):
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
            
    if len(enemy_group) == 0 and dframe < 2:
        door.updateImage()
        dframe += 1
            
    if dframe == 2 and pygame.sprite.collide_mask(player, door):
        room.status = "complete"
        level += 1
        dframe = 0
        door.reset_image()
        player.x = playerX
        player.y = playerY

    enemy_group.draw(screen)
    obstacle_group.draw(screen)
    door_group.draw(screen)
    player_group.draw(screen)
    bullet_group.draw(screen)
    enemy_bullet_group.draw(screen)
    boss_group.draw(screen)
    updateUI()
    pygame.display.update()
