# Modified by HoTen Lee

# Import built-in packages required
import datetime
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

from utils.Basic.velocity import Velocity3D, Velocity2D
from utils.ConfigUtils.outputfile import SaveMode

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


def initialize(phasetimeline: phaselist.PhaseList,
               situparam: situation.SituationParam):
    dynamicutil.initcondition(phasedata=phasetimeline[0], situparam=situparam)

    pass


def ifcreatefiles(oputmode: outputfile.OutputMode):
    if oputmode.savetrajectories:
        with open('output/posandvel.csv', 'w+') as f_outphase:
            csv_outphase = csv.writer(f_outphase)
            csv_outphase.writerow(['time(s)',
                                   'index',
                                   'x(cm)',
                                   'y(cm)',
                                   'z(cm)',
                                   'Vx(cm/s)',
                                   'Vy(cm/s)',
                                   'Vz(cm/s)'])

    if oputmode.saveinnerstates:
        with open('output/posandvel.csv', 'w+') as f_outinnerstates:
            csv_outinnterstates = csv.writer(f_outphase)
            # TODO: used 'NumberOfInnerstates' here
            csv_outinnterstates.writerow(['time(s)'])

    if oputmode.savecollisions is not SaveMode.FALSE:
        with open('output/collisions.csv', 'w+') as f_collisions:
            csv_collision = csv.writer(f_collisions)
            csv_collision.writerow(['time(s)',
                                    'number_of_collisions'])

    if oputmode.savedistancebetweenunits is not SaveMode.FALSE:
        with open('output/distance_between_units.csv', 'w+') as f_distbetweenunits:
            csv_distbetweenunits = csv.writer(f_distbetweenunits)
            csv_distbetweenunits.writerow(['time(s)',
                                           'avg_dist_between_units(cm)',
                                           'stdev_dist_between_units(cm)',
                                           'min_dist_between_units(cm)',
                                           'max_dist_between_units(cm)'])

        # This part in original version is redundant. I don't need this in my version.
        # It is doing the same thing with the outer 'if' code block.
        ''' 
        if (oputmode.savedistancebetweenunits is SaveMode.STAT) \
                or (oputmode.savedistancebetweenunits is SaveMode.STEADYSTAT):
            with open('output/distance_between_units_stdev.csv', 'w+') as f_distbetweenunitsStdev:
                csv_distbetwunitsStdev = csv.writer(f_distbetweenunitsStdev)
                csv_distbetwunitsStdev.writerow(['time(s)',
                                                 'avg_dist_between_units(cm)',
                                                 'stdev_dist_between_units(cm)',
                                                 'min_dist_between_units(cm)',
                                                 'max_dist_between_units(cm)'])
        '''

    if oputmode.savedistancebetweenneighbors is not SaveMode.FALSE:
        with open('output/dist_between_neighbours.csv', 'w+') as f_distbetweenneighbours:
            csv_distbetweenneighbours = csv.writer(f_distbetweenneighbours)
            csv_distbetweenneighbours.writerow(['time(s)',
                                                'avg_dist_between_neighbours(cm)',
                                                'stdev_dist_between_neighbours(cm)',
                                                'max_dist_between_neighbours(cm)',
                                                'min_dist_between_neighbours(cm)'])

        if (oputmode.savedistancebetweenneighbors is SaveMode.STAT) \
                or (oputmode.savedistancebetweenneighbors is SaveMode.STEADYSTAT):
            pass

        pass

    if oputmode.savevelocity is not SaveMode.FALSE:
        with open('output/velocity.csv', 'w+') as f_velocity:
            csv_velocity = csv.writer(f_velocity)
            csv_velocity.writerow(['time(s)',
                                   'avg_velocity(cm/s)',
                                   'stdev_velocity(cm/s)',
                                   'min_velocity(cm/s)',
                                   'max_velocity(cm/s)'])
        if (oputmode.savevelocity is SaveMode.STAT) \
                or (oputmode.savevelocity is SaveMode.STEADYSTAT):
            pass
        pass

    if oputmode.saveCoM is not SaveMode.FALSE:
        with open('output/CoM.csv', 'w+') as f_CoM:
            csv_CoM = csv.writer(f_CoM)
            csv_CoM.writerow(['time(s)',
                              'CoM_x(cm)',
                              'CoM_y(cm)',
                              'CoM_z(cm)'])
        if (oputmode.saveCoM is SaveMode.STAT) \
                or (oputmode.saveCoM is SaveMode.STEADYSTAT):
            pass
        pass

    if oputmode.savecorrelation is not SaveMode.FALSE:
        with open('output/correlation.csv', 'w+') as f_correlation:
            csv_correlation = csv.writer(f_correlation)
            csv_correlation.writerow(['time(s)',
                                      'avg_velocity_correlation',
                                      'stdev_normalized_velocity_scalar_product',
                                      'min_normalized_velocity_scalar_product',
                                      'max_normalized_velocity_scalar_product'])
        if (oputmode.savecorrelation is SaveMode.STAT) \
                or (oputmode.savecorrelation is SaveMode.STEADYSTAT):
            pass
        pass

    if oputmode.savecollisionratio is not SaveMode.FALSE:
        with open('output/collision_ratio.csv', 'w+') as f_collisionratio:
            csv_collisionration = csv.writer(f_collisionratio)
            csv_collisionration.writerow(['time',
                                          'ratio_of_collision'])
        if (oputmode.savecollisionratio is SaveMode.STAT) \
                or (oputmode.savecollisionratio is SaveMode.STEADYSTAT):
            pass
        pass

    if oputmode.saveacceleration is not SaveMode.FALSE:
        with open('output/acceleration.csv') as f_acceleration:
            csv_acceleration = csv.writer(f_acceleration)
            csv_acceleration.writerow(['time(s)',
                                       'avg_acceleration(cm/s2)',
                                       'stdev_acceleration(cm/s2)',
                                       'min_acceleration(cm/s2)',
                                       'max_acceleration(cm/s2)',
                                       'Length_of_acceleration(cm/s2)',
                                       'avg_acceleration_x(cm/s2)',
                                       'avg_acceleration_y(cm/s2)',
                                       'avg_acceleration_z(cm/s2)'])
        if (oputmode.saveacceleration is SaveMode.STAT) \
                or (oputmode.saveacceleration is SaveMode.STEADYSTAT):
            pass
        pass


