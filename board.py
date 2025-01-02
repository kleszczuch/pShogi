class GameState():
    def __init__(self):
        # The board is represented as a 2D array of strings
        # The strings represent the pieces on the board
        # " " represents an empty square
        # board is 9x9
        self.board = [
            ["bLance", "bKnight", "bSilver ", "bGold", "bKing", "bGold", "bSilver", "bKnight", "bLance"],
            [" ", "bRook", " ", " ", " ", " ", " ", "bBishop", " "],
            ["bpawn", "bpawn", "bpawn", "bpawn", "bpawn", "bpawn", "bpawn", "bpawn", "bpawn"],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["wpawn", "wpawn", "wpawn", "wpawn", "wpawn", "wpawn", "wpawn", "wpawn", "wpawn"],
            [" ", "wBishop", " ", " ", " ", " ", " ", "wRook", " "],
            ["wLance", "wKnight", "wSilver ", "wGold", "wKing", "wGold", "wSilver", "wKnight", "wLance"]
        ]
        self.whiteToMove = True
        self.moveLog = []