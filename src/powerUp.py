from datetime import datetime, timedelta


class PowerUp:
    def __init__(self, x, y, expirationTime, imagePath):
        self.x = x
        self.y = y
        self.expirationTime = expirationTime
        self.imagePath = imagePath

    def applyPlayerEffect(self, player):
        raise NotImplementedError("Subclass must implement effect application")

    def removePlayerEffectIfExpired(self, player):
        raise NotImplementedError("Subclass must implement effect removal if an expiration time is set")


class MovementPowerUp(PowerUp):

    def __init__(self, x, y):
        super(MovementPowerUp, self).__init__(
            x=x,
            y=y,
            expirationTime=datetime.now() + timedelta(0, 10),
            imagePath="assets/running-shoe.png"
        )

    def applyPlayerEffect(self, player):
        player.xSpeed *= 10
        player.ySpeed *= 10

    def removePlayerEffectIfExpired(self, player):
        if datetime.now() > self.expirationTime:
            player.xSpeed /= 10
            player.ySpeed /= 10
            return True
        return False
