from utils.Basic.position import Position2D, Position3D
from utils.Basic.velocity import Velocity2D, Velocity3D
from utils.Basic.innerstate import InnerState2D


class PhaseData:

    # TODO:to be finished
    coordinates: Position2D
    velocity: Velocity2D
    innerstates: InnerState2D
    realIDs: list
    innerstatenumber: int
    agentnumber: int

    def __init__(self, coordinates=Position3D(), velocity=Velocity3D(),
                 innerstates=InnerState2D, realIDs=[], innerstatenumber=0, agentnumber=0):
        self.coordinates = coordinates
        self.velocity = velocity
        self.innerstates = innerstates
        self.realIDs = realIDs
        self.innerstatenumber = innerstatenumber
        self.agentnumber = agentnumber

    def func1(self):
        pass


