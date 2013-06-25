#!/usr/bin/env python

from core.main import Game
from core.levels.level001 import myMap

def level001(state):
    print state
    return ''

game = Game()
game.setMap(myMap)
game.setMoveMethod(level001)
game.go()
