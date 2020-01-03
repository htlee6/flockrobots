import utils.PhaseUtils.phase as phasedata
from utils.PhaseUtils.phase import PhaseData


class PhaseList:

    timestep: int
    data: list

    def __init__(self, timestep: int, **phaseinitparam):
        self.timestep = timestep
        if not phaseinitparam:
            self.data = [phasedata.PhaseData().getdefault() for i in range(timestep)]
        else:
            self.data = [phasedata.PhaseData(phaseinitparam['innerstatenumber'], phaseinitparam['agentnumber']) for i in range(timestep)]

    def randomphaselist(self):
        pass

    def __len__(self):
        return self.timestep

