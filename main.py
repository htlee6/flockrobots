# Modified by HoTen Lee

# Import built-in packages required
import datetime
import sys

import model.robotmodel as robm
import model.sensormodel as sensm
import utils.ComputeUtils.playground as plg
# Import self-built packages required
import utils.ConfigUtils.outputfile as opfile
import utils.DynamicUtils.dynamicutil as dyut
import utils.ParamUtils.flock as flk
import utils.ParamUtils.situation as situ
import utils.ParamUtils.unit as unit
import utils.ParamUtils.wind as wind
import utils.PhaseUtils.phase as phase
import utils.PhaseUtils.phaselist as phasel
import utils.StatsticUtils.stat as stat
from utils.Basic.velocity import Velocity3D
from utils.ConfigUtils.outputfile import SaveMode
from utils.ParamUtils.flock import FlockParam
from utils.StatsticUtils.stat import StatUtil
from utils.ParamUtils.unit import UnitParam

# Functions definition, used in main.py only


def pathinput(hint: str, default_return: str):
    """
    A simple path controlling function for easier file path input.

    Args:
        hint: Hint when inputting.
        default_return: When input is nothing (or pressed Enter when inputting), the default result str to be returned.

    Returns: The expected file path, as a str type.

    """
    tmp_input = input(hint)
    if tmp_input is '':
        return default_return
    else:
        return tmp_input


def print_help():
    """

    Help information to be printed.

    """
    print("This is robotsim created at ELTE Department of Biological Physics.\n"
          "\n"
          "Command line options:\n"
          "\n"
          "-c FILE     define color configuration file\n"
          "-f FILE     define flockingparams file\n"
          "-h, --help  print help and exit\n"
          "-i FILE     define initparams file\n"
          "-novis      do not open GUI\n"
          "-o PATH     define output directory\n"
          "-a FILE     define agentparams file\n"
          )


def initialize(p_phasetimeline: phasel.PhaseList,
               p_situparam: situ.SituationParam,
               p_flockparam: FlockParam,
               p_statutil: StatUtil,
               p_unitparam: UnitParam,
               p_starttime: int):
    """

    Args:
        p_phasetimeline: the PhaseTimeLine to use and to store
        p_situparam: the SituationParam to use, involved with computing
        p_flockparam:
        p_statutil:
        p_unitparam:
        p_starttime:

    Returns: A lot of initialized computational parameters and controlling parameters.

    """
    p_flockparam.refresh()

    p_phasetimeline.data[0] = dyut.initcondition(
        phase=p_phasetimeline.data[0], situparam=p_situparam)

    # initializephase() function - Finished on 13/01/2020
    p_phasetimeline.data[0], res_arenas, res_obstacles = phase.initializephase(phase=p_phasetimeline.data[0],
                                                                               flockparam=p_flockparam,
                                                                               situparam=p_situparam)

    init_starttime = p_starttime + \
        round((5.0 + unitparam.communication.tdelay) / p_situparam.deltaT)
    p_phasetimeline.wait(
        time2wait=(5 + unitparam.communication.tdelay),
        h=p_situparam.deltaT)
    res_timebeforeflock = 10.0 + p_unitparam.communication.tdelay

    # Match the steady state timestamps in the 2 corresponding structures.
    p_statutil.startofsteadystate = p_situparam.startofsteadystate

    return p_phasetimeline, p_situparam, p_flockparam, \
        p_statutil, init_starttime, res_arenas, res_obstacles, res_timebeforeflock


