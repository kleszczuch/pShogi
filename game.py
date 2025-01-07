import pygame

from PiecesMoves.Pawn import Pawn
from PiecesMoves.Knight import Knight
from PiecesMoves.Lance import Lance
from PiecesMoves.SilverGeneral import SilverGeneral
from PiecesMoves.GoldGeneral import GoldGeneral
from PiecesMoves.King import King
from PiecesMoves.Rook import Rook
from PiecesMoves.Bishop import Bishop

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
                
def is_valid_move(game, color, target_pos):
    target_piece = game.board[target_pos[0]][target_pos[1]]
    if target_piece == " ":
        return True
    if color == 'white' and target_piece.startswith('w'):
        return False
    if color == 'black' and target_piece.startswith('b'):
        return False
    return True

def load_images():
    pieces = [
        "wLance", "wKnight", "wSilver", "wGold", "wKing", "wRook", "wBishop", "wPawn",
        "bLance", "bKnight", "bSilver", "bGold", "bKing", "bRook", "bBishop", "bPawn"
    ]
    images = {}  # dictionary of images to be able to use them in the draw board function
    for piece in pieces:
        images[piece] = pygame.image.load(f"images/{piece}.png")
    return images

def draw_piece(game, piece, row, col, square_size, images):
    if piece in images:
        piece_image = images[piece]
        piece_image = pygame.transform.scale(piece_image, (square_size, square_size))
        game.screen.blit(piece_image, (col * square_size, row * square_size))  # draw a piece on the screen

def main():
    pygame.init()
    WIDTH, HEIGHT = 720, 720
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption('pShogi - Shogi-Dogi')
    timer = pygame.time.Clock()
    fps = 60

    game = GameState()
    game.screen = screen
    images = load_images()

    dragging = False
    selected_piece = None
    square_size = 80

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for piece in game.get_piece_pos():
                    row, col = piece["pos"]
                    piece_rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
                    piece_to_be_deleted = piece["pos"]
                    if piece_rect.collidepoint(mouse_x, mouse_y):
                        dragging = True
                        selected_piece = piece
                        print(f"Selected piece: {selected_piece}")
                        break
            elif event.type == pygame.MOUSEBUTTONUP:
                if dragging:
                    mouse_x, mouse_y = event.pos
                    grid_x = mouse_y // square_size
                    grid_y = mouse_x // square_size
                    print(f"Mouse released at: ({grid_x}, {grid_y})")
                    if 0 <= grid_x < 9 and 0 <= grid_y < 9:
                        piece_name = selected_piece["piece"]
                        color = 'white' if piece_name.startswith('w') else 'black'
                        new_pos = None
                        valid_move = False
                        if piece_name.endswith("Pawn"):
                            pawn = Pawn(color)
                            new_pos = pawn.move(selected_piece["pos"])
                            valid_move = new_pos == (grid_x, grid_y)
                            print(f"Attempting to move {piece_name} from {selected_piece['pos']} to {new_pos}")
                        elif piece_name.endswith("Knight"):
                            knight = Knight(color)
                            new_pos = knight.move(selected_piece["pos"])
                            valid_move = (grid_x, grid_y) in new_pos
                        elif piece_name.endswith("Lance"):
                            lance = Lance(color)
                            new_pos = lance.move(selected_piece["pos"], game.board)
                            valid_move = (grid_x, grid_y) in new_pos
                        elif piece_name.endswith("Silver"):
                            silver = SilverGeneral(color)
                            new_pos = silver.move(selected_piece["pos"])
                            valid_move = (grid_x, grid_y) in new_pos
                        elif piece_name.endswith("Gold"):
                            gold = GoldGeneral(color)
                            new_pos = gold.move(selected_piece["pos"])
                            valid_move = (grid_x, grid_y) in new_pos
                        elif piece_name.endswith("King"):
                            king = King(color)
                            new_pos = king.move(selected_piece["pos"])
                            valid_move = (grid_x, grid_y) in new_pos
                        elif piece_name.endswith("Rook"):
                            rook = Rook(color)
                            new_pos = rook.move(selected_piece["pos"], game.board)
                            valid_move = (grid_x, grid_y) in new_pos
                        elif piece_name.endswith("Bishop"):
                            bishop = Bishop(color)
                            new_pos = bishop.move(selected_piece["pos"], game.board)
                            print(f"Bishop possible moves: {new_pos}")
                            valid_move = (grid_x, grid_y) in new_pos

                        if valid_move and is_valid_move(game, color, (grid_x, grid_y)):
                            print(f"Moved {piece_name} to {(grid_x, grid_y)}")
                            game.board[grid_x][grid_y] = piece_name
                            game.board[piece_to_be_deleted[0]][piece_to_be_deleted[1]] = " "
                        else:
                            print(f"Invalid move for {piece_name} to {(grid_x, grid_y)}")
                        dragging = False
                        selected_piece = None

        screen.fill((255, 255, 255))
        draw_board(game, images)
        pygame.display.flip()
        timer.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()
