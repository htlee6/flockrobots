import math


class Position2D:

    x: float
    y: float

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

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

    def readfromlist(self, l: list):
        """"""
        for i in l:
            if type(i) is not float and type(i) is not int:
                raise TypeError('Elements in the list should all be int or float type. ')
        return Position2D(x=float(l[0]), y=float(l[1]))


class Position3D(Position2D):

    z: float

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def positiondiff(self, pos: 'Position3D'):
        """

        :param pos:
        :return:
        """
        return Position3D(self.x - pos.x, self.y - pos.y, self.z - pos.z)

    def length(self):
        """

        :return:
        """
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    def readfromlist(self, l: list):
        """"""
        for i in l:
            if type(i) is not float and type(i) is not int:
                raise TypeError('Elements in the list should all be int or float type. ')
        return Position2D(x=float(l[0]), y=float(l[1]), z=float(l[2]))
