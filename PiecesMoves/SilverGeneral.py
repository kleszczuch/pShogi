class SilverGeneral:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos):
        row, col = current_pos
        moves = []
        if self.color == 'white':
            moves = [(row - 1, col), (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]
        elif self.color == 'black':
            moves = [(row + 1, col), (row + 1, col - 1), (row + 1, col + 1), (row - 1, col - 1), (row - 1, col + 1)]
        return moves
