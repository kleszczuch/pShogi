import pygame
from game_logic.moves import move_piece
from game_logic.check import is_in_check
from game_logic.moves import get_all_valid_moves
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

def draw_board(game, images, selected_piece=None):
    background_path = "images/background.png"
    background = pygame.image.load(background_path) 
    to_move_path = "images/whereMove.png"
    to_move = pygame.image.load(to_move_path)
    possible_moves = []
    square_size = 80
    to_move = pygame.transform.scale(to_move, (square_size, square_size)) 
    for row in range(9):
        for col in range(9):
            game.screen.blit(background, (col * square_size, row * square_size)) # adding background to every square
            pygame.draw.rect( # painting boarder
                game.screen,
                (0, 0, 0),  
                pygame.Rect(col * square_size, row * square_size, square_size, square_size), 2
            )   
            piece = game.board[row][col]
            if piece != " ":
                draw_piece(game, piece, row, col, square_size, images)
            if selected_piece:
                possible_moves = get_all_valid_moves(selected_piece, game.board)
            for move in possible_moves:                    
                    game.screen.blit(to_move, (move[0] * square_size, move[1] * square_size))
    

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

def draw_scene(game, images):
    screen.fill(WHITE)
    draw_matrices(game)
    draw_board(game, images) # do not work
    # TODO: Make it work
    # Issue URL: https://github.com/kleszczuch/pShogi/issues/21

def draw_piece(game, piece, row, col, square_size, images):
    if piece in images:
        piece_image = pygame.transform.scale(images[piece], (square_size, square_size))
        game.screen.blit(piece_image, (col * square_size, row * square_size))  # draw a piece on the screen               

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
    firstTime = True
    while running:
 
        pygame.display.flip()

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
                            draw_board(game, images, selected_piece)
                            print(f"Selected piece: {selected_piece}")
                            pygame.display.flip()
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
                    pygame.display.flip()
        screen.fill(WHITE)
        draw_scene(game, images)
        
        timer.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()

