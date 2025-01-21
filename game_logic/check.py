
import pygame
from game_logic.moves import get_all_valid_moves
from game_logic.PiecesMoves.Pawn import Pawn
from game_logic.PiecesMoves.Knight import Knight
from game_logic.PiecesMoves.Lance import Lance
from game_logic.PiecesMoves.SilverGeneral import SilverGeneral
from game_logic.PiecesMoves.GoldGeneral import GoldGeneral
from game_logic.PiecesMoves.King import King
from game_logic.PiecesMoves.Rook import Rook
from game_logic.PiecesMoves.Bishop import Bishop

def is_in_check(board, king_color, game):
    king_pos = None
    isWin = False
    for row in range(9):
        for col in range(9):
            if board[row][col] == f"{king_color}King":
                king_pos = (row, col)
                break
    if not king_pos:
        isWin = True
        if king_color == "w":
           winComunicate = (0,1)
        else:
            winComunicate = (14,1)
        return False, winComunicate, isWin

    enemy_color = "b" if king_color == "w" else "w"
    print(f"Sprawdzanie szacha dla króla {king_color} na pozycji {king_pos}")
    
    for row in range(9):
        for col in range(9):
            piece = board[row][col]
            if piece.startswith(enemy_color):
                selected_piece = {"piece": piece, "pos": (row, col)} 
                possible_moves = get_all_valid_moves(selected_piece, board)  
                if king_pos in possible_moves:
                    return True,king_pos, isWin 
    return False,king_pos, isWin

def is_checkmate(board, king_color): # TODO: implement this function
    if not is_in_check(board, king_color):
        return False

    for row in range(9):
        for col in range(9):
            piece = board[row][col]
            if piece.startswith(king_color):
                valid_moves = get_all_valid_moves(piece, (row, col), board if piece.notendswith("King") else [])
                for move in valid_moves:
                    if 0 <= move[0] < 9 and 0 <= move[1] < 9:  
                        temp_board = [row[:] for row in board] 
                        simulate_move(temp_board, (row, col), move)
                        if not is_in_check(temp_board, king_color):
                            return False
    return True    

def simulate_move(board, start_pos, end_pos):
    if 0 <= end_pos[0] < 9 and 0 <= end_pos[1] < 9:
        piece = board[start_pos[0]][start_pos[1]]
        board[start_pos[0]][start_pos[1]] = " "
        board[end_pos[0]][end_pos[1]] = piece   