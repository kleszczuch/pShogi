from game_logic.PiecesMoves.Pawn import Pawn
from game_logic.PiecesMoves.Knight import Knight
from game_logic.PiecesMoves.Lance import Lance
from game_logic.PiecesMoves.SilverGeneral import SilverGeneral
from game_logic.PiecesMoves.GoldGeneral import GoldGeneral
from game_logic.PiecesMoves.King import King
from game_logic.PiecesMoves.Rook import Rook
from game_logic.PiecesMoves.Bishop import Bishop
from game_logic.caputuring_and_reviving import capture_piece


def get_type_of_piece_and_color(piece):

    piece_name = piece["piece"]
    start_pos = piece["pos"]
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
    return  piece_class, color

def move_piece(game, selected_piece, end_pos):
    piece_class, color = get_type_of_piece_and_color(selected_piece) 
    start_pos = selected_piece["pos"]

    piece = piece_class(color)
    possible_moves = piece.move(start_pos, game.board)
    can_move, target_piece = is_valid_move(game, color, end_pos, selected_piece)
    if end_pos in possible_moves and can_move:
        # Perform the move
        game.board[start_pos[0]][start_pos[1]] = " "
        game.board[end_pos[0]][end_pos[1]] = selected_piece["piece"]
        if target_piece is not None:
            capture_piece(target_piece)
        return True

def get_all_valid_moves(selected_piece, board):
    piece_class, color = get_type_of_piece_and_color(selected_piece)  
    if not piece_class:
        return []
    piece = piece_class(color)
    return piece.move(selected_piece["pos"], board)

def is_valid_move(game, color, target_pos, selected_piece):
    piece_name = selected_piece["piece"]
    start_pos = selected_piece["pos"]
    possible_moves = get_all_valid_moves(selected_piece, game.board)
    if target_pos in possible_moves:
        target_piece = game.board[target_pos[0]][target_pos[1]]
        if target_piece == " ":
            return True, None
        if (color == 'white' and target_piece.startswith('b')) or (color == 'black' and target_piece.startswith('w')):
            return True, target_piece
    return False, None