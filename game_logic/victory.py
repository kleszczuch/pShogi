import tkinter as tk
import PIL
from PIL import Image, ImageTk, ImageSequence
import sys
from game_logic.caputuring_and_reviving import *

def show_victory_message(message,main):
    def on_exit():
        root.destroy()
        sys.exit()

    def on_play_again():
        for key, value in captured_by_white.items(): value["piece"] = None # Reset captured pieces
        for key, value in captured_by_black.items(): value["piece"] = None # Reset captured pieces
        root.destroy()
        main()  

    root = tk.Tk()
    root.title("Victory!")
    root.resizable(False, False)
    root.configure(bg='white')  
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = 500
    window_height = 575

    position_right = int(screen_width/2 - window_width/2)
    position_down = int(screen_height/2 - window_height/2)

    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

    label = tk.Label(root, text=message)
    label.pack(pady=10)

    gif_label = tk.Label(root)
    gif_label.pack()

    gif_path = "images/Victory_GIF.gif" #GIF path
    gif = Image.open(gif_path)
    frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]

    def update_frame(index):
        frame = frames[index]
        gif_label.configure(image=frame)
        root.after(100, update_frame, (index + 1) % len(frames))

    root.after(0, update_frame, 0)

    button_exit = tk.Button(root, text="Exit", command=on_exit ) # Exit button
    button_exit.pack(side=tk.LEFT, padx=20)

    button_play_again = tk.Button(root, text="Play Again", command=on_play_again) # Play again button
    button_play_again.pack(side=tk.RIGHT, padx=20)

    root.protocol("WM_DELETE_WINDOW", on_exit)

    root.mainloop()
    
