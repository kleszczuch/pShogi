import pygame

from PiecesMoves.Pawn import Pawn
from PiecesMoves.Knight import Knight
from PiecesMoves.Lance import Lance
from PiecesMoves.SilverGeneral import SilverGeneral
from PiecesMoves.GoldGeneral import GoldGeneral
from PiecesMoves.King import King
from PiecesMoves.Rook import Rook
from PiecesMoves.Bishop import Bishop

WIDTH, HEIGHT = 900, 720
screen = pygame.display.set_mode([WIDTH, HEIGHT])
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class GameState:
    
    def __init__(self):
        self.board = [
            ["bLance", "bKnight", "bSilver", "bGold", "bKing", "bGold", "bSilver", "bKnight", "bLance"],
            [" ", "bRook", " ", " ", " ", " ", " ", "bBishop", " "],
            ["bPawn", "bPawn", "bPawn", "bPawn", "bPawn", "bPawn", "bPawn", "bPawn", "bPawn"],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["wPawn", "wPawn", "wPawn", "wPawn", "wPawn", "wPawn", "wPawn", "wPawn", "wPawn"],
            [" ", "wBishop", " ", " ", " ", " ", " ", "wRook", " "],
            ["wLance", "wKnight", "wSilver", "wGold", "wKing", "wGold", "wSilver", "wKnight", "wLance"]
        ]

    def get_current_game_state(self):
        return self.board # to be able to refresh the game state

    def get_piece_pos(self):
        pieces = []
        # Loop through the board and get the position of each piece and add them to the pieces list - this is needed to be able to move them around
        for row in range(9):
            for col in range(9):
                piece = self.board[row][col]
                if piece != " ":
                    pieces.append({
                        "piece": piece,
                        "pos": [row, col]
                    })
        return pieces
def load_images():
    pieces = [
        "wLance", "wKnight", "wSilver", "wGold", "wKing", "wRook", "wBishop", "wPawn",
        "bLance", "bKnight", "bSilver", "bGold", "bKing", "bRook", "bBishop", "bPawn"
    ]
    images = {}  # dictionary of images to be able to use them in the draw board function
    for piece in pieces:
        images[piece] = pygame.image.load(f"images/{piece}.png")
    return images


def draw_board(game, images):
    background_path = "images/background.png"
    background = pygame.image.load(background_path) # load the background image
   
    square_size = 80
    for row in range(9):
        for col in range(9):
            game.screen.blit(background, (col * square_size, row * square_size)) # adding background to every square
            pygame.draw.rect( # painting boarder
                game.screen,
                (0, 0, 0),  
                pygame.Rect(col * square_size, row * square_size, square_size, square_size), 2
            )
            # Rysuj pionki
            piece = game.board[row][col]
            if piece != " ":
                draw_piece(game, piece, row, col, square_size, images)

def draw_matrices(game):
    background_path = "images/backbackground.png"
    background = pygame.image.load(background_path) # load the background image
    square_size = 80
    for row in range(9):
        for col in range(2):
            game.screen.blit(background, (col * square_size, row * square_size)) # adding background to every square
            pygame.draw.rect( # painting boarder
                game.screen,
                (0, 0, 0),  
                pygame.Rect(col * square_size, row * square_size, square_size, square_size), 2
            )
def draw_scene():
    screen.fill(WHITE)
    draw_matrices()
    draw_board()

def draw_piece(game, piece, row, col, square_size, images):
    if piece in images:
        piece_image = pygame.transform.scale(images[piece], (square_size, square_size))
        game.screen.blit(piece_image, (col * square_size, row * square_size))  # draw a piece on the screen
                
def is_valid_move(game, color, target_pos):
    target_piece = game.board[target_pos[0]][target_pos[1]]
    if target_piece == " ":
        return True
    if color == 'white' and target_piece.startswith('w'):
        return False
    if color == 'black' and target_piece.startswith('b'):
        return False
    return True

