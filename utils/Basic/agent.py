from utils.Basic.velocity import Velocity2D, Velocity3D
from utils.Basic.position import Position2D, Position3D
from utils.ParamUtils.unit import UnitParam


class Agent:

    index: int
    velocity: Velocity3D
    coordinate: Position3D
    agentparam: UnitParam
    innerstatenumber: int
    innerstate: list

    def __init__(self, idx, velocity=Velocity3D(), coordinate=Position3D(), agentparam=UnitParam(), noinnerstate=0):
        self.index = idx
        self.velocity = velocity
        self.coordinate = coordinate
        self.agentparam = agentparam
        self.innerstatenumber = noinnerstate
        self.innerstate = [0.0 for i in range(noinnerstate)]

