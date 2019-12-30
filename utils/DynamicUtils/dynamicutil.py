from utils.PhaseUtils.phasedata import PhaseData
from utils.PhaseUtils.phaselist import PhaseList
from utils.ParamUtils.situation import Position3D


def randomizephase(phasearray: PhaseList, initsize: Position3D,
                   initcenter: Position3D, fromagentno: int, toagentno: int, radius: float):

    res_phase = PhaseList()

    # agent number of initial phase
    maxstep = 100 * phasearray.data[0].agentnumber
    

    for i in range(fromagentno, toagentno):
        pass

    return res_phase


def initcondition(phasedata: PhaseData, initsize: Position3D,
                  radiusindanger: float):
    randomizephase()
