class WindParam:

    vx: float
    vy: float

    # TODO: why the wind has only a 2-dimensional velocity? What about 3D?

    def __init__(self, vx: float, vy: float):
        self.vx = vx
        self.vy = vy

    def func1(self):
        pass