from core.map import Map
from core.types import Space, Wall, Start, End

s = '''
###############
#S#           #
# # ######### #
# # #       # #
# # # ##### # #
# # # #   # # #
# # # # # # # #
# # # #E# # # #
# # # ### # # #
# # #     # # #
# # ####### # #
# #         # #
# ########### #
#             #
###############
'''[1:-1]

myMap = Map.fromAscii(s)
