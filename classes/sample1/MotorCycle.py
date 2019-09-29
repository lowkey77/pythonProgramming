# Motorcycle
class Motorcycle:
    def __init__(self, speed):
        self.speed = speed

    def increaseSpeed(self, speedUp):
        self.speed += speedUp

    def decreaseSpeed(self, slowDown):
        if self.speed - slowDown < 0:
            self.speed = 0
        else:
            self.speed -= slowDown

    def setSpeed(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def print(self):
        print(f"Motorcycle Name: {self.getName()}\nMotorcycle speed: {self.getSpeed()}")
