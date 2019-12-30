from utils.Basic.velocity import Velocity2D, Velocity3D
from utils.Basic.position import Position2D, Position3D
from utils.ParamUtils.agent import AgentParam


class Agent:

    index: int
    velocity: Velocity3D
    coordinate: Position3D
    agentparam: AgentParam

    def __init__(self, idx, velocity=Velocity3D(), coordinate=Position3D(), agentparam=AgentParam()):
        self.index = idx
        self.velocity = velocity
        self.coordinate = coordinate
        self.agentparam = agentparam

