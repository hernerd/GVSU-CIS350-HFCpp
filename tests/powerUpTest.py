import time
import pygame

from src.powerUp import HealthPowerUp, MovementPowerUp, PortalPowerUp, FirePowerUp
from src.classes import Player


screen = pygame.display.set_mode((800, 600))


def test_health_powerUp():
    player = Player(0, 0)
    player.health = 90

    health = HealthPowerUp(5, 5)
    health.applyPlayerEffect(player)

    assert player.health == 100


def test_movement_powerUp():
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


def test_portal_powerUp():
    player = Player(0, 0)

    portal = PortalPowerUp(5, 5)
    portal.applyPlayerEffect(player)

    assert player.x is not 0 and player.y is not 0


def test_fire_powerUp():
    player = Player(0, 0)

    assert player.bullet == "bullet"

    fire = FirePowerUp(5, 5)
    fire.applyPlayerEffect(player)

    assert player.bullet == "fire"

    time.sleep(5)

    assert not fire.removePlayerEffectIfExpired(player)

    time.sleep(5)

    assert fire.removePlayerEffectIfExpired(player)
    assert player.bullet == "bullet"
