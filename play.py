#!/usr/bin/env python

from core.main import Game
from core.levels.level001 import myMap
from core.types import Space,Wall,Start,End

# Currently you can return one of the four movement directions, L, R, U, D
# Returning anything else skips one move
def level001(state):
    print state
    print "Is there a space above me?", state['look']('U') == Space
    return ''

game = Game()
game.setMap(myMap)
game.setMoveMethod(level001)
game.go(delay=2)
