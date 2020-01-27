from typing import Any

import utils.ParamUtils.collision as coli

from utils.StatsticUtils.stat import StatUtil
from utils.PhaseUtils.phaselist import PhaseList
from utils.ParamUtils.situation import SituationParam
from utils.ParamUtils.flock import FlockParam
from utils.ParamUtils.wind import WindParam
from utils.ParamUtils.unit import UnitParam
from utils.ParamUtils.collision import Collision

from utils.StatsticUtils.stat import SaveMode, StatUtil


class Playground:

    phasetimeline: PhaseList
    situationparam: SituationParam
    flockparam: FlockParam
    unitparam: UnitParam
    windparam: WindParam
    statisticutil: StatUtil
    result: Any
    collision: Collision

    def __init__(self, situparam: SituationParam, flockparam: FlockParam, unitparam: UnitParam,
                 windparam: WindParam, statutil: StatUtil, result: Any):

        self.situationparam = situparam
        self.flockparam = flockparam
        self.unitparam = unitparam
        self.windparam = windparam
        self.statisticutil = statutil
        self.result = result

        self.collision = Collision()
        pass

    # Step positions and velocities and copy realIDs???
    def step(self, timesteplooped: int, ifcountcollisions: bool):
        delaystep = float(
            self.unitparam.communication.tdelay /
            self.situationparam.deltaT)
        phasenow = self.phasetimeline[timesteplooped]
        phasedelayed = self.phasetimeline.data[timesteplooped - int(delaystep)]

        if ifcountcollisions is True:
            self.collision.count = self.collision.count + coli.howmanycollisions(
                self.phasetimeline[timesteplooped],
                agentsindanger=[],
                ifcountcollis=ifcountcollisions,
                dangerradius=self.situationparam.dangerradius)
            # TODO: store collisions in an array or something...
            pass

        # Step coordinates
        for j in range(self.situationparam.agentnumber):
            velo = phasenow.getagentvelocity(agentno=j)
            coordstostep = phasenow.getagentcoordinates(agentno=j)

            # Assume we use 3D coordinates and velocity here
            coordstostep.x = velo.vx * self.situationparam.deltaT
            coordstostep.y = velo.vy * self.situationparam.deltaT
            coordstostep.z = velo.vz * self.situationparam.deltaT

            phasenow.editagentcoordinate(agentidx=j, coord=coordstostep)

        # Step GPS coordinates and velocities (in every 't_gps'-th second)
        if timesteplooped % int(self.unitparam.GPS.tGPS/self.situationparam.deltaT) == 0:
            
        # for j in range(self.situationparam.agentnumber):



    def start(self, now: int, timestep2store: int):
        # local variable definition

        while self.statisticutil.elapsedtime < self.situationparam.simlength:
            if now < timestep2store:

                pass
            else:
                pass
            # if outputmode.savecollisions is SaveMode.STEADYSTAT and statutil.elapsedtime < situparam.startofsteadystate:
                # collisions = 0
            pass
        pass