def get_all_valid_moves(piece_name, pos, board):
    type, color = piece_name[1:], piece_name[0]
    color = 'white' if color == 'w' else 'black'

    piece_classes = {
        "Pawn": Pawn,
        "Knight": Knight,
        "Lance": Lance,
        "Silver": SilverGeneral,
        "Gold": GoldGeneral,
        "King": King,
        "Rook": Rook,
        "Bishop": Bishop
    }

    piece_class = piece_classes.get(type)
    if not piece_class:
        return []

    piece = piece_class(color)
    return piece.move(pos, board)

def simulate_move(board, start_pos, end_pos):
    """
    Symuluje ruch figury na planszy.
    board: lista reprezentująca planszę
    start_pos: pozycja startowa figury
    end_pos: pozycja docelowa figury
    """
    if 0 <= end_pos[0] < 9 and 0 <= end_pos[1] < 9:
        piece = board[start_pos[0]][start_pos[1]]
        board[start_pos[0]][start_pos[1]] = " "
        board[end_pos[0]][end_pos[1]] = piece   

def is_in_check(board, king_color):
    king_pos = None
    for row in range(9):
        for col in range(9):
            if board[row][col] == f"{king_color}King":
                king_pos = (row, col)
                break
    if not king_pos:
        raise ValueError("Nie znaleziono króla na planszy!")

    enemy_color = "b" if king_color == "w" else "w"
    print(f"Sprawdzanie szacha dla króla {king_color} na pozycji {king_pos}")
    for row in range(9):
        for col in range(9):
            piece = board[row][col]
            if piece.startswith(enemy_color):
                possible_moves = get_all_valid_moves(piece, (row, col), board)
                print(f"Figura {piece} na pozycji {(row, col)} może ruszyć na {possible_moves}")
                if king_pos in possible_moves:
                    return True
    return False

def is_checkmate(board, king_color):
    """
    Sprawdza, czy król jest w szach-macie.
    """
    if not is_in_check(board, king_color):
        return False

    for row in range(9):
        for col in range(9):
            piece = board[row][col]
            if piece.startswith(king_color):
                # Dla każdej figury sprawdź, czy ma legalne ruchy
                valid_moves = get_all_valid_moves(piece, (row, col), board if piece.notendswith("King") else [])
                for move in valid_moves:
                    if 0 <= move[0] < 9 and 0 <= move[1] < 9:  # Sprawdź, czy ruch jest w granicach planszy
                        temp_board = [row[:] for row in board]  # Skopiuj planszę
                        simulate_move(temp_board, (row, col), move)
                        if not is_in_check(temp_board, king_color):
                            return False
    return True    
  
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


def main():
    pygame.init()
    pygame.display.set_caption('pShogi - Shogi-Dogi')
    timer = pygame.time.Clock()
    fps = 60

    game = GameState()
    game.screen = screen
    images = load_images()

    dragging = False
    selected_piece = None
    square_size = 80
    turn = 'w'

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                grid_x = mouse_y // square_size
                grid_y = mouse_x // square_size
                for piece in game.get_piece_pos():
                    if piece["pos"] == [grid_x, grid_y]:
                        if piece["piece"][0] == turn:
                            dragging = True
                            selected_piece = piece
                            print(f"Selected piece: {selected_piece}")
                        break

            elif event.type == pygame.MOUSEBUTTONUP:
                if dragging and selected_piece:
                    mouse_x, mouse_y = event.pos
                    grid_x = mouse_y // square_size
                    grid_y = mouse_x // square_size
                    end_pos = (grid_x, grid_y)

                    print(f"Attempting to move to {end_pos}")
                    if move_piece(game, selected_piece, end_pos):
                        turn = 'b' if turn == 'w' else 'w'
                        print(f"Moved {selected_piece['piece']} to {end_pos}")
                    else:
                        print(f"Move failed for {selected_piece['piece']} to {end_pos}")
                    
                    dragging = False
                    selected_piece = None
        
                    if is_in_check(game.board, 'w'):
                        print("White king is in check!")
                    if is_in_check(game.board, 'b'):
                        print("Black king is in check!")
        screen.fill(WHITE)
        draw_board(game, images)
        pygame.display.flip()
        timer.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    main()

