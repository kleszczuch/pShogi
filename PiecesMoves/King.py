class King:
    def __init__(self, color):
        self.color = color

    def move(self, current_pos, board):
        row, col = current_pos
        potential_moves = [
            (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1),
            (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)
        ]

        # Filtruj ruchy w granicach planszy (9x9 dla shogi)
       
        return potential_moves
