from utils.ParamUtils.flockparam import FlockParam
from utils.ParamUtils.situationparam import SituationParam
from utils.ParamUtils.unitparam import UnitParam
from utils.ParamUtils.windparam import WindParam
from utils.PhaseUtils.phasedata import PhaseData


def initpreferredvelocity(phasedata: PhaseData, flockparam: FlockParam,
                          situparam: SituationParam, unitparam: UnitParam, windparam: WindParam):

    preferredvelocity = []

    for i in range(situparam.agentnumber):
        preferredvelocity.append({'vx': 0.0, 'vy': 0.0, 'vz': 0.0})

    return phasedata, flockparam, situparam, unitparam, windparam
    pass
