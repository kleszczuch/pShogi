from game_logic.PiecesMoves.GoldGeneral import GoldGeneral

class Lance:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos, board, promotion):
        row, col = current_pos
        moves = []
        if self.color == 'white':
            general = GoldGeneral(color = 'white')
            if promotion:
                return general.move(current_pos, board, promotion) # Promoted pieces can move like a GoldGeneral
            else:
                for r in range(row - 1, -1, -1):
                    if board[r][col] == " ":
                        moves.append((r, col))
                    elif board[r][col].startswith(self.color[0]):
                        break
                    else:
                        moves.append((r, col))
                        break
        elif self.color == 'black':
            general = GoldGeneral(color = 'black')
            if promotion:
                return general.move(current_pos, board, promotion)
            else:
                for r in range(row + 1, 9):
                    if board[r][col] == " ":
                        moves.append((r, col))
                    elif board[r][col].startswith(self.color[0]):
                        break
                    else:
                        moves.append((r, col))
                        break
        return moves