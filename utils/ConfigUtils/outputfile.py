import json
import csv


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

    # TODO: Not finished: when the item user want is in deeper level of the JSON file
    return output_config[item]
    # print(output_config)


def generatefile(filepath):

    try:
        isinstance(filepath, str)
    except TypeError:
        print('The \'filepath\' should be str type')

    # TODO: finish the 'newline' parameter after specifying what results items we need
    with open(filepath, 'w', newline='') as output_csvfile:

        output_csvfile_writer = csv.writer(output_csvfile)
        # TODO: finish the value of result
        # [] indicates the param should be a dict type
        output_csvfile_writer.writerow([])

    pass
