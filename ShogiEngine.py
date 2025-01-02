import pygame as p 
import board

Width = Height = 1350 # 9 squares * 150 pixels
Dimension = 9 # 9x9 board
SqSize = Height // Dimension
Max_FPS = 15
IMAGES = {}


'''
Initialize a global dictionary of images.
'''
def loadImages():
    for piece in board.Pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("pieceImages/" + piece + ".png"), (SqSize, SqSize))


def main():
    p.init()
    screen = p.display.set_mode((Width, Height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    b = board.GameState()
    loadImages() # load images
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        clock.tick(Max_FPS)
        p.display.flip()

def drawBoard(screen):
    for r in range(Dimension):
        for c in range(Dimension):
            p.draw.rect(screen, (196, 164, 132), p.Rect(c*SqSize, r*SqSize, SqSize, SqSize))
            
if __name__ == "__main__":
    main()