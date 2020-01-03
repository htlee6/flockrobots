# Modified by HoTen Lee

# Import third-party packages required
import datetime
import random
import sys
import csv

# Import self-built packages required
import utils.ConfigUtils.outputfile as outputfile

import utils.ParamUtils.situation as situation
import utils.ParamUtils.flock as flock
import utils.ParamUtils.unit as unit
import utils.ParamUtils.wind as wind

import utils.PhaseUtils.phase as phase
import utils.PhaseUtils.phaselist as phaselist

import utils.StatsticUtils.stat as stat

import utils.DynamicUtils.dynamicutil as dynamicutil

import model.robotmodel as robotmodel
import model.sensormodel as sensormodel

# Functions definition, only used in main.py
pass


def print_help():
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


def initialize(phasetimeline: phaselist.PhaseList, situparam: situation.SituationParam):
    dynamicutil.initcondition(phasedata=phasetimeline[0], situparam=situparam)

    pass


if __name__ == '__main__':

    # variable declaration
    no_agentparams = 0
    no_flockparams = 0
    now = 0.0
    phasetimeline = [phase.PhaseData()]
    conditionreset = [True, True]

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

    OutputPath = input(
        '1. Set output file path (Press Enter to use the default): ')
    if OutputPath == '':
        # aka input nothing/pressed Enter,
        # so we will use the default settings reading from the output config
        # file

        # Output filename
        OutputPath = outputfile.getconfig()

    OutputPath = outputfile.getconfig(item='OutputDirectory') + '/' + \
                 datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '_' + \
                 OutputPath + '.csv'

    # Check optional flag '-i', which defines the input file for situation
    # params
    SituationConfigPath = input(
        '2. Set situation config file path (Press Enter to use the default): ')
    if SituationConfigPath == '':
        # like 'OutputPath', the same we process 'InputPath'

        # Input file path
        SituationConfigPath = 'default'

    '''Create a situation parameter instance'''

    situparam = situation.SituationParam(agentnumber=200)
    # agentnumber = 200 for test
    situparam = situparam.getdefault(filepath=SituationConfigPath)

    if situparam.simlength < 50:
        situparam.simlength = 50

    if situparam.length2store < 10:
        situparam.length2store = 10

    '''Create a flock parameter instance'''

    # define flock param config file
    FlockConfigPath = input(
        "3. Set flock config file path (Press Enter to use the default): ")
    if FlockConfigPath == '':
        FlockConfigPath = 'default'

    flockparam = flock.FlockParam()
    flockparam = flockparam.getdefault(filepath=FlockConfigPath)

    # adjust each parameter in 'flockparam' instance
    flockparam.applyrange()
    # flockparam = flockparam.applyrange()

    '''Create a unit parameter instance'''
    unitparam = unit.UnitParam()

    '''Create a phase data instance'''

    # init a 'PhaseData' instance
    phasenow = phase.PhaseData()

    '''Create a wind parameter instance'''

    # init a 'WindParam' instance
    windparam = wind.WindParam(vx=1.0, vy=2.0)

    '''Several controlling parameters essential in simulation'''

    # define the variable 'stored_time'
    stored_time = float(20.0 + situparam.length2store)
    # Compute 'timestep2store'
    timestep2store = int((stored_time / situparam.deltaT) - 1)

    phasedata, flockparam, situparam, unitparam, windparam = robotmodel.initpreferredvelocity(
        phasedata=phasenow,
        flockparam=flockparam,
        situparam=situparam,
        unitparam=unitparam,
        windparam=windparam)

    noises = sensormodel.initnoise(situparam.agentnumber)
    agentsindanger = [False] * situparam.agentnumber

    statutil = stat.StatUtil()
    statutil.elapsedtime = now * situparam.deltaT - \
                           5.0 - unitparam.communication.tdelay

    # Prepare everything before starting... Are you ready?
    initialize(phasetimeline=phaselist.PhaseList(), situparam=situparam)

    # Info to be printed...
    # agent number
    print('Simulation started with', situparam.agentnumber, 'agent(s). ')
    # size of area
    print('Sizes of the starting area: %fcm * %fcm * %fcm' % situparam.initpos.x, situparam.initpos.y, situparam.initpos.z)

    # The real challenge starts!
    statutil.elapsedtime = (now * situparam.deltaT) - 5.0 - unitparam.communication.tdelay

    statutil.reset()

    # Log printing
    print('[' + datetime.datetime.now().strftime("%H:%M:%S") + '] ' +
          "The result will be written into '" + OutputPath + "'")

    # Create the output file & Write the result into file
    outputfile.generatefile(filepath=OutputPath)

    pass
