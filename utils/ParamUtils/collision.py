from typing import Any
import copy as cp

from utils.PhaseUtils.phase import Phase
from utils.Basic.position import Position3D
from utils.Basic.velocity import Velocity3D


class Collision:
    count: int
    tbd: Any

    def __init__(self, count=0):
        self.count = count

    def __str__(self):
        return str(self.count) + ' collisions in all. '


def howmanycollisions(phasenow: Phase, agentsindanger: list,
                      ifcountcollis: bool, dangerradius: float):

    collisions = 0
    ithagentcoord = Position3D()
    jthagentcoord = Position3D()
    prevsituation = False

    if ifcountcollis is True:
        for j in range(phasenow.noagentsinphase()):
            prevsituation = agentsindanger[j]
            agentsindanger[j] = False
            for i in range(j):

                # Doubted, i will never be equal with j
                if i != j:

                    ithagentcoord = phasenow.getagentcoordinates(agentno=i)
                    jthagentcoord = phasenow.getagentcoordinates(agentno=j)

                    if (ithagentcoord - jthagentcoord).length() <= dangerradius:
                        agentsindanger[j] = True
                        agentsindanger[i] = True

            if prevsituation is False and agentsindanger[j] is True:
                collisions = collisions + 1

    return collisions
