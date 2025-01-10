class Knight:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos, board):
        row, col = current_pos
        if self.color == 'white':
            return [(row - 2, col - 1), (row - 2, col + 1)]  # Example moves for white knight
        elif self.color == 'black':
            return [(row + 2, col - 1), (row + 2, col + 1)]  # Example moves for black knight