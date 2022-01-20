from calendar import c
from game import game
from ui import ui
import os


board = game()
ui = ui(board)
currentplayer = 0

os.system('cls' if os.name == 'nt' else 'clear')
while not board.gameOver(currentplayer):
    ui.printBoardState(currentplayer)
    ui.getMove(currentplayer)
    os.system('cls' if os.name == 'nt' else 'clear')
    currentplayer = 1-currentplayer
if(not board.gameOver(1-currentplayer)):
    print("Player " + str(2-currentplayer) + " wins!")
else:
    winner = board.getWinner()
    if(winner == -1):
        print("Both players tied!")
    else:
        print("Player " + winner + " wins!")