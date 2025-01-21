from game_logic.PiecesMoves.King import King
promoted_moves = King(color='white')
class Bishop:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos, board, promotion):

        row, col = current_pos
        moves = []
        if promotion:
            moves = (promoted_moves.move(current_pos, board,promotion)) # Promoted Bishop moves appends with king moves

        # Check diagonal moves
        for i in range(1, 9):
            if row + i < 9 and col + i < 9:
                if board[row + i][col + i] == " ":
                    moves.append((row + i, col + i))
                elif board[row + i][col + i].startswith(self.color[0]):
                    break
                else:
                    moves.append((row + i, col + i))
                    break
            else:
                break

        for i in range(1, 9):
            if row - i >= 0 and col - i >= 0:
                if board[row - i][col - i] == " ":
                    moves.append((row - i, col - i))
                elif board[row - i][col - i].startswith(self.color[0]):
                    break
                else:
                    moves.append((row - i, col - i))
                    break
            else:
                break

        for i in range(1, 9):
            if row + i < 9 and col - i >= 0:
                if board[row + i][col - i] == " ":
                    moves.append((row + i, col - i))
                elif board[row + i][col - i].startswith(self.color[0]):
                    break
                else:
                    moves.append((row + i, col - i))
                    break
            else:
                break

        for i in range(1, 9):
            if row - i >= 0 and col + i < 9:
                if board[row - i][col + i] == " ":
                    moves.append((row - i, col + i))
                elif board[row - i][col + i].startswith(self.color[0]):
                    break
                else:
                    moves.append((row - i, col + i))
                    break
            else:
                break
        
        return moves