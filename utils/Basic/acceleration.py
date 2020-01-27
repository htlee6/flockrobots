import random


class Acceleration2D():
    ax: float
    ay: float

    def __init__(self, vx=0.0, vy=0.0):
        self.vx = 0.0
        self.vy = 0.0

    def __str__(self):
        return 'Acceleration (' + str(self.ax) + ', ' + str(self.ay) + ')'


class Acceleration3D(Acceleration2D):
    az: float

    def __init__(self, az=0.0):
        self.az = az

    def __str__(self):
        return 'Acceleration (' + str(self.ax) + ', ' + str(self.ay) + ', ' + str(self.az) + ')'

    def randguassian(self):
        random.seed()
        self.ax = random.gauss(mu=0, sigma=1)
        self.ay = random.gauss(mu=0, sigma=1)
        self.az = random.gauss(mu=0, sigma=1)

