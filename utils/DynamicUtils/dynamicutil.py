from utils.PhaseUtils.phasedata import PhaseData
from utils.PhaseUtils.phaselist import PhaseList
from utils.ParamUtils.situation import Position3D


def randomphase(pl: PhaseList, initsize: Position3D, initcenter: Position3D,
                fromagentno: int, toagentno: int, radius: float):
    # variables

    # agent number of initial phase (whose index is 0)
    maxstep = 100 * len(pl.data[0])
    # is arrangement correct?
    arrangementcorrect = False

    pl.data[0].random(fromno=fromagentno, tono=toagentno + 1)

    for i in range(fromagentno, toagentno + 1):
        while not arrangementcorrect:
            arrangementcorrect = True

    return pl


def initcondition(phasedata: PhaseData, initsize: Position3D,
                  radiusindanger: float):
    randomphase()
