from utils.Basic.position import Position2D, Position3D
from utils.Basic.velocity import Velocity2D, Velocity3D
from utils.Basic.innerstate import InnerState2D
from utils.Basic.agent import Agent
import random


class PhaseData:

    # TODO:to be finished
    agents: list
    innerstates: list

    def __init__(self, innerstatenumber=0, agentnumber=0):
        # self.innerstates = [defaultinnerstate for i in range(self.innerstatenumber)]
        self.innerstates = [InnerState2D() for i in range(innerstatenumber)]

        # self.agents = [defalutagent.__init__(idx=i) for i in range(self.agentnumber)]
        self.agents = [Agent(idx=i) for i in range(agentnumber)]

    def getdefault(self):
        self.innerstates = [InnerState2D() for i in range(5)]
        self.agents = [Agent(idx=i) for i in range(10)]
        return self

    def random(self, fromno: int, tono: int):
        for i in range(fromno, tono):

            # you can change the value filled here
            self.agents[i].coordinate = Position3D(2e22, 2e22, 2e22)
            # TODO: to debug, set to 1.0, 2.0, 3.0; should be all 0.0
            self.agents[i].velocity = Velocity3D(1.0, 2.0, 3.0)

    def randomphase(self, initsize: Position3D, initcenter: Position3D,
                    fromagentno: int, toagentno: int, radius: float):

        # variables

        # agent number of initial phase (whose index is 0)
        maxstep = 100 * len(self)
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

    def __len__(self):
        return len(self.agents)
