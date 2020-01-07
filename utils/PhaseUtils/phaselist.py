import utils.PhaseUtils.phase as phasedata
from utils.PhaseUtils.phase import PhaseData
from utils.Basic.velocity import Velocity3D


class PhaseList:
    timestep: int
    data: list

    def __init__(self, timestep: int, **phaseinitparam):
        self.timestep = timestep
        if not phaseinitparam:
            self.data = [PhaseData().getdefault() for i in range(timestep)]
        else:
            self.data = [PhaseData(phaseinitparam['innerstatenumber'], phaseinitparam['agentnumber']) for i in
                         range(timestep)]

    def __len__(self):
        return self.timestep

    def randomphaselist(self):
        pass

    def wait(self, time2wait: float, h: float):

        for i in range(1, int((1 + time2wait) / h)):
            for j in range(self.data[0].noagentsinphase()):

                self.data[i].agents[j].coordinate = self.data[i-1].agents[j].coordinate
                self.data[i].agents[j].velocity = Velocity3D(vx=0.0, vy=0.0, vz=0.0)

                for k in range(self.data[0].noinnerstatesinphase()):
                    self.data[i].agents[j].innerstate[k] = self.data[i-1].agents[j].innerstate[k]

