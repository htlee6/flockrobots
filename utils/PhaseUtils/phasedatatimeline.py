import utils.PhaseUtils.phasedata as PhaseData


class PhaseTimeline:

    timestep: int
    data: list

    def __init__(self, timestep=1):
        self.timestep = timestep
        self.data = [PhaseData.PhaseData() for i in range(timestep)]
