class TickTackToe:
    # Start screen

    # Default layout
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, player1, player2
    player1 = "X"
    player2 = "O"
    a1 = " "
    a2 = " "
    a3 = " "
    b1 = " "
    b2 = " "
    b3 = " "
    c1 = " "
    c2 = " "
    c3 = " "

    def drawBoard():
        print(f"\n\n\n\n\n  | 1 | 2 | 3 |")
        print(f"A | {a1} | {a2} | {a3} |\n   -----------\nB | {b1} | {b2} | {b3} |\n   -----------\nC | {c1} | {c2} | {c3} |")
    def checkWin(player): 
        if a1 == a2 == a3 == player:
            return True
        elif b1 == b2 == b3 == player:
            return True
        elif c1 == c2 == c3 == player:
            return True
        elif a1 == b1 == c1 == player:
            return True
        elif a2 == b2 == c2 == player:
            return True
        elif a3 == b3 == c3 == player:
            return True
        elif a1 == b2 == c3 == player:
            return True
        elif a3 == b2 == c1 == player:
            return True
        else:
            return False
    def checkDraw():
        if a1 != " " and a2 != " " and a3 != " " and b1 != " " and b2 != " " and b3 != " " and c1 != " " and c2 != " " and c3 != " ":
            return True
        else:
            return False
    def restart(): 
        global a1, a2, a3, b1, b2, b3, c1, c2, c3
        a1 = " "
        a2 = " "
        a3 = " "
        b1 = " "
        b2 = " "
        b3 = " "
        c1 = " "
        c2 = " "
        c3 = " "
    def move(player, cell):
        global a1, a2, a3, b1, b2, b3, c1, c2, c3
        if cell == "a1":
            if a1 == " ":
                a1 = player
                return True
            else:
                print("Cell already taken")
                return False
        if cell == "a2":
            if a2 == " ":
                a2 = player
                return True
            else:
                print("Cell already taken")
                return False
        if cell == "a3":
            if a3 == " ":
                a3 = player
                return True
            else:
                print("Cell already taken")
                return False
        if cell == "b1":
            if b1 == " ":
                b1 = player
                return True
            else:
                print("Cell already taken")
                return False
        if cell == "b2":
            if b2 == " ":
                b2 = player
                return True
            else:
                print("Cell already taken")
                return False
        if cell == "b3":
            if b3 == " ":
                b3 = player
                return True
            else:
                print("Cell already taken")
                return False
        if cell == "c1":
            if c1 == " ":
                c1 = player
                return True
            else:
                print("Cell already taken")
                return False
        if cell == "c2":
            if c2 == " ":
                c2 = player
                return True
            else:
                print("Cell already taken")
                return False
        if cell == "c3":
            if c3 == " ":
                c3 = player
                return True
            else:
                print("Cell already taken")
                return False
def move2(player, cell):
        if cell == "a1":
            if a1 == " ":
                a1 = player
                return True
            else:
                print("Cell already taken")
                return False
        if cell == "a2":
            if a2 == " ":
                a2 = player
                return True
            else:
                print("Cell already taken")
                return False
        if cell == "a3":
            if a3 == " ":
                a3 = player
                return True
            else:
                print("Cell already taken")
                return False
        if cell == "b1":
            if b1 == " ":
                b1 = player
                return True
            else:
                print("Cell already taken")
                return False
        if cell == "b2":
            if b2 == " ":
                b2 = player
                return True
            else:
                print("Cell already taken")
                return False