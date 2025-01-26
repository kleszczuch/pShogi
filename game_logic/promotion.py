import tkinter as tk
from tkinter import messagebox
from itertools import cycle
from game_logic.images_import import load_images
from PIL import Image, ImageTk  # Import PIL for image conversion
import pygame

class PromotionWindow:
    def __init__(self, piece_name, color):
        self.promotion = False
        self.piece_name = piece_name
        self.color = color
        self.root = tk.Tk()
        self.root.title("Promotion")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = 300
        window_height = 150

        position_right = int(screen_width/2 - window_width/2)
        position_down = int(screen_height/2 - window_height/2)

        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")
        self.images = load_images()
        imageBefore = self.images[piece_name+"_NPY"]
        imageBefore = pygame.transform.scale(imageBefore, (100, 100))
        imageAfter = self.images[piece_name+"_P"]
        imageAfter = pygame.transform.scale(imageAfter, (100, 100))
        change = pygame.image.load("images/change.png")
        change = pygame.transform.scale(change, (100, 100))

        self.images = cycle([self.convert_to_tk_image(imageBefore), 
                             self.convert_to_tk_image(change), 
                             self.convert_to_tk_image(imageAfter)])  # Convert to iterator using cycle
        self.background_label = tk.Label(self.root)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.update_background()

        self.create_widgets()

    def convert_to_tk_image(self, pygame_image):
        size = pygame_image.get_size()
        data = pygame.image.tostring(pygame_image, "RGBA")
        image = Image.frombytes("RGBA", size, data)
        return ImageTk.PhotoImage(image)

    def update_background(self):
        self.background_label.config(image=next(self.images))
        self.root.after(1000, self.update_background)  # Change image every 1000ms (1 second)
            
    def create_widgets(self):
        yes_button = tk.Button(self.root, text="Yes", command=self.on_yes, width=10, bg="green", fg="white")
        yes_button.pack(side=tk.LEFT, padx=20, pady=10)

        no_button = tk.Button(self.root, text="No", command=self.on_no, width=10, bg="red", fg="white")
        no_button.pack(side=tk.RIGHT, padx=20, pady=10)

        self.root.mainloop()

    def on_yes(self):
        self.promotion = True
        self.root.destroy()  # Close the window after the decision

    def on_no(self):
        self.promotion = False
        self.root.destroy()  # Close the window after the decision

def want_and_able_to_promote(piece_name, piece_pos, color, promotion):
    if piece_name.lower() != "king" and piece_name.lower() != "gold" and not promotion:
        if color == "white":
            if piece_pos <= 2:  # check if is able to promo
                promotion_window = PromotionWindow(piece_name, color)
                return promotion_window.promotion
        elif color == "black":
            if piece_pos >= 6:  # check if is able to promo
                promotion_window = PromotionWindow(piece_name, color)
                return promotion_window.promotion
        else:
            return False
    else:
        return False