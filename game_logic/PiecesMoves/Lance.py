from game_logic.PiecesMoves.GoldGeneral import GoldGeneral

class Lance:
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
                for r in range(row - 1, -1, -1):
                    if board[r][col] == " ":
                        moves.append((r, col))
                    elif board[r][col].startswith(self.color[0]):
                        break
                    else:
                        moves.append((r, col))
                        break
        elif self.color == 'black':
            promoted_moves = GoldGeneral(color='black')
            if promotion:
                moves.extend(promoted_moves.move(current_pos, board, promotion))
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