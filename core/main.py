class Game(object):
    x,y = 0,0
    def setMap(self, map):
        self.map = map
        (self.x, self.y) = self.map.start

    def setMoveMethod(self, func):
        self.move = func

    def checkWon(self):
        return self.map.end == (x,y)

    def go(self):
        count = 0
        while not self.checkWon() and count < 1000:
            self.move()
            count += 1
