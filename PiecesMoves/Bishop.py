class Bishop:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos, board):
        row, col = current_pos
        moves = []
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

        print(f"Bishop at ({row}, {col}) possible moves: {moves}")
        return moves