if __name__ == '__main__':

    # variable declaration
    no_agentparams = 0
    no_flockparams = 0
    now = 0.0
    timestep2store = 0
    phasetimeline = [phase.PhaseData()]
    conditionreset = [True, True]
    accelerations = [Velocity3D()]
    collisions = 0

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
        datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '_' + OutputPath + '.csv'

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
    print('Sizes of the starting area: %fcm * %fcm * %fcm' %
          situparam.initpos.x, situparam.initpos.y, situparam.initpos.z)

    # The real challenge starts!
    statutil.elapsedtime = (now * situparam.deltaT) - \
        5.0 - unitparam.communication.tdelay

    statutil.reset()

    outputmode = outputfile.OutputMode()

    #
    statutil.savemode = outputmode.savemodelspecifics

    ifcreatefiles(outputmode)

    # Imagine 'accelerations' as a numberofagents*3 matrix (3 dims, x, y, z)
    for i in range(situparam.agentnumber - 1):
        accelerations.append(Velocity3D())

    if outputmode.savemodelspecifics is not SaveMode.FALSE:
        statutil.initmodelspecificstatus()
    flockparam.refresh()

    while statutil.elapsedtime < situparam.simlength:
        if now < timestep2store:
            pass
        else:
            pass
        if outputmode.savecollisions is SaveMode.STEADYSTAT and statutil.elapsedtime < situparam.startofsteadystate:
            collisions = 0
        pass

    # Log printing
    print('[' + datetime.datetime.now().strftime("%H:%M:%S") + '] ' +
          "The result will be written into '" + OutputPath + "'")

    # Create the output file & Write the result into file
    outputfile.generatefile(filepath=OutputPath)

    pass
