class Computer:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.player1 = "X"
        self.player2 = "O"
        self.cell_map = {
            "1": (0, 0), "2": (0, 1), "3": (0, 2),
            "4": (1, 0), "5": (1, 1), "6": (1, 2),
            "7": (2, 0), "8": (2, 1), "9": (2, 2)
        }
    def drawBoard(self):
        # Print the board with row and column labels
        print("" + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2] + "")
        print("-----------")
        print("" + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2] + "")
        print("-----------")
        print("" + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2] + "\n\n\n")

    def move(self, player, cell):
        # Map cell input (like "1", "2", "3" etc.) to board indices
        if cell in self.cell_map:
            row, col = self.cell_map[cell]
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
            win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                                (0, 4, 8), (2, 4, 6)]  # Diagonals
            for cond in win_conditions:
                if self.board[cond[0] // 3][cond[0] % 3] == self.board[cond[1] // 3][cond[1] % 3] == self.board[cond[2] // 3][cond[2] % 3] == player:
                    return True
            return False

    def checkDraw(self):
        return 
    # " " not in self.board


    def restart(self):
        # Reset the board
        self.board = [[" " for _ in range(3)] for _ in range(3)]
    def checkIfOpponentCloseToWin(self, opponentPlayer):
        for row in range(3):
            if self.board[row].count(opponentPlayer) == 2 and self.board[row].count(" ") == 1:
                return True
        for col in range(3):
            if [self.board[row][col] for row in range(3)].count(opponentPlayer) == 2 and [self.board[row][col] for row in range(3)].count(" ") == 1:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == opponentPlayer:
            return True
        if self.board[1][1] == opponentPlayer and (self.board[0][2] or self.board[2][0] == opponentPlayer):
            return True
        return False

    def computerMove(self, player):
        # Computer's move logic
        if self.checkIfOpponentCloseToWin(self.player1):
            
            for row in range(3):
                if self.board[row].count(self.player1) == 2 and self.board[row].count(" ") == 1:
                    return self.move(player, str(row * 3 + self.board[row].index(" ")))
                else: 
                    continue
            for col in range(3):
                if self.board[col].count(self.player1) == 2 and self.board[col].count(" ") == 1:
                    return self.move(player, str(self.board[col].index(" ")))
                else: 
                    continue
                
                
            if self.board[1][1] == self.player1 and (self.board[0][2] or self.board[2][0] == self.player1):
                if self.board[0][2] == " ":
                    return self.move(player, "1")
                elif self.board[2][0] == " ":
                    return self.move(player, "9")
                else:
                    pass
                
            if self.board[0][2] == self.player1 and self.board[2][0] == self.player1:
                if self.board[1][1] == " ":
                    return self.move(player, "5")
                else: 
                    pass
            if self.board[0][0] == self.player1 and self.board[1][1] == self.player1:
                if self.board[2][2] == " ":
                    return self.move(player, "9")
                else: 
                    pass
            if self.board[2][2] == self.player1 and self.board[1][1] == self.player1:
                if self.board[0][0] == " ":
                    return self.move(player, "1")
                else: 
                    pass
            if self.board[0][0] == self.player1 and self.board[2][2] == self.player1:
                if self.board[1][1] == " ":
                    return self.move(player, "5")
                else: 
                    pass
        else:
            if self.board[1][1] == " ":
                return self.move(player, "5")
            else:
                if self.board[0][2] == " ":
                    return self.move(player, "3")
                else:
                    if self.board[2][0] == " ":
                        return self.move(player, "7")
                    else:
                        if self.board[2][2] == " ":
                            return self.move(player, "9")
                        else:
                            if self.board[0][0] == " ":
                                return self.move(player, "1")
                            else:
                                return self.move(player, self.board.index(" "))
        
        
            
        if self.checkIfOpponentCloseToWin(self.player2):
            for row in range(3):
                if self.board[row].count(self.player2) == 2 and self.board[row].count(" ") == 1:
                    return self.move(player, str(self.board[row].index(" ")))
                else: 
                    continue
            for col in range(3):
                if self.board[col].count(self.player2) == 2 and self.board[col].count(" ") == 1:
                    return self.move(player, str(self.board[col].index(" ")))
                else: 
                    continue
            if self.board[1][1] == self.player2 and (self.board[0][2] or self.board[2][0] == self.player2):
                if self.board[0][2] == " ":
                    return self.move(player, "1")
                elif self.board[2][0] == " ":
                    return self.move(player, "9")
                else:
                    pass
            if self.board[0][2] == self.player2 and self.board[2][0] == self.player2:
                return self.move(player, "5")
            if self.board[0][0] == self.player2 and self.board[1][1] == self.player2:
                if self.board[2][2] == " ":
                    return self.move(player, "9")
                else: 
                    pass
            if self.board[2][2] == self.player2 and self.board[1][1] == self.player2:
                if self.board[0][0] == " ":
                    return self.move(player, "1")
                else: 
                    pass
            if self.board[0][0] == self.player2 and self.board[2][2] == self.player2:
                if self.board[1][1] == " ":
                    return self.move(player, "5")
                else: 
                    pass
        else:
            if self.board[1][1] == " ":
                return self.move(player, "5")
            else:
                if self.board[0][0] == " ":
                    return self.move(player, "1")
                else:
                    if self.board[0][2] == " ":
                        return self.move(player, "3")
                    else:
                        if self.board[2][0] == " ":
                            return self.move(player, "7")
                        else:
                            if self.board[2][2] == " ":
                                return self.move(player, "9")
                            else:
                                pass
                            
                            
                            
computer = Computer()
start = input("Type 1 to start\nType 2 to exit\nType 3 for credits\n")
if start == "1":
    gameEnded = False
    while not gameEnded:
        computer.drawBoard()
        move = input("Enter your move: ")
        legal = computer.move("X", move)
        
        if not legal:
            print("Invalid move. Try again.")
            move = input("Enter your move: ")
            legal = computer.move("X", move)
            
        if computer.checkWin("X"):
            print("You win!")
            computer.drawBoard()
            gameEnded = True
            break
        elif computer.checkDraw():
            print("It's a draw!")
            computer.drawBoard()
            gameEnded = True
            break
        
        computer.drawBoard()
        computer.computerMove("O")
        
        if computer.checkWin("O"):
            print("Computer wins!")
            computer.drawBoard()
            gameEnded = True
            break
        elif computer.checkDraw(): 
            print("It's a draw!")
            computer.drawBoard()
            gameEnded = True
            break