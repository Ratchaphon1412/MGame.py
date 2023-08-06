from src.MGame import MGame
from src.Player import Player
from src.Board import Board
from src.Square import Square
from src.Die import Die
from src.Piece import Piece

listSquare = []
for i in range(40):
    listSquare.append(Square(str(i)))
    
board = Board(listSquare)

listDies=[]
listDies.append(Die())
listDies.append(Die())


playersList = []
playersList.append(Player("Player 1",board,listDies,Piece(listSquare[0])))
playersList.append(Player("Player 2",board,listDies,Piece(listSquare[0])))
playersList.append(Player("Player 3",board,listDies,Piece(listSquare[0])))

roundCat = 30

mGame = MGame(playersList,board,listDies,roundCat)
mGame.playGame()