import tkinter as tk
from tkinter import messagebox # Import messagebox for custom alerts
from PIL import Image, ImageTk # Import Pillow for image manipulation

import cv2
import threading
import time

from constants import *
from texts import *
from GenericFrame import GenericFrame
from GamerFrame import GamerFrame


# Global Variables for camera and Thread Control
cap = None 
stop_event = threading.Event() # Event to signal the video thread to stop
video_thread = None
video_label = None # To hold the label that displays the video feed
qr_decoder = None
qr_detected = False
talking_label = None

# Global Variables for Tkinter Control 
storyFrame1 = None
storyFrame2 = None
storyFrameUsing = 1
root_window = None # Global reference to the root Tkinter window
runningFrame = None

# Criando e configurando os frames
startFrame = GenericFrame()
startGameFrame = GamerFrame()
playingFrame = GamerFrame()
    

storyLabels = []

def show_options():
    """Placeholder function for showing game options."""
    messagebox.showinfo("Options", "Displaying game options... (Not implemented yet!)")


def on_closing(root : tk.Tk, frame : GamerFrame):
    """
    Handles the window closing event.
    Releases the camera and stops the video thread.
    """
    frame.close_thread()
    root.destroy()


def test_frame(frameObj):
    global mainMenuFrame, storyFrame1, storyFrame2, storyFrameUsing, storyFrames, storyLabels

    if mainMenuFrame:
        mainMenuFrame.forget()

    frameObj.pack_frame()
    return
    thisFrame = None

    if storyFrameUsing == 1:
        thisFrame = storyFrame1
        storyFrameUsing = 2
        

    if storyFrameUsing == 2:
        thisFrame = storyFrame2
        storyFrameUsing = 1

    if thisFrame:
        thisFrame.pack(pady=10, expand=True, fill="both")
        

def handle_frames(frameObj):
    global runningFrame

    if frameObj.isReady == False:
        return

    if runningFrame != None:
        runningFrame.forget()

    frameObj.pack_frame()
    runningFrame = frameObj


def end_story_frame():
    handle_frames(playingFrame)


def create_window():
    """
    Creates a Tkinter window with a themed menu.
    """
    global runningFrame, video_label, video_thread, stop_event, root_window, storyFrames

    # Create the main window (root window)
    root_window = tk.Tk()
    # --- Theme Configuration (Buckshot Roulette inspired) ---
    # Dark background colors
    bg_color = COLOR_DARK_CHARCOAL # Dark charcoal
    fg_color = COLOR_LIGHT_GRAY # Light gray for text
    accent_color = COLOR_DEEP_RED # Deep red for accents

    # Font for a gritty/monospace feel
    # 'Courier New' is a good default monospace font available on most systems.
    # You could also try 'Consolas', 'Lucida Console', or 'Monaco' if available.
    font_family = FONT_FAMILY
    font_size = 12
    heading_font_size = 16

    root_window.title("Vaccines, Please")
    root_window.geometry(str(WIDTH)+"x"+str(HEIGHT)) # Slightly larger window
    root_window.configure(bg=bg_color) # Set window background
    root_window.resizable(False, False)

    root_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(root_window, playingFrame))

    # --- Create Menu Bar ---
    menu_bar = tk.Menu(root_window, bg=bg_color, fg=fg_color,
                       activebackground=accent_color, activeforeground=fg_color,
                       font=(font_family, font_size))
    root_window.config(menu=menu_bar) # Attach the menu bar to the root_window window

    ##### ADICIONA OS FRAMES DE HISTÓRIA #####
    # Adicionando os frames (agora como dicionários completos)
    

    for frame_dict in storyFrames:  # Adiciona os frames
        startFrame.add_frame_data(frame_dict)

    # Criando o frame na janela
    startFrame.create_frame_with_image(root_window)
    startFrame.setEndCallback(end_story_frame)

    # Adicionando o frame de jogo
    playingFrame.setRoot(root_window)
    playingFrame.add_frame_data(playingFrames[0])
    playingFrame.create_frame_with_image(root_window)     
    playingFrame.next_button.destroy()
    for frame_dict in playingFrames:
        playingFrame.add_frame_data(frame_dict)
    playingFrame.place_camera()
    playingFrame.place_playing_menu()
    playingFrame.place_counter()
    # playingFrame.place_lifebox()
    playingFrame.place_false_counter()

    ############################################
    menu_bar.add_command(label="Start", command=lambda:handle_frames(startFrame))
    menu_bar.add_command(label="Options", command=show_options)
    menu_bar.add_command(label="Quit", command=lambda:on_closing(root_window, playingFrame))
    menu_bar.add_command(label="Credits", command=lambda:test_frame())

    mainMenuFrame = GenericFrame()

    mainMenuFrame.create_empty_frame(root_window)
    mainMenuFrame.pack_frame()    
    runningFrame = mainMenuFrame

    main_label = tk.Label(mainMenuFrame.frame,
                          text="Vaccines, Please",
                          bg=bg_color,
                          fg=fg_color,
                          font=(font_family, heading_font_size, "bold"))
    main_label.pack(pady=20) # Add some padding

    sub_label = tk.Label(mainMenuFrame.frame,
                         text="Será que você consegue escapar da Mexicolândia e entrar nos estados vacinados da América?",
                         bg=bg_color,
                         fg=fg_color,
                         font=(font_family, font_size),
                         wraplength=300)
    sub_label.pack(pady=10)

    return root_window


if __name__ == "__main__":
    
    root_window = create_window()
    root_window.mainloop()
