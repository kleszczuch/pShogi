import pygame
from board import TRANSLUCENT_RED, GameState, draw_board, draw_scene, highlight_tile, screen
from game_logic.moves import move_piece, get_type_color_and_promotion, is_valid_move, get_revive_pos
from game_logic.check import is_in_check
from game_logic.caputuring_and_reviving import get_captured_by_black, get_captured_by_white
from game_logic.victory import show_victory_message
from game_logic.images_import import load_images

class Game_class:
    def game_loop(self):
        
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
        takenfrom = ""
        ischeck = ""
        isWwin = False
        isBwin = False
        isWin = False
        while running:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if firstTime: # So the board is drawn only once at the beginning 
                pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                if not isWin:    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        firstTime = False
                        
                        grid_x = mouse_y  // square_size
                        grid_y = mouse_x  // square_size 
                        revive = False
                        # check if the click was on a piece
                        for piece in game.get_piece_pos_board():
                            if piece["pos"] == [grid_x , grid_y -3]:
                                if piece["piece"][0] == turn:
                                    dragging = True
                                    selected_piece = piece
                                    draw_board(game, images, selected_piece)
                                    pygame.display.flip()
                                break
                        # check if the click was on a captured piece
                        for key, value in get_captured_by_white().items():
                            if value["pos"] == (grid_x, grid_y) and value["piece"] is not None and value["piece"][0] == turn:
                                selected_piece = value
                                dragging = True
                                takenfrom = "white"
                                revive = True
                                draw_board(game, images, selected_piece, revive)
                                pygame.display.flip()
                                break

                        # check if the click was on a captured piece
                        for key, value in get_captured_by_black().items():
                            if value["pos"] == (grid_x, grid_y) and value["piece"] is not None and value["piece"][0] == turn:
                                selected_piece = value
                                dragging = True
                                takenfrom = "black"
                                revive = True
                                draw_board(game, images, selected_piece, revive)
                                pygame.display.flip()
                                break

                    elif event.type == pygame.MOUSEBUTTONUP:
                        if dragging and selected_piece:
                            grid_x = mouse_y // square_size
                            grid_y = mouse_x // square_size - 3
                            end_pos = (grid_x, grid_y)
                            if move_piece(game, selected_piece, end_pos, revive):
                                turn = 'b' if turn == 'w' else 'w'
                                                
                            dragging = False
                            selected_piece = None
                            wCheckKing, wking_pos, isBwin= is_in_check(game.board, 'w', game)    
                            bCheckKing, bking_pos, isWwin = is_in_check(game.board, 'b', game)
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
                highlight_tile(wking_pos[0],wking_pos[1], TRANSLUCENT_RED) 
            elif ischeck == "Black":
                highlight_tile(bking_pos[0],bking_pos[1], TRANSLUCENT_RED)
            elif isWwin:
                pygame.display.flip()
                isWin = True
                show_victory_message("White won", self.game_loop)
            elif isBwin:
                pygame.display.flip()
                isWin = True
                show_victory_message("Black won", self.game_loop)
            if after_move: 
                pygame.display.flip()
                after_move = False
            timer.tick(fps)
        pygame.quit()