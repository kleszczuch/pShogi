import tkinter as tk
from tkinter import messagebox
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
        self.create_widgets()

    def create_widgets(self):
        host_button = tk.Button(self.root, text="Host", command=self.on_host, width=20, height=2, bg="blue", fg="white")
        host_button.pack(pady=20)

        join_button = tk.Button(self.root, text="Join", command=self.on_join, width=20, height=2, bg="blue", fg="white")
        join_button.pack(pady=20)

        local_button = tk.Button(self.root, text="Local", command=self.on_local, width=20, height=2, bg="blue", fg="white")
        local_button.pack(pady=20)

        self.root.mainloop()

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