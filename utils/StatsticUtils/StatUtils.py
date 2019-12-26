from enum import Enum


class SaveMode(Enum):
    FALSE = 0
    TIMELINE = 1
    STAT = 2
    STEADYSTAT = 3


class StatUtil:
    elapsedtime: float
    startofsteadystate: float
    savemode: SaveMode

    def __init__(self, elpasedtime=0.0, startofsteadystate=0.0, savemode=SaveMode.FALSE):
        self.elapsedtime = elpasedtime
        self.startofsteadystate = startofsteadystate
        self.savemode = savemode
        pass

    def func1(self):
        pass
