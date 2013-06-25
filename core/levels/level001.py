from core.map import Map
from core.types import Space, Wall, Start, End

myMap = Map([
    [Wall,  Wall,  Wall,  Wall,  Wall],
    [Wall,  Space, Space, Start, Wall],
    [Wall,  Space, Wall,  Wall,  Wall],
    [Wall,  Space, Space, End,   Wall],
    [Wall,  Wall,  Wall,  Wall,  Wall],
])
