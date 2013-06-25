from core.types import Start, End, Player, Characters

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

    def checkValue(self, xy):
        x,y = xy

        if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
            return None
        else:
            return self.gameboard[y][x]

    def draw(self, playerpos=None):
        def callback(xy, char):
            if xy[0] == 0 and xy[1] > 0:
                print # Newline at the beginning of every row
            _char = Characters.get(char)
            if xy == playerpos:
                _char = Characters.get(Player)
            print _char,
            if xy[0] == self.rows - 1 and xy[1] == self.cols - 1:
                print # Final newline to clean things up
        self.iterateTiles(callback)
