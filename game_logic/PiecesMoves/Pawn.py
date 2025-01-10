class Pawn:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos, board):
        move = (0,0)
        row, col = current_pos
        if self.color == 'white':
            move = (row - 1, col)  # Move one square forward for white
        elif self.color == 'black':
            move = (row + 1, col)  # Move one square forward for black
        return [move]