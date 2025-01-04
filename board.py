import pygame

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

def load_images():
    pieces = [
        "bLance", "bKnight", "bSilver", "bGold", "bKing", "bRook", "bBishop", "bPawn", 
        "wLance", "wKnight", "wSilver", "wGold", "wKing", "wRook", "wBishop", "wPawn"
    ]
    images = {} # dictionary of images to be able to use them in the draw board function
    for piece in pieces:
        images[piece] = pygame.image.load(f"images/{piece}.png")  
    return images

def draw_piece(game, piece, row, col, square_size, images):
    if piece in images:
        piece_image = images[piece]
        piece_image = pygame.transform.scale(piece_image, (square_size, square_size))
        game.screen.blit(piece_image, (col * square_size, row * square_size)) # draw a piece on the screen (blit is a pygame function that draws one image onto another))

def main():
    pygame.init()
    WIDTH, HEIGHT = 720, 720
    screen = pygame.display.set_mode([WIDTH, HEIGHT]) # set the screen size if needed change the values above
    pygame.display.set_caption('pShogi - Shogi-Dogi') #Name of the app
    timer = pygame.time.Clock()
    fps = 60 # frames per second, may be changed in the future to 30 or even less

    game = GameState()
    game.screen = screen
    images = load_images()

    dragging = False
    selected_pawn = None
    square_size = 80

    running = True
    # main game loop, mouse movement is handled here
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse is over the piece and start dragging
                mouse_x, mouse_y = event.pos
                for piece in game.get_piece_pos(): # get the position of all the pieces to check if the mouse is over one of them
                    row, col = piece["pos"]
                    piece_rect = pygame.Rect(
                        col * square_size, row * square_size, square_size, square_size
                    )
                    piece_to_be_deleted = piece["pos"]
                    if piece_rect.collidepoint(mouse_x, mouse_y):
                        dragging = True
                        selected_piece = piece
                        
                        break
                        
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                # end dragging
                if dragging:
                    mouse_x, mouse_y = event.pos# getting mouse position at the end of the event 
                    grid_x = mouse_y // square_size
                    grid_y = mouse_x // square_size
                    if 0 <= grid_x < 9 and 0 <= grid_y < 9: # check if the mouse is over the board
                        # TODO: Add a def of each piece movement
                        # Issue URL: https://github.com/kleszczuch/pShogi/issues/14
                        selected_piece["pos"] = [grid_x, grid_y]
                        piece_name = selected_piece["piece"]
                        game.board[selected_piece["pos"][0]][selected_piece["pos"][1]] = piece_name # move the piece to the new position
                        game.board[piece_to_be_deleted[0]][piece_to_be_deleted[1]] = " " # delete the piece from the old position
                    dragging = False
                    selected_piece= None
            
 
        # draw the current board over the white background
        screen.fill((255, 255, 255))
        draw_board(game, images)
        pygame.display.flip() # update the screen 
        timer.tick(fps) # set the fps to 60 if needed change the FPS value

    pygame.quit()

if __name__ == "__main__":
    main()
