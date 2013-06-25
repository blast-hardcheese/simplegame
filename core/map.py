from core.types import Start, End, Characters
class Map(object):
    def __init__(self, gameboard):
        self.gameboard = gameboard
        self.rows = len(self.gameboard)
        self.cols = len(self.gameboard[0])
        self.start = self.findStart()
        self.end = self.findEnd()

    def iterateTiles(self, callback):
        for y in range(self.cols):
            for x in range(self.rows):
                r = callback((x,y), self.gameboard[y][x])
                if r is not None:
                    return r

    def findStart(self):
        return self.findType(Start)

    def findEnd(self):
        return self.findType(End)

    def findType(self, TYPE):
        def callback(xy, char):
            if char == TYPE:
                return xy
        return self.iterateTiles(callback)

    def draw(self):
        def callback(xy, char):
            if xy[0] == 0 and xy[1] > 0:
                print
            _char = Characters.get(char)
            print _char,
        self.iterateTiles(callback)
