from game_logic.PiecesMoves.GoldGeneral import GoldGeneral

class Knight:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos, board, promotion):
        row, col = current_pos
        if self.color == 'white':
            promoted_moves = GoldGeneral(color='white')
            if promotion:
                return promoted_moves.move(current_pos, board, promotion)
            else:
                return [(row - 2, col - 1), (row - 2, col + 1)]  # Example moves for white knight
        elif self.color == 'black':
            promoted_moves = GoldGeneral(color='black')
            if promotion:
                return promoted_moves.move(current_pos, board, promotion)
            else:
                return [(row + 2, col - 1), (row + 2, col + 1)]  # Example moves for black knight
            