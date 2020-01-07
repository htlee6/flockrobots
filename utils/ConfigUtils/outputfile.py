import json
import csv
import os
from utils.StatsticUtils.stat import SaveMode


def getconfig(filepath='default',
              item='OutputFilename'):
    """ Get information from output config file.

    :param filepath: Where the output config file lies;
    :param item: The index of the item you wish to acquire;
    :return: The selected status/setting of index 'item' in JSON;
    :rtype: String;
    """
    if filepath == 'default':
        filepath = 'config/output/output_default.json'

    config_file = open(filepath)
    output_config = json.load(fp=config_file)

    # TODO: Not finished: when the item user want is in deeper level of the
    # JSON file
    return output_config[item]
    # print(output_config)


def generatefile(filepath):

    try:
        isinstance(filepath, str)
    except TypeError:
        print('The \'filepath\' should be str type')

    # TODO: finish the 'newline' parameter after specifying what results items
    # we need
    with open(filepath, 'w', newline='') as output_csvfile:

        output_csvfile_writer = csv.writer(output_csvfile)
        # TODO: finish the value of result
        # [] indicates the param should be a dict type
        output_csvfile_writer.writerow([])

    pass


def str2savemode(string: str):
    if string == 'STAT':
        return SaveMode.STAT
    elif string == 'STEADYSTAT':
        return SaveMode.STEADYSTAT
    elif string == 'FALSE':
        return SaveMode.FALSE
    elif string == 'TIMELINE':
        return SaveMode.TIMELINE
    else:
        raise Exception(
            'The savemode content in JSON is illegal. Must be one of STAT/STEADYSTAT/FALSE/TIMELINE. Check again.')
        return 0


class OutputMode:
    #
    savetrajectories: bool
    saveinnerstates: bool

    #
    savedistancebetweenunits: SaveMode
    savedistancebetweenneighbors: SaveMode
    savevelocity: SaveMode
    savecorrelation: SaveMode
    saveCoM: SaveMode
    savecollisions: SaveMode
    savecollisionratio: SaveMode
    saveacceleration: SaveMode

    # Save model specific params
    savemodelspecifics: SaveMode

    def __init__(self, savetrajectories=True,
                 saveinnerstates=True,
                 savedistancebetweenunits=SaveMode.STAT,
                 savedistancebetwenneighbors=SaveMode.STAT,
                 savevelocity=SaveMode.STAT,
                 savecorrelation=SaveMode.STAT,
                 saveCoM=SaveMode.STAT,
                 savecollisions=SaveMode.STAT,
                 savecollisionratio=SaveMode.STAT,
                 saveaccerleration=SaveMode.STAT,
                 savemodelspecific=SaveMode.STAT):

        self.savetrajectories = savetrajectories
        self.saveacceleration = saveaccerleration
        self.saveinnerstates = saveinnerstates
        self.savedistancebetweenunits = savedistancebetweenunits
        self.savedistancebetweenneighbors = savedistancebetwenneighbors
        self.savevelocity = savevelocity
        self.savecorrelation = savecorrelation
        self.saveCoM = saveCoM
        self.savecollisions = savecollisions
        self.savecollisionratio = savecollisionratio
        self.savemodelspecifics = savemodelspecific

    def usedefault(self, filepath='config/output/output_default.json'):
        configjson = json.load(fp=open(filepath))
        ifsavedetailjson = configjson['ifSaveDetail']
        self.savedistancebetweenunits = str2savemode(
            ifsavedetailjson['SaveDistanceBetweenUnits'])
        self.savedistancebetweenneighbors = str2savemode(
            ifsavedetailjson['SaveDistanceBetweenNeighbours'])
        self.savevelocity = str2savemode(ifsavedetailjson['SaveVelocity'])
        self.savecorrelation = str2savemode(
            ifsavedetailjson['SaveCorrelation'])
        self.saveCoM = str2savemode(ifsavedetailjson['SaveCoM'])
        self.savecollisions = str2savemode(ifsavedetailjson['SaveCollisions'])
        self.savecollisionratio = str2savemode(
            ifsavedetailjson['SaveCollisionRatio'])
        self.saveacceleration = str2savemode(
            ifsavedetailjson['SaveAcceleration'])


def createdatastorefiles(oputmode: OutputMode, **symbolsyoulike):
    """
    Files all stored in 'output' directory, including:

    - posandvel.csv
    - innerstates.csv
    - collisions.csv
    - distance_between_units.csv
    - dist_between_units.csv
    - velocity.csv
    - CoM.csv
    - correlation.csv
    - collision_ratio.csv
    - acceleration.csv
    :param oputmode: outputmode
    :return: None
    """
    if len(symbolsyoulike) is not 0:
        symbol = str(symbolsyoulike['symbol'])
        try:
            os.mkdir('output/'+symbol)
        except OSError:
            print('Can\'t create a new folder with symbol. ')
    else:
        symbol = ''

    if oputmode.savetrajectories:
        with open('output/'+symbol+'/posandvel.csv', 'w+') as f_outphase:
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
        with open('output/'+symbol+'/innerstates.csv', 'w+') as f_outinnerstates:
            csv_outinnterstates = csv.writer(f_outinnerstates)
            csv_outinnterstates.writerow(['time(s)'])

    if oputmode.savecollisions is not SaveMode.FALSE:
        with open('output/'+symbol+'/collisions.csv', 'w+') as f_collisions:
            csv_collision = csv.writer(f_collisions)
            csv_collision.writerow(['time(s)',
                                    'number_of_collisions'])

    if oputmode.savedistancebetweenunits is not SaveMode.FALSE:
        with open('output/'+symbol+'/distance_between_units.csv', 'w+') as f_distbetweenunits:
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
        with open('output/'+symbol+'/dist_between_neighbours.csv', 'w+') as f_distbetweenneighbours:
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
        with open('output/'+symbol+'/velocity.csv', 'w+') as f_velocity:
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
        with open('output/'+symbol+'/CoM.csv', 'w+') as f_CoM:
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
        with open('output/'+symbol+'/correlation.csv', 'w+') as f_correlation:
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
        with open('output/'+symbol+'/collision_ratio.csv', 'w+') as f_collisionratio:
            csv_collisionration = csv.writer(f_collisionratio)
            csv_collisionration.writerow(['time',
                                          'ratio_of_collision'])
        if (oputmode.savecollisionratio is SaveMode.STAT) \
                or (oputmode.savecollisionratio is SaveMode.STEADYSTAT):
            pass
        pass

    if oputmode.saveacceleration is not SaveMode.FALSE:
        with open('output/'+symbol+'/acceleration.csv', 'w+') as f_acceleration:
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
