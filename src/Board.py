class Board:
    def __init__(self,listSquare):
        self.square = listSquare
        
    def getSquares(self,oldLoc,fvTot):
        
        # new index is the index of the new location of the piece
        newIndex = self.square.index(oldLoc) + fvTot
        squareNew = None
        try:
            squareNew = self.square[newIndex]
        except IndexError:
            newIndex = newIndex - len(self.square)
            squareNew = self.square[newIndex]
        
        
        return squareNew
    
    def __str__(self):
        
        listSquare = []
        for square in self.square:
            listSquare.append(square.getName())
        
        return "Board: " + str(listSquare)