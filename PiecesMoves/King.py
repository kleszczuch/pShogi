class King:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos):
        row, col = current_pos
        moves = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1),
                 (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]
        return moves