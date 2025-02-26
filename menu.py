import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from game import Game_class


class Menu_class:
    def __init__(self):
        self.root = tk.Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = 360
        window_height = 720

        self.root.geometry(f"{window_width}x{window_height}+{(screen_width - window_width) // 2}+{(screen_height - window_height) // 2}")
        self.root.title("Menu")
        self.root.resizable(False, False)

        # Load and set the background image
        background_path = "images/menu.png"  # Path to the background image
        background_image = Image.open(background_path)
        background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self.root, image=background_photo)
        background_label.image = background_photo  # Keep a reference to avoid garbage collection
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):
        # Create a frame for the bottom buttons
        bottom_frame = tk.Frame(self.root, bg=self.root.cget("bg"))
        bottom_frame.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        button1 = tk.Button(bottom_frame, text="Host", command=self.on_host, width=10, height=2, bg="blue", fg="white")
        button1.pack(side=tk.LEFT, padx=10)

        button2 = tk.Button(bottom_frame, text="Join", command=self.on_join, width=10, height=2, bg="blue", fg="white")
        button2.pack(side=tk.LEFT, padx=10)

        button3 = tk.Button(bottom_frame, text="Local", command=self.on_local, width=10, height=2, bg="blue", fg="white")
        button3.pack(side=tk.LEFT, padx=10)

    def on_host(self):
        messagebox.showinfo("Host", "Host button clicked")
        self.root.destroy()

    def on_join(self):
        messagebox.showinfo("Join", "Join button clicked")
        self.root.destroy()

    def on_local(self):
        messagebox.showinfo("Local", "Local button clicked")
        self.root.destroy()
        game = Game_class()
        game.game_loop()