from core.Types import Characters
class Map(object):
    def __init__(self, gameboard):
        self.gameboard = gameboard

    def draw(self):
        for row in self.gameboard:
            for column in row:
                char = Characters.get(column)
                print char,
            print
