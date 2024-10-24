from computer import Computer


class ComputerTest:
    def __init__(self) -> None:    
        computer = Computer()

        computer.drawBoard()
        computer.move("X", "1")
        computer.drawBoard()
        computer.move("O", "2")
        computer.drawBoard()
        computer.move("X", "3")
        computer.drawBoard
        computer.move("O", "4")
        computer.checkDraw()
        computer.checkWin("X")
        computer.checkIfOpponentCloseToWin("X")
        computer.computerMove("X")

ComputerTest()