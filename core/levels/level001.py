from core.map import Map
from core import types

myMap = Map([
    [types.Wall, types.Wall, types.Wall, types.Wall, types.Wall],
    [types.Wall, types.Space, types.Space, types.Start, types.Wall],
    [types.Wall, types.Space, types.Wall, types.Wall, types.Wall],
    [types.Wall, types.Space, types.Space, types.End, types.Wall],
    [types.Wall, types.Wall, types.Wall, types.Wall, types.Wall],
])
