from utils.ParamUtils.FlockParam import FlockParam
from utils.ParamUtils.SituationParam import SituationParam
from utils.ParamUtils.UnitParam import UnitParam
from utils.ParamUtils.WindParam import WindParam
from utils.PhaseUtils.PhaseData import PhaseData


def initpreferredvelocity(phasedata: PhaseData, flockparam: FlockParam,
                          situparam: SituationParam, unitparam: UnitParam, windparam: WindParam):

    preferredvelocity = []

    for i in range(situparam.agentnumber):
        preferredvelocity.append({'vx': 0.0, 'vy': 0.0, 'vz': 0.0})

    return phasedata, flockparam, situparam, unitparam, windparam
    pass
