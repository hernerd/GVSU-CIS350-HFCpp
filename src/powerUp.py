from datetime import datetime, timedelta
import random


class PowerUp:
    def __init__(self, x, y, imagePath, isInventory = False):
        self.isInventory = isInventory
        self.x = x
        self.y = y
        self.imagePath = imagePath

    def applyPlayerEffect(self, player):
        raise NotImplementedError("Subclass must implement effect application")

    def removePlayerEffectIfExpired(self, player):
        raise NotImplementedError("Subclass must implement effect removal if an expiration time is set")


class HealthPowerUp(PowerUp):
    def __init__(self, x, y):
        super(HealthPowerUp, self).__init__(
            x=x,
            y=y,
            imagePath="assets/heart.png"
        )

    def applyPlayerEffect(self, player):
        self.expirationTime = datetime.now()

        healthGained = random.randint(1, 3) * 10
        if player.health < (100 - healthGained):
            player.health = player.health + healthGained
        else:
            player.health = 100

    def removePlayerEffectIfExpired(self, player):
        return True


class MovementPowerUp(PowerUp):

    def __init__(self, x, y):
        super(MovementPowerUp, self).__init__(
            x=x,
            y=y,
            imagePath="assets/running-shoe.png",
            isInventory=True
        )

    def applyPlayerEffect(self, player):
        self.expirationTime = datetime.now() + timedelta(0, 10)
        
        player.xSpeed *= 1.5
        player.ySpeed *= 1.5

    def removePlayerEffectIfExpired(self, player):
        if datetime.now() > self.expirationTime:
            player.xSpeed /= 1.5
            player.ySpeed /= 1.5
            return True
        return False


class PortalPowerUp(PowerUp):

    def __init__(self, x, y):
        super(PortalPowerUp, self).__init__(
            x=x,
            y=y,
            imagePath="assets/portal.png",
            isInventory=True
        )

    def applyPlayerEffect(self, player):
        self.expirationTime = datetime.now()

        player.x = random.randint(70, 730)
        player.y = random.randint(70, 525)

    def removePlayerEffectIfExpired(self, player):
        return True

class FirePowerUp(PowerUp):

    def __init__(self, x, y):
        super(FirePowerUp, self).__init__(
            x=x,
            y=y,
            imagePath="assets/fire_power.png",
            isInventory=True
        )

    def applyPlayerEffect(self, player):
        self.expirationTime = datetime.now() + timedelta(0, 10)
        player.bullet = "fire"

    def removePlayerEffectIfExpired(self, player):
        if datetime.now() > self.expirationTime:
            player.bullet = "bullet"
            return True
        return False
