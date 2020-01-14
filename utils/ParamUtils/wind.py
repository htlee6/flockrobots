from utils.ParamUtils.unit import Wind
import math


class WindParam(Wind):

    # TODO: why the wind has only a 2-dimensional velocity? What about 3D?

    def __init__(self, vx: float, vy: float):
        self.vx = vx
        self.vy = vy
        self.angle = math.atan(vy/vx)

    def func1(self):
        pass
