from utils.ParamUtils.flock import FlockParam
from utils.ParamUtils.situation import SituationParam
from utils.ParamUtils.unit import UnitParam
from utils.ParamUtils.wind import WindParam
from utils.PhaseUtils.phase import Phase

from utils.Basic.velocity import Velocity3D


def initpreferredvelocity(p_phase: Phase, p_situparam: SituationParam):
    """Calculate a preferred velocity for the agents in the flock.

    
    Args:
        p_phase (Phase): A phase object.
        p_flockparam (FlockParam): The actual flock parameter object.
        p_situparam (SituationParam): The actual situation parameter object.
        p_unitparam (UnitParam): The actual unit parameter object.
        p_windparam (WindParam): The actual wind parameter object.

    Returns:
        phase: the calculated phase.
        flockparam: never used. 
        situparam: never used.



    """
    preferredvelocity = []

    for i in range(p_situparam.agentnumber):
        preferredvelocity.append(Velocity3D(vx=0.0, vy=0.0, vz=0.0))
        p_phase.agents[i].noise = True

    return p_phase, preferredvelocity
    pass
