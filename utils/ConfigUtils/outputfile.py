import json
import csv
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



