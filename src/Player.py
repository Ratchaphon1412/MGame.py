class Player:
    def __init__(self,name,board,dies,piece):
        self.piece = piece
        self.name = name
        self.board = board
        self.dies = dies
    
    
    def takeTurn(self):
        # fv is the sum of the face values of the dies
        fv = 0 
        for die in self.dies:
            die.roll()
            fv += die.getFaceValue()
        # oldLoc is object of Square that is the current location of the piece
        oldLoc = self.piece.getLocation()
        print (self.name + " old location " + oldLoc.getName() )
        # newLoc is object of Square that is the new location of the piece
        newLoc = self.board.getSquares(oldLoc,fv)
        
        print("------------------------------------")
        print(self.name + " new location " + newLoc.getName())
        print (self.name + " old location " + oldLoc.getName() )
        print("------------------------------------")
        
        
        # set the location of the piece to the new location
        self.piece.setLocation(newLoc)