from utils.ParamUtils.flock import FlockParam
from utils.ParamUtils.situation import SituationParam
from utils.ParamUtils.agent import UnitParam
from utils.ParamUtils.wind import WindParam
from utils.PhaseUtils.phasedata import PhaseData


def initpreferredvelocity(phasedata: PhaseData, flockparam: FlockParam,
                          situparam: SituationParam, unitparam: UnitParam, windparam: WindParam):

    preferredvelocity = []

    for i in range(situparam.agentnumber):
        preferredvelocity.append({'vx': 0.0, 'vy': 0.0, 'vz': 0.0})

    return phasedata, flockparam, situparam, unitparam, windparam
    pass
