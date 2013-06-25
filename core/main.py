from core.types import Space,Wall,Start,End
class Game(object):
    x,y = 0,0
    def setMap(self, map):
        self.map = map
        (self.x, self.y) = self.map.start

    def setMoveMethod(self, func):
        self.move = func

    def checkWon(self):
        return self.map.end == (self.x,self.y)

    def xy(self):
        return (self.x, self.y)

    def buildDirections(self):
        x,y = self.xy()

        directions = {
            'L':(x-1, y),
            'R':(x+1, y),
            'U':(x, y-1),
            'D':(x, y+1),
        }
        return directions

    def validMoves(self):
        map = self.map
        directions = self.buildDirections()

        r = []
        for key in directions:
            xy = directions[key]
            value = map.checkValue(xy)
            if value in (Space, Start, End):
                r.append(key)
        return r

    def applyMovement(self, direction):
        directions = self.buildDirections()
        newXy = directions.get(direction)
        if newXy:
            self.x,self.y = newXy

    def go(self):
        count = 0
        state = {}
        while not self.checkWon() and count < 1000:
            state['x'] = self.x
            state['y'] = self.y
            state['clock'] = count
            direction = self.move(state)
            validMoves = self.validMoves()
            if direction in validMoves:
                self.applyMovement(direction)
            self.map.draw(self.xy())
            count += 1
