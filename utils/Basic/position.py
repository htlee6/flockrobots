import math
import numpy as np


class Position2D:

    x: float
    y: float

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return '[%f, %f]' % (self.x, self.y)

    def __add__(self, toaddpos: 'Position2D'):
        return Position2D(self.x+toaddpos.x, self.y+toaddpos.y)

    def __sub__(self, tosubpos: 'Position2D'):
        return Position2D(self.x-tosubpos.x, self.y-tosubpos.y)

    def positiondiff(self, pos: 'Position2D'):
        """

        :param pos:
        :return: a Position2D object contains the difference of 2 vectors.
        """
        return Position2D(self.x-pos.x, self.y-pos.y)

    def length(self):
        """

        :return: the length of the 2 dim vector.
        """
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def readfromlist(self, toread: list):
        """"""
        for i in toread:
            if type(i) is not float and type(i) is not int:
                raise TypeError('Elements in the list should all be int or float type. ')
        return Position2D(x=float(toread[0]), y=float(toread[1]))


class Position3D(Position2D):

    z: float

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '[%f, %f, %f]' % (self.x, self.y, self.z)

    def __add__(self, toaddpos: 'Position3D'):
        return Position3D(self.x+toaddpos.x, self.y+toaddpos.y, self.z+toaddpos.z)

    def __sub__(self, tosubpos: 'Position3D'):
        return Position3D(self.x-tosubpos.x, self.y-tosubpos.y, self.z-tosubpos.z)

    def positiondiff(self, pos: 'Position3D'):
        """

        :param pos:s
        :return:
        """
        return Position3D(self.x - pos.x, self.y - pos.y, self.z - pos.z)

    def length(self):
        """

        :return:
        """
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    def readfromlist(self, toread: list):
        """"""
        for i in toread:
            if type(i) is not float and type(i) is not int:
                raise TypeError('Elements in the list should all be int or float type. ')
        return Position2D(x=float(toread[0]), y=float(toread[1]), z=float(toread[2]))


def ifpure(list2judge: list, typeexpected: type):
    """

    """
    for i in list2judge:
        if type(i) is not typeexpected:
            return False
    return True


def centerofpositions(positions: list):
    if ifpure(list2judge=positions, typeexpected=Position2D):
        x_array = []
        y_array = []
        for i in positions:
            x_array.append(i.x)
            y_array.append(i.y)
        return Position2D(np.average(x_array), np.average(y_array))
    elif ifpure(list2judge=positions, typeexpected=Position3D):
        x_array = []
        y_array = []
        z_array = []
        for i in positions:
            x_array.append(i.x)
            y_array.append(i.y)
            z_array.append(i.z)
        return Position3D(np.average(x_array), np.average(y_array), np.average(z_array))
    else:
        raise ValueError('The parameter is not a list filled with either \'Position2D\' class or \'Position3D\' class. ')



