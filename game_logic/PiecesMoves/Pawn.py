from game_logic.PiecesMoves.GoldGeneral import GoldGeneral

class Pawn:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos, board, promotion):
        moves = []
        row, col = current_pos
        
        # Jeśli pionek jest promowany
        if promotion:
            promoted_moves = GoldGeneral(color=self.color)  # Tworzymy instancję GoldGeneral
            moves.extend(promoted_moves.move(current_pos, board, promotion))  # Dodajemy ruchy z GoldGeneral
        else:
            # Jeśli pionek nie jest promowany, normalnie przesuwa się o 1 pole
            if self.color == 'white':
                move = (row - 1, col)  # Ruch białego pionka
                moves.append(move)
            elif self.color == 'black':
                move = (row + 1, col)  # Ruch czarnego pionka
                moves.append(move)

        return moves