import pygame
from game_logic.moves import move_piece, get_type_of_piece_and_color, is_valid_move
from game_logic.check import is_in_check, winner
from game_logic.caputuring_and_reviving import get_captured_by_black, get_captured_by_white

# it may be not needed but can not think what couses it/ game works well 
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='pygame')

WIDTH, HEIGHT = 1200, 720
screen = pygame.display.set_mode([WIDTH, HEIGHT], pygame.SRCALPHA)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
TRANSCULCENT_RED = (255, 0, 0, 128)
square_size = 80

class GameState:

# NPY - Not Promoted Yet
# P - Promoted
    
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

def draw_board(game, images, selected_piece=None):
    background_path = "images/background.png"
    background = pygame.image.load(background_path)
    possible_moves = []
    
    background = pygame.transform.scale(background, (square_size, square_size))
    # Rysowanie głównej planszy (środkowej)
    for row in range(9):
        for col in range(9):
            x = (col + 3) * square_size  # Przesunięcie planszy o dwie kolumny w prawo
            y = row * square_size
            game.screen.blit(background, (x, y))
            pygame.draw.rect(
                game.screen,
                (0, 0, 0),
                pygame.Rect(x, y, square_size, square_size), 2
            )
            piece = game.board[row][col]
            if piece != " ":
                draw_piece(game, piece, row, col + 3, square_size, images)
    
    # Pokazywanie możliwych ruchów dla wybranego pionka
    if selected_piece:
        piece_name = selected_piece["piece"]
        start_pos = selected_piece["pos"]
        piece_class, color = get_type_of_piece_and_color(selected_piece)
        piece = piece_class(color)
        possible_moves = piece.move(start_pos, game.board)
        
    for move in possible_moves:
        is_valid, target_piece = is_valid_move(game, color, move, selected_piece)
        if is_valid:
            row, col = move
            x = (col + 3) * square_size + square_size // 2
            y = row * square_size + square_size // 2
            pygame.draw.circle(
                game.screen,
                (0, 255, 0),
                (x, y),
                square_size // 6
            )

def draw_matrices(game, turn):
    background_path = "images/backbackground.png"
    background = pygame.image.load(background_path)
    white_player_path = "images/wPlayer.jpg"
    black_player_path = "images/bPlayer.jpg"
    white_player = pygame.image.load(white_player_path)
    black_player = pygame.image.load(black_player_path)
    black_player = pygame.transform.scale(black_player, (square_size, square_size))
    white_player = pygame.transform.scale(white_player, (square_size, square_size))
    turn_path = "images/turn.jpg"
    turnIMG = pygame.image.load(turn_path)
    turnIMG = pygame.transform.scale(turnIMG, (square_size, square_size))
    images = load_images()
    
    # Lewe kolumny
    for row in range(9):
        for col in range(3):
            x = col * square_size
            y = row * square_size
            if (row == 0 and col == 0):
                game.screen.blit(white_player, (x, y))
            elif (row == 0 and col == 1 and turn == 'w'):
                game.screen.blit(turnIMG, (x, y))
            else:                
                game.screen.blit(background, (x, y))
            pygame.draw.rect(
                game.screen,
                (0, 0, 0),
                pygame.Rect(x, y, square_size, square_size), 1
            )
    # Pionki na lewej kolumnie
    white_capture = get_captured_by_white()
    for pos, piece in white_capture.items():
        if piece["piece"] is not None:
            draw_piece(game, piece["piece"], piece["pos"][1], piece["pos"][0], square_size, images)         
            

    # Prawe kolumny
    for row in range(9):
        for col in range(3):
            x = (col +12) * square_size
            y = row * square_size
            if (row == 0 and col == 2):
                game.screen.blit(black_player, (x, y))
            elif (row == 0 and col == 1 and turn == 'b'):
                game.screen.blit(turnIMG, (x, y))
            else:         
                game.screen.blit(background, (x, y))
            pygame.draw.rect(
                game.screen,
                (0, 0, 0),
                pygame.Rect(x, y, square_size, square_size), 1
            )

    black_capture = get_captured_by_black()
    for pos, piece in black_capture.items():
        if piece["piece"] is not None:
            draw_piece(game, piece["piece"], piece["pos"][1], piece["pos"][0], square_size, images)        
            
def draw_scene(game, images, turn):
    screen.fill((255, 255, 255))  # Białe tło
    draw_matrices(game, turn)  # Rysowanie bocznych kolumn
    draw_board(game, images)  # Rysowanie głównej planszy


def draw_piece(game, piece, row, col, square_size, images):
    if piece in images:
        piece_image = pygame.transform.scale(images[piece], (square_size, square_size))
        game.screen.blit(piece_image, (col * square_size, row * square_size))  # draw a piece on the screen           

def highlight_tile(row, col,color):
    col = col+3
    col = col * square_size
    row = row * square_size
    pygame.draw.rect(screen, color, (col, row, square_size, square_size), 2)  # Grubsza krawędź dla podświetlenia


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
    after_move = False
    running = True
    firstTime = True
    ischeck = ""
    isWwin = False
    isWbin = False
    isWin = False
    while running:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if firstTime:
            pygame.display.flip()
          
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
            if not isWin:    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    firstTime = False
                    
                    grid_x = mouse_y  // square_size
                    grid_y = mouse_x  // square_size - 3
                    for piece in game.get_piece_pos():
                        if piece["pos"] == [grid_x , grid_y]:
                            if piece["piece"][0] == turn:
                                dragging = True
                                selected_piece = piece
                                draw_board(game, images, selected_piece)
                                print(f"Selected piece: {selected_piece}")
                                pygame.display.flip()
                            break

                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragging and selected_piece:
                        grid_x = mouse_y // square_size
                        grid_y = mouse_x // square_size - 3
                        end_pos = (grid_x, grid_y)

                        print(f"Attempting to move to {end_pos}")
                        if move_piece(game, selected_piece, end_pos):
                            turn = 'b' if turn == 'w' else 'w'
                            
                            print(f"Moved {selected_piece['piece']} to {end_pos}")
                        else:
                            print(f"Move failed for {selected_piece['piece']} to {end_pos}")
                        
                        dragging = False
                        selected_piece = None
                        wCheckKing, wking_pos, isWwin= is_in_check(game.board, 'w', game)    
                        bCheckKing, bking_pos, isWbin = is_in_check(game.board, 'b', game)
                        if wCheckKing: 
                            ischeck = "White"
                        elif bCheckKing:
                            ischeck = "Black"   
                        else:
                            ischeck = ""
                        after_move = True    
                         
        screen.fill((255, 255, 255, 0))
        draw_scene(game, images, turn)
        if ischeck == "White":
            highlight_tile(wking_pos[0],wking_pos[1], TRANSCULCENT_RED) 
        elif ischeck == "Black":
            highlight_tile(bking_pos[0],bking_pos[1], TRANSCULCENT_RED)
        elif isWwin and isWin == False:
            winner(game, "w")
            pygame.display.flip()
            isWin = True
        elif isWbin and isWin == False:
            winner(game, "b")
            pygame.display.flip()
            isWin = True
        if after_move: 
            pygame.display.flip()
            after_move = False
        timer.tick(fps)
    pygame.quit()

if __name__ == "__main__":
    main()

