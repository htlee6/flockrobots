from typing import Any

from utils.StatsticUtils.stat import StatUtil
from utils.ParamUtils.situation import SituationParam
from utils.ParamUtils.flock import FlockParam
from utils.ParamUtils.wind import WindParam

from utils.StatsticUtils.stat import SaveMode, StatUtil


class Playground:

    situationparam: SituationParam
    flockparam: FlockParam
    windparam: WindParam
    statisticutil: StatUtil
    result: Any

    def __init__(self, situparam: SituationParam, flockparam: FlockParam, windparam: WindParam, statutil: StatUtil, result: Any):

        self.situationparam = situparam
        self.flockparam = flockparam
        self.windparam = windparam
        self.statisticutil = statutil
        self.result = result
        pass

    def gamestart(self, timestep2store: int):
        # local variable definition
        now = 0

        while self.statutil.elapsedtime < self.situationparam.simlength:
            if now < timestep2store:

                pass
            else:
                pass
            if outputmode.savecollisions is SaveMode.STEADYSTAT and statutil.elapsedtime < situparam.startofsteadystate:
                collisions = 0
            pass
        pass


