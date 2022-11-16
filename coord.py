

class Coord:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return "Coord: x: " + str(self.x) + " - y: " + str(self.y) 