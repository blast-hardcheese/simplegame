from core.types import Start, End, Player, Characters

class Map(object):
    def __init__(self, gameboard):
        self.gameboard = gameboard
        self.rows = len(self.gameboard)
        self.cols = len(self.gameboard[0])
        self.start = self.findStart()
        self.end = self.findEnd()

    @classmethod
    def fromAscii(cls, s):
        lines = s.split('\n')
        gameboard = []
        for y in xrange(len(lines)):
            row = []
            gameboard.append(row)
            for x in xrange(len(lines[y])):
                char = lines[y][x]
                val = Characters.get(char)
                row.append(val)
        return cls(gameboard)

    def iterateTiles(self, callback, accumulate=False):
        r = None
        grid = []
        for y in range(self.rows):
            row = []
            grid.append(row)
            for x in range(self.cols):
                r = callback((x,y), self.gameboard[y][x])
                if accumulate:
                    row.append(r)
                elif r is not None:
                    return r
        if accumulate:
            r = grid
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
            _char = Characters.get(char)
            if xy == playerpos:
                _char = Characters.get(Player)
            return _char

        grid = self.iterateTiles(callback, accumulate=True)
        s = '\n'.join([''.join(row) for row in grid])
        print s
