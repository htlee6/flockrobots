from enum import Enum


class SaveMode(Enum):
    FALSE = 0
    TIMELINE = 1
    STAT = 2
    STEADYSTAT = 3


# to avoid naming conflicts, using 'cSum' instead of 'Sum' to name the class which
# is used to process sum statistics


class Item:
    # 4 digits
    acceleration: list
    # 4 digits
    correlation: list
    # 4 digits
    distancebetweenunits: list
    # 3 digits
    distancebetweenneighbors: list
    # 1 digits
    collisionratio: float
    # 8 digits
    velocity: list
    # 3 digits
    CoM: list

    def __init__(self, acceleration=[0.0, 0.0, 0.0, 0.0],
                 correlation=[0.0, 0.0, 0.0, 0.0],
                 distancebetweenunits=[0.0, 0.0, 0.0, 0.0],
                 distancebetweenneighbors=[0.0, 0.0, 0.0],
                 collisionratio=0.0,
                 velocity=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                 CoM=[0.0, 0.0, 0.0]):

        self.acceleration = acceleration
        self.correlation = correlation
        self.distancebetweenunits = distancebetweenunits
        self.distancebetweenneighbors = distancebetweenneighbors
        self.collisionratio = collisionratio
        self.velocity = velocity
        self.CoM = CoM
        pass

    def reset(self):
        self.acceleration = [0.0, 0.0, 0.0, 0.0]
        self.correlation = [0.0, 0.0, 0.0, 0.0]
        self.distancebetweenunits = [0.0, 0.0, 0.0, 0.0]
        self.distancebetweenneighbors = [0.0, 0.0, 0.0]
        self.collisionratio = 0.0
        self.velocity = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.CoM = [0.0, 0.0, 0.0]


class StatUtil:
    elapsedtime: float
    startofsteadystate: float
    savemode: SaveMode
    sum: Item
    stdev: Item

    def __init__(self, elpasedtime=0.0, startofsteadystate=0.0,
                 savemode=SaveMode.FALSE, sum=Item(), stdev=Item()):
        self.elapsedtime = elpasedtime
        self.startofsteadystate = startofsteadystate
        self.savemode = savemode
        self.sum = sum
        self.stdev = stdev
        pass

    def reset(self):
        self.sum.reset()
        self.stdev.reset()
        pass

    def initmodelspecificstatus(self):
        if self.savemode is SaveMode.STAT or self.savemode is not SaveMode.STEADYSTAT:
            

        pass
