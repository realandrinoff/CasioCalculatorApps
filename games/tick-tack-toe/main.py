from functions import TickTackToe as ttt

print("Tick Tack Toe \n Type 1 to start \n Type 2 to exit \n Type 3 for credits \n")
program = input()
if program == "1":
    while True:
        global gameEnded
        gameEnded = False
        while not gameEnded:
            ttt.drawBoard()
            cell1 = input("Player 1, enter cell: ")
            move1 = ttt.move("X", cell1)
            if not move1:
                cell1 = input("Enter cell: ")
                move = ttt.move("X", cell1)
            if ttt.checkWin("X"):
                print("Player 1 wins")
                ttt.drawBoard()
                gameEnded = True
                break
            elif ttt.checkDraw():
                print("Draw")
                ttt.drawBoard()
                gameEnded = True
                break
            ttt.drawBoard()
            cell2= input("Player 2, enter cell: ")
            move2 = ttt.move("O", cell2)
            if not move2:
                cell2 = input("Enter cell: ")
                move2 = ttt.move("X", cell2)
            if ttt.checkWin("O"):
                print("Player 2 wins")
                ttt.drawBoard()
                gameEnded = True
                break
            elif ttt.checkDraw():
                print("Draw")
                ttt.drawBoard()
                gameEnded = True
                break
        if gameEnded: 
            print("Type 1 to restart \n Type 2 to exit \n Type 3 for credits \n")
            restart = input()
            if restart == "1":
                ttt.restart()
                gameEnded = False
            elif program == "2":
                exit()
                break
            elif program == "3":
                pass


elif program == "2":
    exit()
elif program == "3":
    pass

