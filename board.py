import pygame

class GameState():
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
        
    pygame.init()
    WIDTH = 720
    HEIGHT = 720

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display. set_caption('pShogi')   
    

    timer = pygame.time.Clock()
    fps = 60 

def load_images():
    pieces = [
        "bLance", "bKnight", "bSilver", "bGold", "bKing", "bRook", "bBishop", "bPawn", 
        "wLance", "wKnight", "wSilver", "wGold", "wKing", "wRook", "wBishop", "wPawn"
    ]
    images = {}
    for piece in pieces:
        images[piece] = pygame.image.load(f"images/{piece}.png")
    return images

def draw_piece(game, piece, row, col, square_size, images):
    if piece in images:
        piece_image = images[piece] #Collecting the image from the dictionary
        piece_image = pygame.transform.scale(piece_image, (square_size, square_size))  # Resizing the image
        game.screen.blit(piece_image, (col * square_size, row * square_size))
        
        
def main():
    pygame.init()  # Pygame initialization
    game = GameState()
    images = load_images()

    running = True      
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        draw_board(game, images)  # Draw the board
        pygame.display.flip() # refresh the screen
        game.timer.tick(game.fps) # fps limit set 

    pygame.quit()  #End the program

def draw_board(game, images):
    """
    Rysuje planszę na ekranie.
    """
    background_path = "images/background.png"  
    background = pygame.image.load(background_path )  
    square_size = 80 
    for row in range(9):
        for col in range(9):
            game.screen.blit(background, (col * square_size, row * square_size))
            
            pygame.draw.rect(
                game.screen,
                (0, 0, 0), # color of boarder
                pygame.Rect(col * square_size, row * square_size, square_size, square_size), 2    # size of boarder in px
            )
               
            piece = game.board[row][col]
            if piece != " ":
                draw_piece(game, piece, row, col, square_size, images)


if __name__ == "__main__":
    main()