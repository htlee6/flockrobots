from utils.Basic.Position import Position2D
from utils.Basic.Velocity import Velocity2D
from utils.Basic.InnerState import InnerState2D


class PhaseData:

    # TODO:to be finished
    coordinates: Position2D
    velocity: Velocity2D
    innerstates: InnerState2D
    realIDs: list
    innerstatenumber: int
    agentnumber: int

    def __init__(self, coordinates=Position2D(), velocity=Velocity2D,
                 innerstates=InnerState2D, realIDs=[], innerstatenumber=0, agentnumber=0):
        self.coordinates = coordinates
        self.velocity = velocity
        self.innerstates = innerstates
        self.realIDs = realIDs
        self.innerstatenumber = innerstatenumber
        self.agentnumber = agentnumber

    def func1(self):
        pass
