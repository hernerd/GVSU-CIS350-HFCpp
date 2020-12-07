import time

import pygame

from classes import Player, Enemy
from powerUp import HealthPowerUp, MovementPowerUp, DropKey


def initialize_display():
    return pygame.display.set_mode((800, 600))


def test_health_powerUp():
    screen = initialize_display()

    player = Player(0, 0)
    player.health = 90

    health = HealthPowerUp(5, 5)
    health.applyPlayerEffect(player)

    assert player.health == 100


def test_movement_powerUp():
    screen = initialize_display()

    player = Player(0, 0)

    assert player.xSpeed == 5 and player.ySpeed == 5

    speed = MovementPowerUp(5, 5)
    speed.applyPlayerEffect(player)

    assert player.xSpeed == 7.5 and player.ySpeed == 7.5

    time.sleep(5)

    assert not speed.removePlayerEffectIfExpired(player)

    time.sleep(5)

    assert speed.removePlayerEffectIfExpired(player)
    assert player.xSpeed == 5 and player.ySpeed == 5


def test_drop_key():
    screen = initialize_display()

    enemy = Enemy(50,50)
    enemy.health = 0
    key = DropKey(50,50)

    player = Player(100, 100)
    assert key.unlocked == False

