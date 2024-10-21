class TickTackToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # Initialize an empty board

    def drawBoard(self):
        # Print the current state of the board
        for i in range(3):
            print(self.board[i * 3] + " | " + self.board[i * 3 + 1] + " | " + self.board[i * 3 + 2])
            if i < 2:
                print("---------")

    def move(self, player, cell):
        cell = int(cell) - 1  # Convert cell to zero-based index
        if self.board[cell] == " ":  # Check if the cell is empty
            self.board[cell] = player
            return True
        return False

    def checkWin(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                          (0, 4, 8), (2, 4, 6)]  # Diagonals
        for cond in win_conditions:
            if self.board[cond[0]] == self.board[cond[1]] == self.board[cond[2]] == player:
                return True
        return False

    def checkDraw(self):
        return " " not in self.board

    def restart(self):
        self.board = [" " for _ in range(9)]  # Reset the board


# Main game logic
def main():
    ttt = TickTackToe()
    print("Tick Tack Toe\nType 1 to start\nType 2 to exit\nType 3 for credits\n")
    
    program = input()  # Take input from the user
    
    if program == "1":
        gameEnded = False
        while not gameEnded:
            ttt.drawBoard()
            
            # Player 1's turn
            cell1 = input("Player 1, enter cell (1-9): ")
            while not ttt.move("X", cell1):
                cell1 = input("Cell already taken. Enter a new cell (1-9): ")
            
            if ttt.checkWin("X"):
                print("Player 1 wins!")
                ttt.drawBoard()
                gameEnded = True
                break
            elif ttt.checkDraw():
                print("It's a draw!")
                ttt.drawBoard()
                gameEnded = True
                break
            
            # Player 2's turn
            ttt.drawBoard()
            cell2 = input("Player 2, enter cell (1-9): ")
            while not ttt.move("O", cell2):
                cell2 = input("Cell already taken. Enter a new cell (1-9): ")
            
            if ttt.checkWin("O"):
                print("Player 2 wins!")
                ttt.drawBoard()
                gameEnded = True
                break
            elif ttt.checkDraw():
                print("It's a draw!")
                ttt.drawBoard()
                gameEnded = True
                break
        
        # Ask for restart or exit
        print("Type 1 to restart\nType 2 to exit\nType 3 for credits\n")
        restart = input()
        if restart == "1":
            ttt.restart()
            main()  # Restart the game
        elif restart == "2":
            exit()

    elif program == "2":
        exit()
    elif program == "3":
        print("Credits: Made by You!")


# Start the game
main()