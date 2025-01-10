class King:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos, board):
        row, col = current_pos
        potential_moves = [      
            (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1),
            (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)
        ]
        valid_moves = [
            move for move in potential_moves
            if 0 <= move[0] < 9 and 0 <= move[1] < 9
        ]
        return valid_moves
        
        
