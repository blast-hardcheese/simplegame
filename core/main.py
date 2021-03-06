import time
import functools

class reprwrapper(object):
    def __init__(self, repr, func):
        self._repr = repr
        self._func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kw):
        return self._func(*args, **kw)

    def __repr__(self):
        if callable(self._repr):
            r = self._repr(self._func)
        else:
            r = self._repr
        return r

def withrepr(reprfun):
    def _wrap(func):
        return reprwrapper(reprfun, func)
    return _wrap

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

    def buildDirections(self, xy=None):
        if xy is None:
            xy = self.xy()
        x,y = xy

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

    def look(self, directionList):
        r = None
        xy = self.xy()
        for d in directionList:
            xy = self.buildDirections(xy)[d]
        return self.map.checkValue(xy)

    def go(self, delay=0):
        self.map.draw(self.xy())
        time.sleep(delay)

        @withrepr("<Function: look(Direction or DirectionList)>")
        def _look(dir):
            return self.look(dir)

        builtin_state = ['look', 'x', 'y', 'xy', 'clock']

        count = 0
        state = {}
        state['look'] = _look

        while not self.checkWon() and count < 1000:
            state['x'] = self.x
            state['y'] = self.y
            state['xy'] = self.x, self.y
            state['clock'] = count
            direction = self.move(state)
            validMoves = self.validMoves()
            if direction in validMoves:
                self.applyMovement(direction)
            self.map.draw(self.xy())
            count += 1
            time.sleep(delay)

        if self.checkWon():
            print "You won!"
        elif clock == 1000:
            print "You ran out of time, try again!"
        else:
            print "Try again!"

        statevars = [key for key in state if not key in builtin_state]
        print "  Clock:", count, 'out of', 1000
        print "  Used", len(statevars), "state variables!"
        print "  State Variables:", statevars
