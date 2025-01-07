class Pawn:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos):
        row, col = current_pos
        if self.color == 'white':
            return (row - 1, col)  # Move one square forward for white
        elif self.color == 'black':
            return (row + 1, col)  # Move one square forward for black