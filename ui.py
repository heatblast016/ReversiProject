from game import game
class ui:
    def __init__(self, board: game):
        self.board = board
    
    def printBoardState(self, nextPlayer: int) -> None:
        layout = self.board.getBoardState()
        valid = self.board.getValid(nextPlayer)
        print("    1   2   3   4   5   6   7   8")
        for i in range(0,8):
            print(str(i+1) + " |", end='')
            for j in range(0,8):
                symbol = " "
                if layout[j,i] == 1:
                    symbol = "◉"
                elif layout[j,i] == 0:
                    symbol = "◎"
                elif valid[j,i]:
                    symbol = "x" 
                print(" " + symbol + " |", end='')
            print("")
            print("-----------------------------------")
    def getMove(self, player: int) -> None:
        while True:
            x = int(input("Player " + str(player+1) + ", please enter your desired x coordinate for your next move: "))
            y = int(input("Please enter your desired y coordinate for your next move: "))
            if (x >8 or x < 1) or (y > 8 or y < 1):
                print("Error: The coordinates you provided were not integers between 1 and 8")
                continue
            elif not self.board.move(player, x-1, y-1):
                print("Error: Your move was not a valid move")
                continue
            return
            

