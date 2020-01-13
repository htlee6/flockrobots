import random

from utils.Basic.agent import Agent
from utils.Basic.position import Position3D
from utils.Basic.velocity import Velocity3D
from utils.ParamUtils.flock import FlockParam
from utils.ParamUtils.situation import SituationParam
from utils.ParamUtils.arena import Arena, ArenaList
from utils.ParamUtils.obstacle import Obstacle, ObstacleList


class Phase:

    # TODO:to be finished
    agents: list

    def __init__(self, innerstatenumber=0, agentnumber=0):
        # self.innerstates = [defaultinnerstate for i in range(self.innerstatenumber)]
        # self.innerstates = [InnerState3D() for i in range(innerstatenumber)]

        # self.agents = [defalutagent.__init__(idx=i) for i in range(self.agentnumber)]
        self.agents = [Agent(idx=i) for i in range(agentnumber)]

    def getdefault(self):
        # TODO: need to read from configuration files
        # self.innerstates = [InnerState2D() for i in range(5)]
        self.agents = [Agent(idx=i) for i in range(10)]

    def getagentcoordinates(self, agentno: int):
        return self.agents[agentno].coordinate

    def editagentcoordinate(self, coord: Position3D, agentidx: int):
        self.agents[agentidx].coordinate = coord

    def editagentvelocity(self, velo: Velocity3D, agentidx: int):
        self.agents[agentidx].velocity = velo

    def random(self, fromno: int, tono: int):
        for i in range(fromno, tono):

            # you can change the value filled here
            self.agents[i].coordinate = Position3D(2e22, 2e22, 2e22)
            # TODO: to debug, set to 1.0, 2.0, 3.0; should be all 0.0
            self.agents[i].velocity = Velocity3D(1.0, 2.0, 3.0)

    def randomphase(self, initsize: Position3D, initcenter: Position3D,
                    fromagentno: int, toagentno: int, radius: float):
        """

        :param initsize:
        :param initcenter:
        :param fromagentno:
        :param toagentno:
        :param radius:
        :return:
        """
        # variables

        # agent number of initial phase (whose index is 0)
        maxstep = 100 * self.noagentsinphase()
        # which means -- is arrangement correct?
        arrangementcorrect = False
        #
        stepcount = 0

        self.random(fromno=fromagentno, tono=toagentno + 1)

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

                    posofj = self.agents[j].coordinate
                    diff = posofj.positiondiff(randpos)

                    if diff.length() <= radius:
                        arrangementcorrect = False

                stepcount = stepcount + 1
                if stepcount > maxstep:
                    raise TimeoutError(
                        'Stepcount bigger than maxstep, please check! ')

            self.agents[i].velocity = Velocity3D()
            self.agents[i].coordinate = randpos
            arrangementcorrect = False

    def noagentsinphase(self):
        return len(self.agents)

    def noinnerstatesinphase(self):
        return self.agents[0].innerstatenumber

    def placeagentsonXYplane(self, xsize: float, ysize: float, xcenter: float,
                             ycenter: float, zcenter: float, fromagentno: int, toagentno: int, radius: float):
        arrangementcorrect = False
        stepcount = 0
        maxstep = 100 * self.noagentsinphase()
        for i in range(fromagentno, toagentno):
            while arrangementcorrect is False:
                arrangementcorrect = True
                agentcoordinate = Position3D(x=xcenter + random.uniform(-xsize / 2, xsize / 2),
                                             y=ycenter +
                                             random.uniform(-ysize / 2,
                                                            ysize / 2),
                                             z=zcenter)
            for j in range(self.noagentsinphase()):
                if i == j:
                    j = toagentno - 1
                    continue
                tmpcoordinate = self.getagentcoordinates(agentno=j)
                diff = tmpcoordinate - agentcoordinate

                if diff.length() <= radius:
                    arrangementcorrect = False

            self.editagentcoordinate(coord=agentcoordinate, agentidx=i)
            self.editagentvelocity(velo=Velocity3D(0.0, 0.0, 0.0), agentidx=i)
            arrangementcorrect = False


def initializephase(phase: Phase, flockparam: FlockParam,
                    situparam: SituationParam):
    # finished part
    arenas = ArenaList(maxarenacount=10, content=[])
    arenas.readfromfile(
        toreadlist=[
            'triangle',
            'pentagon1',
            'pentagon2',
            'octagon'])
    obstacles = ObstacleList(maxobs=10, content=[])
    obstacles.readfromfile(
        toreadlist=[
            'leftrectangle',
            'rightrectangle',
            'pentagon1'])
    phase.placeagentsonXYplane(
        xsize=2 * flockparam.arena_radius,
        ysize=2 * flockparam.arena_radius,
        xcenter=flockparam.arena_centerx,
        ycenter=flockparam.arena_centery,
        zcenter=0,
        fromagentno=0,
        toagentno=phase.noagentsinphase(),
        radius=max(
            situparam.dangerousradius,
            flockparam.v_flock * 2))
    if flockparam.dimofsimulation == 2:
        for m in range(phase.noagentsinphase()):
            phase.agents[m].coordinate.z = 0.0
            phase.agents[m].veloctiy.vz = 0.0
    pass
    # TODO not finished yet

    return phase, arenas, obstacles
