#!/usr/bin/env python

from core import Types
from core import Map

myMap = Map([
    [Types.Wall, Types.Wall, Types.Wall, Types.Wall, Types.Wall],
    [Types.Wall, Types.Space, Types.Space, Types.Start, Types.Wall],
    [Types.Wall, Types.Space, Types.Wall, Types.Wall, Types.Wall],
    [Types.Wall, Types.Space, Types.Space, Types.End, Types.Wall],
    [Types.Wall, Types.Wall, Types.Wall, Types.Wall, Types.Wall],
])

myMap.draw()
