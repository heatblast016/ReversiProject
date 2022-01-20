import numpy as np;
from typing import Tuple

class game:
    def __init__(self):
        #Initializes board and set containing all valid moves
        self.board = np.full((8,8), -1)
        self.validcounter = [0,0]
        self.valid = np.full((8,8,2), 0)
        self.board[3,3] = 1
        self.board[4,4] = 1
        self.board[3,4] = 0
        self.board[4,3] = 0
        self.score = [0,0]
        #pre-seeds board with all valid moves
        self.updateValid(1,3,3)
        self.updateValid(1,4,4)
        self.updateValid(0,3,4)
        self.updateValid(0,4,3)

    def getBoardState(self) -> np.ndarray:
        return self.board

    def getValid(self, player: int) -> np.ndarray:
        return (self.valid[:,:,player] > 0)

    def gameOver(self, player: int) -> bool:
        if self.validcounter[player] == 0:
           return True
        return False 

    def setValid(self, player: int, x: int, y: int, direction: Tuple[int, int]) -> None:
        (newx, newy) = (x+direction[0],y + direction[1]) 
        #checks out of bounds
        if not ((newx > 7 or newx < 0) or (newy > 7 or newy < 0)):
            self.valid[newx,newy,player] = self.valid[newx,newy,player] + 1
            #increment count of valid moves
            self.validcounter[player] = self.validcounter[player] + 1
            self.setValid(player, newx, newy, direction)

    def updateValid(self, player: int, x: int, y: int) -> None:
        #function to start updating valid moves in all directions
        #purely for convenience
        for dirx in range(-1,2):
            for diry in range(-1,2):
                if not (dirx == 0 and diry == 0):
                    self.setValid(player, x,y, (dirx, diry))

    #update valid states for flips
    def flipValid(self, player: int, x: int, y: int, direction: Tuple[int, int]) -> None:
        (newx, newy) = (x+direction[0],y + direction[1]) 
        #checks out of bounds
        if not ((newx > 7 or newx < 0) or (newy > 7 or newy < 0)):
            self.valid[newx,newy,player] = self.valid[newx,newy,player] + 1
            self.valid[newx,newy,1-player] = self.valid[newx,newy,1-player] - 1
            #increment count of valid moves

            self.validcounter[player] = self.validcounter[player] + 1
            self.validcounter[1-player] = self.validcounter[1-player] - 1
            self.flipValid(player, newx, newy, direction)

    def updateValidFlips(self, player: int, x: int, y: int) -> None:
        #function to start updating valid moves in all directions
        #purely for convenience
        for dirx in range(-1,2):
            for diry in range(-1,2):
                if not (dirx == 0 and diry == 0):
                    self.flipValid(player, x,y, (dirx, diry))


    def move(self, player: int, x: int, y: int) -> bool:
        if self.valid[x,y,player] == 0: 
            return False
        else:
            self.validcounter[player] = self.validcounter[player] - 1;
            self.valid[x,y,player] = 0
            self.board[x,y] = player
            
            self.score[player] = self.score[player] + 1
            self.updateValid(player, x, y)
            self.updateFlips(player, x, y)
            return True

    def updateFlips(self, player: int, x: int, y: int) -> None:
        #function to start flipping in all directions
        #purely for convenience
        for dirx in range(-1,2):
            for diry in range(-1,2):
                if not (dirx == 0 and diry == 0):
                    self.flip(player, x,y, (dirx, diry))
    
    def flip(self, player: int, x: int, y: int, direction: Tuple[int, int]) -> bool:
        #recursive function to execute the flipping mechanic
        #works by recursively looking down a direction, terminating at either another disc of the same color(in which case it'd return true) or an edge (returns false)
        (newx, newy) = (x+direction[0],y + direction[1]) 
        #checks out of bounds
        if ((newx > 7 or newx < 0) or (newy > 7 or newy < 0)):
            return False
        elif self.board[newx, newy] == player:
            return True
        if self.flip(player, newx, newy, direction):
            if self.board[newx, newy] == 1-player:
                self.board[newx, newy] = player 
                self.score[player] = self.score[player] + 1
                self.score[1-player] = self.score[1-player] - 1
                self.updateValidFlips(player,newx,newy)
            return True
        else:
            return False

    def getWinner(self) -> int:
        if(self.score[0] > self.score[1]):
            return 1
        elif (self.score[0] == self.score[1]):
            return -1
        return 2