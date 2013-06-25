#!/usr/bin/env python

from core.main import Game
from core.levels.level001 import myMap

# Currently you can return one of the four movement directions, L, R, U, D
# Returning anything else skips one move
def level001(state):
    print state
    return ''

game = Game()
game.setMap(myMap)
game.setMoveMethod(level001)
game.go()
