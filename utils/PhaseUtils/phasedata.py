from utils.Basic.position import Position2D, Position3D
from utils.Basic.velocity import Velocity2D, Velocity3D
from utils.Basic.innerstate import InnerState2D
from utils.Basic.agent import Agent


class PhaseData:

    # TODO:to be finished
    agents: list
    innerstates: list

    def __init__(self,  innerstatenumber=0, agentnumber=0):
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

    def __len__(self):
        return len(self.agents)
