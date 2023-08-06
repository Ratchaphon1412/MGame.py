class MGame:
    def __init__(self,listPlayers,board,listDies,num):
        self.players = listPlayers
        self.board = board
        self.dies = listDies
        self.roundCat = 0
        self.num = num
        
        
    def playGame(self):
        print("Playing game")
        print(self.board)
        while self.roundCat < self.num:
            print("Playing round " + str(self.roundCat))
            self.__playRound()
            self.roundCat += 1
    
    def __playRound(self):
        for player in self.players:
           
            player.takeTurn()
            # print(self.board)
