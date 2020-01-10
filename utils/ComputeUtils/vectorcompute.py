from utils.Basic.position import Position3D, Position2D
from utils.Basic.velocity import Velocity3D, Velocity2D
import math


def euclideandistance(pos):
    if type(pos) is Position3D:
        return math.sqrt(pow(pos.x, 2) + pow(pos.y, 2) + pow(pos.z, 2))
    if type(pos) is Position2D:
        return math.sqrt(pow(pos.x, 2) + pow(pos.y, 2))
