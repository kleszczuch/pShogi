class Lance:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos, board):
        row, col = current_pos
        moves = []
        if self.color == 'white':
            for r in range(row - 1, -1, -1):
                if board[r][col] == " ":
                    moves.append((r, col))
                elif board[r][col].startswith(self.color[0]):
                    break
                else:
                    moves.append((r, col))
                    break
        elif self.color == 'black':
            for r in range(row + 1, 9):
                if board[r][col] == " ":
                    moves.append((r, col))
                elif board[r][col].startswith(self.color[0]):
                    break
                else:
                    moves.append((r, col))
                    break
        return moves