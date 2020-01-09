import json
from utils.Basic.position import Position2D, Position3D


class Arena:
    name: str
    maxvertices: int
    vertex: int
    vertexcoordinate: list

    def __init__(self, name: str, maxvertices: int, vertexcoord: list):
        self.name = name
        self.maxvertices = maxvertices
        if self.maxvertices >= len(vertexcoord):
            self.vertexcoordinate = vertexcoord
            self.vertex = len(vertexcoord)
        else:
            raise ValueError('vertex can\'t be more than it\'s maximum limitation. ')

    def func1(self):
        pass


class ArenaList:
    numofarena: int
    maxnumofarena: int
    content: list

    def __init__(self, maxarenacount: int, content: list):
        self.maxnumofarena = maxarenacount
        if self.maxnumofarena >= len(content):
            self.content = content
            self.numofarena = len(content)
        else:
            raise ValueError('numofarena can\'t be more than it\'s maximum limitation. ')

    def changemax(self, expectedmax: int):
        self.maxnumofarena = expectedmax

    def appendarena(self, arena: Arena):
        if self.numofarena+1 <= self.maxnumofarena:
            self.numofarena = self.numofarena + 1
            self.content.append(arena)
        else:
            raise ValueError('Out of max number limitation during appending an \'Arena\' object. ')

    def readfromfile(self, filepath="config/arena.json", toreadlist=[]):
        with open(filepath, 'r') as f_arenajson:
            arenajson = json.load(f_arenajson)
            for i in toreadlist:
                coordinates = arenajson[i]['vertex']
                poslist = []
                p = Position2D()
                for j in coordinates:
                    poslist.append(p.readfromlist(j))
                arena_tmp = Arena(name=i, maxvertices=10, vertexcoord=poslist)
                self.appendarena(arena_tmp)
                pass


