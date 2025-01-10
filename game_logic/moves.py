from game_logic.PiecesMoves.Pawn import Pawn
from game_logic.PiecesMoves.Knight import Knight
from game_logic.PiecesMoves.Lance import Lance
from game_logic.PiecesMoves.SilverGeneral import SilverGeneral
from game_logic.PiecesMoves.GoldGeneral import GoldGeneral
from game_logic.PiecesMoves.King import King
from game_logic.PiecesMoves.Rook import Rook
from game_logic.PiecesMoves.Bishop import Bishop

import pygame

def move_piece(game, selected_piece, end_pos):
    piece_name = selected_piece["piece"]
    start_pos = selected_piece["pos"]
    color = 'white' if piece_name.startswith('w') else 'black'

    piece_classes = {
        "Pawn": Pawn,
        "Knight": Knight,
        "Lance": Lance,
        "Silver": SilverGeneral,
        "Gold": GoldGeneral,
        "King": King,
        "Rook": Rook,
        "Bishop": Bishop,
    }

    piece_type = piece_name[1:]  # Get piece type, e.g., "Pawn", "Knight"
    piece_class = piece_classes.get(piece_type)
 
    piece = piece_class(color)
    possible_moves = piece.move(start_pos, game.board)
    if end_pos in possible_moves:
        # Perform the move
        game.board[start_pos[0]][start_pos[1]] = " "
        game.board[end_pos[0]][end_pos[1]] = piece_name
        return True

    print(f"Invalid move for {piece_name} to {end_pos}")
    return False

def get_all_valid_moves(selected_piece, board):
    piece_name = selected_piece['piece']
    start_pos = selected_piece['pos']
    color = 'white' if piece_name.startswith('w') else 'black'
    piece_type = piece_name[1:]
    piece_classes = {
        "Pawn": Pawn,
        "Knight": Knight,
        "Lance": Lance,
        "Silver": SilverGeneral,
        "Gold": GoldGeneral,
        "King": King,
        "Rook": Rook,
        "Bishop": Bishop,
    }

    piece_class = piece_classes.get(piece_type)
    if not piece_class:
        return []
    piece = piece_class(color)
    return piece.move(start_pos, board)
# sprawdzic czy to wogole potrzebne
def is_valid_move(game, color, target_pos, selected_piece):
    piece_name = selected_piece["piece"]
    start_pos = selected_piece["pos"]
    possible_moves = get_all_valid_moves(piece_name, start_pos, game.board)
    if target_pos in possible_moves:
        target_piece = game.board[target_pos[0]][target_pos[1]]
        if target_piece == " ":
            return True
        if (color == 'white' and target_piece.startswith('b')) or (color == 'black' and target_piece.startswith('w')):
            return True
    return False