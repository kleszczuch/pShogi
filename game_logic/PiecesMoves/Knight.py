from game_logic.PiecesMoves.GoldGeneral import GoldGeneral

class Knight:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos, board, promotion):
        row, col = current_pos
        moves = []
        if self.color == 'white':
            promoted_moves = GoldGeneral(color='white')
            if promotion:
                moves.extend(promoted_moves.move(current_pos, board, promotion))
            else:
                potential_moves = [(row - 2, col - 1), (row - 2, col + 1)]
                moves = [move for move in potential_moves if 0 <= move[0] < 9 and 0 <= move[1] < 9]
        elif self.color == 'black':
            promoted_moves = GoldGeneral(color='black')
            if promotion:
                moves.extend(promoted_moves.move(current_pos, board, promotion))
            else:
                potential_moves = [(row + 2, col - 1), (row + 2, col + 1)]
                moves = [move for move in potential_moves if 0 <= move[0] < 9 and 0 <= move[1] < 9]
        return moves