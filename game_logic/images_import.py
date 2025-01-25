# game_logic/utils.py
import pygame

def load_images():
    pieces = [
        "wLance_NPY", "wKnight_NPY", "wSilver_NPY", "wGold", "wKing", "wRook_NPY", "wBishop_NPY", "wPawn_NPY",
        "bLance_NPY", "bKnight_NPY", "bSilver_NPY", "bGold", "bKing", "bRook_NPY", "bBishop_NPY", "bPawn_NPY",
        "wLance_P", "wKnight_P", "wSilver_P", "wRook_P", "wBishop_P", "wPawn_P",
        "bLance_P", "bKnight_P", "bSilver_P", "bRook_P", "bBishop_P", "bPawn_P"
    ]
    
    images = {}  # dictionary of images to be able to use them in the draw board function
    for piece in pieces:
        images[piece] = pygame.image.load(f"images/{piece}.png")
    return images