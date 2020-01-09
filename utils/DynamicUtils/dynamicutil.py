from utils.PhaseUtils.phase import PhaseData
from utils.PhaseUtils.phaselist import PhaseList
from utils.ParamUtils.situation import Position3D
import utils.Basic.velocity as veloctiy
import utils.Basic.position as position
import utils.ParamUtils.situation as situation

'''
def randomphase(pl: PhaseList, initsize: Position3D, initcenter: Position3D,
                fromagentno: int, toagentno: int, radius: float):
    # variables

    # agent number of initial phase (whose index is 0)
    maxstep = 100 * len(pl.data[0])
    # which means -- is arrangement correct?
    arrangementcorrect = False
    #
    stepcount = 0

    pl.data[0].random(fromno=fromagentno, tono=toagentno + 1)

    for i in range(fromagentno, toagentno + 1):
        while not arrangementcorrect:
            arrangementcorrect = True
            random.seed()

            randpos = Position3D(
                x=random.uniform(
                    initcenter.x - initsize.x / 2,
                    initcenter.x + initsize.x / 2),
                y=random.uniform(
                    initcenter.y - initsize.y / 2,
                    initcenter.y + initsize.y / 2),
                z=random.uniform(
                    initcenter.z - initsize.z / 2,
                    initcenter.z + initsize.z / 2))

            for j in range(toagentno):

                if i == j:
                    j = toagentno - 1
                    continue

                posofj = pl.data[0].agents[j].coordinate
                diff = posofj.positiondiff(randpos)

                if diff.length() <= radius:
                    arrangementcorrect = False

            stepcount = stepcount + 1
            if stepcount > maxstep:
                raise TimeoutError(
                    'Stepcount bigger than maxstep, please check! ')

        pl.data[0].agents[i].velocity = veloctiy.Velocity3D()
        pl.data[0].agents[i].coordinates = randpos
        arrangementcorrect = False

    return pl
'''


def initcondition(phasedata: PhaseData, situparam: situation.SituationParam):
    phasedata.randomphase(initsize=situparam.initpos,
                          initcenter=Position3D(x=0.0, y=0.0, z=0.0),
                          fromagentno=0, toagentno=phasedata.noagentsinphase(),
                          radius=situparam.dangerousradius)

    return phasedata
    pass


