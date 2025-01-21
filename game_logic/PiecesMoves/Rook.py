from game_logic.PiecesMoves.King import King
promoted_moves = King(color = 'white')
class Rook:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos, board,promotion):
        row, col = current_pos
        moves = []
        if promotion:
            moves = (promoted_moves.move(current_pos, board, promotion)) # Promoted rook moves appends with king moves
        # Check vertical moves
        for r in range(row - 1, -1, -1):
            if board[r][col] == " ":
                moves.append((r, col))
            elif board[r][col].startswith(self.color[0]):
                break
            else:
                moves.append((r, col))
                break
        for r in range(row + 1, 9):
            if board[r][col] == " ":
                moves.append((r, col))
            elif board[r][col].startswith(self.color[0]):
                break
            else:
                moves.append((r, col))
                break
        # Check horizontal moves
        for c in range(col - 1, -1, -1):
            if board[row][c] == " ":
                moves.append((row, c))
            elif board[row][c].startswith(self.color[0]):
                break
            else:
                moves.append((row, c))
                break
        for c in range(col + 1, 9):
            if board[row][c] == " ":
                moves.append((row, c))
            elif board[row][c].startswith(self.color[0]):
                break
            else:
                moves.append((row, c))
                break
        
        return moves