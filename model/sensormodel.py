from utils.PhaseUtils.phase import Phase
from utils.ParamUtils.unit import UnitParam
from utils.Basic.position import Position3D
from utils.Basic.velocity import Velocity3D
from utils.Basic.acceleration import Acceleration3D
import math


def initnoise(agentnumber: int):
    res = [False] * agentnumber
    return res


def stepGPSnoises(phase: Phase, unitparam: UnitParam):

    for i in range(phase.noagentsinphase()):
        if phase.agents[i].noise is False:
            continue
        GPSposition = phase.getagentcoordinates(agentno=i)
        GPSvelocity = phase.getagentvelocity(agentno=i)

        # Random acceleration vector
        GPSnoise2add = Acceleration3D()
        GPSnoise2add = GPSnoise2add.randguassian()

        # Quadratic potential with friction
        lambda_GPS_XY = 0.1
        lambda_GPS_Z = 0.1
        # TODO: what does '300' stands for?
        D_GPS_XY = math.sqrt(2 * lambda_GPS_XY * unitparam.GPS.sigmax) / 300
        D_GPS_Z = math.sqrt(2 * lambda_GPS_Z * unitparam.GPS.sigmaz) / 300

        # Spring-like force
        # -------------------------------------------------------
        # Let's assume 'force' variable is a 'Velocity3D' object|
        # -------------------------------------------------------
        force = Velocity3D()
        force = force + GPSposition




        # Damping

        return