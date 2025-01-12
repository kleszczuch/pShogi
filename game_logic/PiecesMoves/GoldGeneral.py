class GoldGeneral:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos, board):
        row, col = current_pos
        moves = []
        if self.color == 'white':
            moves = [(row - 1, col), (row - 1, col - 1), (row - 1, col + 1), (row, col - 1), (row, col + 1), (row + 1, col)]
        elif self.color == 'black':
            moves = [(row + 1, col), (row + 1, col - 1), (row + 1, col + 1), (row, col - 1), (row, col + 1), (row - 1, col)]
        moves = [move for move in moves if 0 <= move[0] < 9 and 0 <= move[1] < 9]
        return moves