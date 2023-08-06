class Piece:
    def __init__(self,squareLocation):
        self.squareLocation = squareLocation
    
    def getLocation(self):
        return self.squareLocation
    
    def setLocation(self,squareLocation):
        self.squareLocation = squareLocation
        