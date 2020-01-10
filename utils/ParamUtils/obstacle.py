from utils.Basic.position import Position3D, Position2D
import utils.Basic.position as position
import json


class Obstacle:
    """

    """
    name: str
    vertex: int
    vertexcoordinates: list
    center: Position2D
    maxvertex: int

    def __init__(self, name: str, vcoords: list, maxv: int):

        self.name = name
        self.maxvertex = maxv
        self.center = position.centerofpositions(position=vcoords)
        if len(vcoords) <= self.maxvertex:
            self.vertex = len(vcoords)
            self.vertexcoordinates = vcoords
        else:
            raise ValueError('vertex can\'t be more than it\'s maximum limitation. ')


class ObstacleList:
    """

    """
    # TODO didn't take the property 'angle' into consideration; for detail read config/obstacle.json
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

    def appendobstacle(self, obstacle: Obstacle):
        if self.numofobstacle+1 <= self.maxobstacle:
            self.numofobstacle = self.numofobstacle + 1
            self.content.append(obstacle)
        else:
            raise ValueError('Out of max number limitation during appending an \'Obstacle\' object. ')

    def readfromfile(self, filepath="config/obstacles.json", toreadlist=[]):
        with open(filepath) as f_obstaclejson:
            obstaclejson = json.load(f_obstaclejson)
            for i in toreadlist:
                coordinates = obstaclejson['obstacles'][i]
                poslist = []
                p = Position2D()
                for j in coordinates:
                    poslist.append(p.readfromlist(j))
                obstacle_tmp = Obstacle(name=i, maxv=10, vcoords=poslist)
                self.appendobstacle(obstacle_tmp)

