import utils.PhaseUtils.phasedata as phasedata


class PhaseList:

    timestep: int
    data: list

    def __init__(self, timestep=1):
        self.timestep = timestep
        self.data = [phasedata.PhaseData() for i in range(timestep)]
