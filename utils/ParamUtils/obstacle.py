from utils.Basic.position import Position3D, Position2D


class Obstacle:
    """

    """
    name: str
    vertex: int
    vertexcoordinates: list
    centerofvertex: Position2D
    maxvertex: int

    def __init__(self, name: str, vertex: int, vcoords: list, centerofv: Position2D, maxv: int):
        self.name = name
        self.vertexcoordinates = vcoords
        self.centerofvertex = centerofv
        self.maxvertex = maxv
        if vertex <= self.maxvertex:
            self.vertex = vertex
        else:
            raise ValueError('vertex can\'t be more than it\'s maximum limitation. ')


class ObstacleList:
    """

    """
    maxobstacle: int
    numofobstacle: int
    content: list

    def __init__(self, maxobs: int, content: list):
        self.maxobstacle = maxobs
        if self.maxobstacle >= len(content):
            self.numofobstacle = len(content)
            self.content = content
        else:
            raise ValueError('numbofobstacles can\'t be more than it\'s maximum limitation. ')

