#!/usr/bin/env python

from core import types
from core.map import Map

myMap = Map([
    [types.Wall, types.Wall, types.Wall, types.Wall, types.Wall],
    [types.Wall, types.Space, types.Space, types.Start, types.Wall],
    [types.Wall, types.Space, types.Wall, types.Wall, types.Wall],
    [types.Wall, types.Space, types.Space, types.End, types.Wall],
    [types.Wall, types.Wall, types.Wall, types.Wall, types.Wall],
])

myMap.draw()
