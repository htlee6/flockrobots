from utils.Basic.velocity import Velocity2D, Velocity3D
from utils.Basic.position import Position2D, Position3D
from utils.ParamUtils.unit import UnitParam


class Agent:

    index: int
    velocity: Velocity3D
    coordinate: Position3D
    agentparam: UnitParam

    def __init__(self, idx, velocity=Velocity3D(), coordinate=Position3D(), agentparam=UnitParam()):
        self.index = idx
        self.velocity = velocity
        self.coordinate = coordinate
        self.agentparam = agentparam

