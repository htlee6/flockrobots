class Position3D:

    x: float
    y: float
    z: float

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z


class Position2D:

    x: float
    y: float

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y