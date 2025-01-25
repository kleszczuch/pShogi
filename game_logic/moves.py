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
from game_logic.caputuring_and_reviving import del_from_dict
def get_type_color_and_promotion(piece):

    piece_name = piece["piece"]
    color = piece_name[0]  # color 
    rest = piece_name[1:]  # rest 
    if "_" in rest:
        type_of_piece, promotion = rest.split("_") # type_of_piece = type of piece, promotion = promotion
    else:
        type_of_piece = rest
        promotion = None # King and GoldGeneral don't have promotion
    

    color = 'white' if color == 'w' else 'black'
    if promotion == "P":
        promotion = True
    else:
        promotion = False
    piece_classes = { # list of class of pieces
        "Pawn": Pawn,
        "Knight": Knight,
        "Lance": Lance,
        "Silver": SilverGeneral,
        "Gold": GoldGeneral,
        "King": King,
        "Rook": Rook,
        "Bishop": Bishop,
    }
    piece_class = piece_classes.get(type_of_piece) # get class of piece from list
    return  piece_class, color, promotion

def get_revive_pos(game, piece_name): 
    temp_table = []
    enemy_king_color = "w" if piece_name[0] == "b" else "b"
    enemy_king_pos = None
    for row in range(9):
        for col in range(9):
            if game.board[row][col] == f"{enemy_king_color}King":
                enemy_king_pos = (row, col)
                break
        if enemy_king_pos:
            break

    if piece_name.endswith("Pawn"): # There can not be 2 pawns in 1 column and pawn can not check king on revive move
            possible_moves = []
            for col in range(9):
                clear_column = False
                for row in range(9):
                    piece_to_check = game.board[row][col]
                    if piece_to_check == " " :
                        if not clear_column:  
                            if enemy_king_pos and (
                            (enemy_king_color == 'w' and row == enemy_king_pos[0] - 1 and col == enemy_king_pos[1]) or
                            (enemy_king_color == 'b' and row == enemy_king_pos[0] + 1 and col == enemy_king_pos[1])
                            ):
                                continue
                            else:
                                temp_table.append((row, col))
                    elif piece_to_check.startswith(piece_name[0] + "Pawn"):
                        clear_column = True  
                        temp_table.clear()
                        break
                if temp_table:
                    possible_moves.extend(temp_table)
                    temp_table.clear()
    else:
            possible_moves = []
            for row in range(9):
                for col in range(9):
                    if game.board[row][col] == " ":
                        possible_moves.append((row, col))
    return possible_moves


def move_piece(game, selected_piece, end_pos, revive):
    piece_class, color, promotion = get_type_color_and_promotion(selected_piece)
    start_pos = selected_piece["pos"]
    if "_" in selected_piece["piece"]:
        piece_name, promotion = selected_piece["piece"].split("_") #to get promotion from piece name
    else:
        piece_name = selected_piece["piece"] #to get piece name if there is no promotion
        promotion = None
    
    piece = piece_class(color)
    if revive:
        possible_moves = get_revive_pos(game, piece_name)
        if end_pos in possible_moves:
            if want_and_able_to_promote(piece_name, end_pos[0], color, promotion): # check if promotion is possible and wanted
                promoted_piece = f"{piece_name.split('_')[0]}_P" # update piece name to promote 
                game.board[end_pos[0]][end_pos[1]] = promoted_piece
            else:
                game.board[end_pos[0]][end_pos[1]] = selected_piece["piece"]
            if color == "black":
                del_from_dict("black", start_pos) # delete from captured pieces
            else:
                del_from_dict("white", start_pos) # delete from captured pieces
            return True
    else:
        possible_moves = piece.move(start_pos, game.board, promotion)
        can_move, target_piece = is_valid_move(game, color, end_pos, selected_piece)
        
        if end_pos in possible_moves and can_move:
            game.board[start_pos[0]][start_pos[1]] = " "
            if want_and_able_to_promote(piece_name, end_pos[0], color, promotion): # check if promotion is possible and wanted
                promoted_piece = f"{piece_name.split('_')[0]}_P" # update piece name to promote
                game.board[end_pos[0]][end_pos[1]] = promoted_piece
            else:
                game.board[end_pos[0]][end_pos[1]] = selected_piece["piece"]
            if target_piece is not None:
                capture_piece(target_piece)
            return True


def get_all_valid_moves(selected_piece, board): # get all valid moves for selected piece
    piece_class, color, promotion = get_type_color_and_promotion(selected_piece)  
    if not piece_class:
        return []
    piece = piece_class(color)
    return piece.move(selected_piece["pos"], board, promotion)

def is_valid_move(game, color, target_pos, selected_piece): # check if selected move is valid
    if target_pos[0] < 0 or target_pos[0] > 9 or target_pos[1] < 0 or target_pos[1] > 9: # check if target position is on board
        return False, None

    possible_moves = get_all_valid_moves(selected_piece, game.board)
    if target_pos in possible_moves:
        target_piece = game.board[target_pos[0]][target_pos[1]]
        if target_piece == " ":
            return True, None
        if (color == 'white' and target_piece.startswith('b')) or (color == 'black' and target_piece.startswith('w')):
            return True, target_piece
    return False, None