if __name__ == '__main__':

    # variable declaration
    no_agentparams = 0
    no_flockparams = 0
    now = 0.0
    timestep2store = 0
    conditionreset = [True, True]
    accelerations = [Velocity3D()]
    collisions = 0

    # search for some useful parameters in sys.argv
    for i in sys.argv:
        if i == '-h' or i == '--help':
            print_help()
            sys.exit(0)
        if i == '-u':
            no_agentparams = no_agentparams + 1
        if i == '-f':
            no_flockparams = no_flockparams + 1
        if no_agentparams > 1 or no_flockparams > 1:
            print('More than 1 agent/flock param files. Check twice! ')
            sys.exit(0)

    OutputPath = pathinput(hint='1. Set output file path (Press Enter to use the default): ',
                           default_return=opfile.getconfig())

    OutputPath = opfile.getconfig(item='OutputDirectory') + '/' + \
        datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '_' + OutputPath + '.csv'

    # Check optional flag '-i', which defines the input file for situation
    # params
    SituationConfigPath = pathinput(
        hint='2. Set situation config file path (Press Enter to use the default): ',
        default_return='default')

    '''Create a situation parameter instance'''
    situparam = situ.SituationParam(agentnumber=200)
    # agentnumber = 200 for test
    situparam = situparam.getdefault(filepath=SituationConfigPath)

    # some limitations on member variables of object --'situparam'
    if situparam.simlength < 50:
        situparam.simlength = 50

    if situparam.length2store < 10:
        situparam.length2store = 10

    '''Create a flock parameter instance'''
    # define flock param config file
    FlockConfigPath = pathinput(
        hint="3. Set flock config file path (Press Enter to use the default): ",
        default_return='default')

    flockparam = flk.FlockParam()
    flockparam = flockparam.getdefault(filepath=FlockConfigPath)

    # adjust each parameter in 'flockparam' instance
    flockparam.applyrange()
    # flockparam = flockparam.applyrange()

    # init a 'UnitParam' instance
    unitparam = unit.UnitParam()

    # init a 'PhaseData' instance
    phasenow = phase.Phase().getdefault()

    # init a 'WindParam' instance
    windparam = wind.WindParam(vx=1.0, vy=2.0)

    '''Several controlling parameters essential in simulation'''
    # define the variable 'stored_time'
    stored_time = float(20.0 + situparam.length2store)
    # Compute 'timestep2store'
    timestep2store = int((stored_time / situparam.deltaT) - 1)

    phasenow, preferredvelocity = robm.initpreferredvelocity(
        p_phase=phasenow, p_situparam=situparam)

    # noise is a bool type member variable stored in the Agent object.
    # noises = sensm.initnoise(situparam.agentnumber)
    agentsindanger = [False] * situparam.agentnumber

    phasetimeline = phasel.PhaseList(timestep=timestep2store)

    statutil = stat.StatUtil()

    # Prepare everything before starting... Are you ready?
    phasetimeline, situparam, flockparam, statutil, now, arenas, obstacles, timebeforeflock \
        = initialize(p_phasetimeline=phasetimeline, p_situparam=situparam,
                     p_flockparam=flockparam, p_statutil=statutil, p_unitparam=unitparam, p_starttime=int(now))

    statutil.elapsedtime = now * situparam.deltaT - \
        5.0 - unitparam.communication.tdelay

    # Log printing
    # agent number
    print('[' + datetime.datetime.now().strftime("%H:%M:%S") + '] ' +
          'Simulation started with', situparam.agentnumber, 'agent(s). ')
    # size of area
    print('[' + datetime.datetime.now().strftime("%H:%M:%S") + '] ' + 'Sizes of the starting area: ' + str(situparam.initpos.x) + 'cm*' + str(situparam.initpos.y) + 'cm*' + str(
        situparam.initpos.z) + 'cm')

    # The real challenge starts!
    statutil.elapsedtime = (now * situparam.deltaT) - \
        5.0 - unitparam.communication.tdelay

    statutil.reset()

    outputmode = opfile.OutputMode()

    #
    statutil.savemode = outputmode.savemodelspecifics

    # Create a lot of files to store the simulation data
    currentdir = opfile.createdatastorefiles(
        outputmode, symbol=datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))

    # Imagine 'accelerations' as a numberofagents*3 matrix (3 dims, x, y, z)
    for i in range(situparam.agentnumber - 1):
        accelerations.append(Velocity3D())

    if outputmode.savemodelspecifics is not SaveMode.FALSE:
        statutil.initmodelspecificstatus(currentdirectory=currentdir)
    flockparam.refresh()

    pg = plg.Playground(
        situparam=situparam,
        flockparam=flockparam,
        windparam=windparam,
        statutil=statutil,
        result=[])
    pg.start(timestep2store=timestep2store)

    # Log printing
    # Output file directory
    print('[' + datetime.datetime.now().strftime("%H:%M:%S") + '] ' +
          "The result will be written into '" + OutputPath + "'")

    # Create the output file & Write the result into file
    opfile.generatefile(filepath=OutputPath)

    pass
