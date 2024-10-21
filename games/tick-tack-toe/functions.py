class TickTackToe:
    def __init__(self):
        # Initialize the board as a 3x3 list of spaces
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.player1 = "X"
        self.player2 = "O"

    def drawBoard(self):
        # Print the board with row and column labels

        print(f"| {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} |")
        print("   -----------")
        print(f"| {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} |")
        print("   -----------")
        print(f"| {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} |")

    def move(self, player, cell):
        # Map cell input (like "a1", "b2") to board indices
        cell_map = {
            "1": (0, 0), "2": (0, 1), "3": (0, 2),
            "4": (1, 0), "5": (1, 1), "6": (1, 2),
            "7": (2, 0), "8": (2, 1), "9": (2, 2)
        }

        if cell in cell_map:
            row, col = cell_map[cell]
            if self.board[row][col] == " ":  # Check if the cell is empty
                self.board[row][col] = player
                return True
            else:
                print("Cell already taken")
                return False
        else:
            print("Invalid cell input")
            return False

    def checkWin(self, player):
        # Check rows, columns, and diagonals for a win
        for row in self.board:
            if all([cell == player for cell in row]):
                return True
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def checkDraw(self):
        # Check if all cells are filled and there's no winner
        return all(cell != " " for row in self.board for cell in row)

    def restart(self):
        # Reset the board
        self.board = [[" " for _ in range(3)] for _ in range(3)]


# Example usage:
game = TickTackToe()