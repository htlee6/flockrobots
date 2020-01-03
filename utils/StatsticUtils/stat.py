from enum import Enum


class SaveMode(Enum):
    FALSE = 0
    TIMELINE = 1
    STAT = 2
    STEADYSTAT = 3


# to avoid naming conflicts, using 'cSum' instead of 'Sum' to name the class which
# is used to process sum statistics
class cSum:
    # 4 digits
    acceleration: list
    # 4 digits
    correlation: list
    # 4 digits
    distancebetweenunits: list
    # 3 digits
    distancebetweenneighbors: list
    # 1 digits
    collisionration: float
    # 8 digits
    velocity: list
    # 3 digits
    CoM: list

    def __init__(self, acceleration=list[0.0, 0.0, 0.0, 0.0], correlation=list[0.0, 0.0, 0.0, 0.0],
                 distancebetweenunits=list[0.0, 0.0, 0.0, 0.0], distancebetweenneighbors=[0.0, 0.0, 0.0],
                 collisionratio=0.0, velocity=list[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], CoM=list[0.0, 0.0, 0.0]):
        self.acceleration = acceleration
        self.correlation = correlation
        self.distancebetweenunits = distancebetweenunits
        self.distancebetweenneighbors = distancebetweenneighbors
        self.collisionration = collisionratio
        self.velocity = velocity
        self.CoM = CoM
        pass


class StandardDeviation:

    # digits of the member variables are the same as the 'cSum' class
    acceleration: list
    correlation: list
    distancebetweenunits: list
    distancebetweenneighbors: list
    collisionration: float
    velocity: list
    CoM: list

    def __init__(self, acceleration=list[0.0, 0.0, 0.0, 0.0], correlation=list[0.0, 0.0, 0.0, 0.0],
                 distancebetweenunits=list[0.0, 0.0, 0.0, 0.0], distancebetweenneighbors=[ 0.0, 0.0, 0.0],
                 collisionratio=0.0, velocity=list[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], CoM=list[0.0, 0.0, 0.0]):
        self.acceleration = acceleration
        self.correlation = correlation
        self.distancebetweenunits = distancebetweenunits
        self.distancebetweenneighbors = distancebetweenneighbors
        self.collisionration = collisionratio
        self.velocity = velocity
        self.CoM = CoM
        pass


class StatUtil:
    elapsedtime: float
    startofsteadystate: float
    savemode: SaveMode
    csum: cSum
    stdev: StandardDeviation

    def __init__(self, elpasedtime=0.0, startofsteadystate=0.0,
                 savemode=SaveMode.FALSE, csum=cSum(), stdev=StandardDeviation()):
        self.elapsedtime = elpasedtime
        self.startofsteadystate = startofsteadystate
        self.savemode = savemode
        self.csum = csum
        self.stdev = stdev
        pass

    def reset(self):

        pass
