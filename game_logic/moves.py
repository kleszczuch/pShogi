from game_logic.PiecesMoves.Pawn import Pawn
from game_logic.PiecesMoves.Knight import Knight
from game_logic.PiecesMoves.Lance import Lance
from game_logic.PiecesMoves.SilverGeneral import SilverGeneral
from game_logic.PiecesMoves.GoldGeneral import GoldGeneral
from game_logic.PiecesMoves.King import King
from game_logic.PiecesMoves.Rook import Rook
from game_logic.PiecesMoves.Bishop import Bishop
from game_logic.caputuring_and_reviving import capture_piece
from game_logic.promotion import want_and_able_to_promote

def get_type_color_and_promotion(piece):

    piece_name = piece["piece"]
    color = piece_name[0]  # color 
    rest = piece_name[1:]  # rest 
    if "_" in rest:
        type_of_piece, promotion = rest.split("_") # type_of_piece = type of piece, promotion = promotion
    else:
        type_of_piece = rest
        promotion = None  # Brak wartości po "_"
    

    color = 'white' if color == 'w' else 'black'
    if promotion == "P":
        promotion = True
    else:
        promotion = False
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
    piece_class = piece_classes.get(type_of_piece)
    return  piece_class, color, promotion

def move_piece(game, selected_piece, end_pos):
    piece_class, color, promotion = get_type_color_and_promotion(selected_piece)
    start_pos = selected_piece["pos"]
    if "_" in selected_piece["piece"]:
        piece_name, promotion = selected_piece["piece"].split("_")
    else:
        piece_name = selected_piece["piece"]
        promotion = None
    
    piece = piece_class(color)
    possible_moves = piece.move(start_pos, game.board, promotion)
    can_move, target_piece = is_valid_move(game, color, end_pos, selected_piece)
    
    if end_pos in possible_moves and can_move:
        # Wykonaj ruch
        game.board[start_pos[0]][start_pos[1]] = " "

        # Obsługuje promocję, jeżeli jest możliwa
        if want_and_able_to_promote(piece_name, end_pos[0], color, promotion):
            # Zaktualizuj nazwę figury po promocji (np. pionek na złotego generała)
            promoted_piece = f"{piece_name.split('_')[0]}_P"
            print(f"Promoted to {promoted_piece}")
            game.board[end_pos[0]][end_pos[1]] = promoted_piece
        else:
            game.board[end_pos[0]][end_pos[1]] = selected_piece["piece"]

        # Sprawdzenie czy na docelowym polu jest figura, którą należy zbić
        if target_piece is not None:
            capture_piece(target_piece)
        return True


def get_all_valid_moves(selected_piece, board):
    piece_class, color, promotion = get_type_color_and_promotion(selected_piece)  
    if not piece_class:
        return []
    piece = piece_class(color)
    return piece.move(selected_piece["pos"], board, promotion)

def is_valid_move(game, color, target_pos, selected_piece):
    piece_name = selected_piece["piece"]
    start_pos = selected_piece["pos"]
    
    # Sprawdzanie, czy target_pos znajduje się w obrębie planszy (od 0 do 9)
    if target_pos[0] < 0 or target_pos[0] > 9 or target_pos[1] < 0 or target_pos[1] > 9:
        return False, None

    possible_moves = get_all_valid_moves(selected_piece, game.board)
    print(f"Possible moves in get all valid: {possible_moves}")
    print(f"Target pos: {target_pos}")
    if target_pos in possible_moves:
        print (f"Target pos in possible moves: {target_pos}")
        target_piece = game.board[target_pos[0]][target_pos[1]]
        if target_piece == " ":
            return True, None
        if (color == 'white' and target_piece.startswith('b')) or (color == 'black' and target_piece.startswith('w')):
            return True, target_piece
    return False, None