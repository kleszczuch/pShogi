from game_logic.PiecesMoves.GoldGeneral import GoldGeneral

class Pawn:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos, board, promotion):
        moves = []
        row, col = current_pos
        
        # Jeśli pionek jest promowany
        if promotion:
            promoted_moves = GoldGeneral(color=self.color) 
            moves.extend(promoted_moves.move(current_pos, board, promotion))
        else:
            if self.color == 'white':
                move = (row - 1, col) 
                moves.append(move)
            elif self.color == 'black':
                move = (row + 1, col)
                moves.append(move)

        return moves