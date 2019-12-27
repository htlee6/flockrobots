class Velocity3D:

    vx: float
    vy: float
    vz: float

    def __init__(self, vx=0.0, vy=0.0, vz=0.0):
        self.vx = vx
        self.vy = vy
        self.vz = vz


class Velocity2D:

    vx: float
    vy: float

    def __init__(self, vx=0.0, vy=0.0):
        self.vx = vx
        self.vy = vy