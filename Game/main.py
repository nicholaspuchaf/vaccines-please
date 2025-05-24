import tkinter as tk
from tkinter import messagebox # Import messagebox for custom alerts
from PIL import Image, ImageTk # Import Pillow for image manipulation

import cv2
import threading
import time

from constants import *


# Global Variables for camera and Thread Control
cap = None
stop_event = threading.Event() # Event to signal the video thread to stop
video_thread = None
video_label = None # To hold the label that displays the video feed

# Global Variables for Tkinter Control 
mainMenuFrame = None
startGameFrame = None
root_window = None # Global reference to the root Tkinter window


def start_game():
    """Placeholder function for starting the game."""
    global mainMenuFrame, startGameFrame, video_thread, stop_event, video_label, root_window

    if mainMenuFrame:
        mainMenuFrame.pack_forget()
    
    if startGameFrame:
        startGameFrame.pack(pady=10, expand=True, fill="both")

    # Start the video stream in a separate thread ONLY when game starts
    # Ensure it's not already running
    if video_thread is None or not video_thread.is_alive():
        stop_event.clear() # Clear any previous stop signal
        # Pass the global root_window to the video_stream function
        video_thread = threading.Thread(target=video_stream, args=(root_window,))
        video_thread.daemon = True # Allow the main program to exit even if this thread is running
        video_thread.start()


def show_options():
    """Placeholder function for showing game options."""
    messagebox.showinfo("Options", "Displaying game options... (Not implemented yet!)")


def on_closing(root):
    """
    Handles the window closing event.
    Releases the camera and stops the video thread.
    """
    global cap, stop_event, video_thread
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        stop_event.set() # Signal the thread to stop
        if video_thread and video_thread.is_alive():
            video_thread.join(timeout=1.0) # Wait for the thread to finish (with a timeout)
        if cap and cap.isOpened():
            cap.release() # Release the camera
        root.destroy() # Close the Tkinter window


def update_video_label(tk_image):
    """Updates the video_label with the new Tkinter PhotoImage."""
    global video_label
    if video_label:
        video_label.config(image=tk_image)
        video_label.image = tk_image # Keep a reference to prevent garbage collection


def video_stream(root):
    
    global cap, video_label, stop_event

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        messagebox.showerror("Camera Error", "Could not open video stream or file.")
        stop_event.set() # Set stop event if camera fails to open
        return
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while not stop_event.is_set():
        ret, frame = cap.read() # Read a frame from the camera
        if not ret:
            messagebox.showerror("Camera Error", "Failed to grab frame.")
            break

        # Convert the frame from BGR (OpenCV) to RGB (Pillow)
        cv2_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert to PIL Image
        pil_image = Image.fromarray(cv2_image)

        # Resize image to fit the label, maintaining aspect ratio
        # Calculate new dimensions to fit within a max size (e.g., 600x400)
        max_width = CAMERA_SIZE_WIDTH
        max_height = CAMERA_SIZE_HEIGHT
        original_width, original_height = pil_image.size

        aspect_ratio = original_width / original_height

        if original_width > max_width or original_height > max_height:
            if aspect_ratio > (max_width / max_height):
                new_width = max_width
                new_height = int(new_width / aspect_ratio)
            else:
                new_height = max_height
                new_width = int(new_height * aspect_ratio)
            pil_image = pil_image.resize((new_width, new_height), Image.LANCZOS)


        # Convert PIL Image to Tkinter PhotoImage
        tk_image = ImageTk.PhotoImage(image=pil_image)

        # Update the label with the new image
        # Use root.after to schedule the update on the main Tkinter thread
        # This is crucial because Tkinter widgets can only be modified from the main thread.
        root.after(0, lambda: update_video_label(tk_image))

        # Small delay to prevent 100% CPU usage, adjust as needed
        time.sleep(0.01)


def create_window():
    """
    Creates a Tkinter window with a themed menu.
    """
    global video_label, video_thread, stop_event, mainMenuFrame, startGameFrame, root_window

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
    root_window.geometry(str(HEIGHT)+"x"+str(WIDTH)) # Slightly larger window
    root_window.configure(bg=bg_color) # Set window background

    root_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(root_window))

    # --- Create Menu Bar ---
    menu_bar = tk.Menu(root_window, bg=bg_color, fg=fg_color,
                       activebackground=accent_color, activeforeground=fg_color,
                       font=(font_family, font_size))
    root_window.config(menu=menu_bar) # Attach the menu bar to the root_window window

    # --- Create 'Game' Menu ---
    game_menu = tk.Menu(menu_bar, tearoff=0, bg=bg_color, fg=fg_color,
                        activebackground=accent_color, activeforeground=fg_color,
                        font=(font_family, font_size))
    menu_bar.add_cascade(label="Game", menu=game_menu) # Add 'Game' as a top-level menu

    # Add commands to the 'Game' menu
    game_menu.add_command(label="Start Game", command=start_game)
    game_menu.add_command(label="Options", command=show_options)
    game_menu.add_separator() # Add a visual separator
    game_menu.add_command(label="Quit", command=root_window.quit) # Quits the application


    # --- Start Game Frame ---
    
    startGameFrame = tk.Frame(root_window, bg=BG_COLOR, padx=20, pady=20)
    video_label = tk.Label(startGameFrame, bg=BG_COLOR)
    video_label.pack(pady=10, expand=True, fill="both") # Allow label to expand

    room_image_path = "static/mainRoom.jpeg"

    pil_image_main_room = None

    try:
        pil_image_main_room = Image.open(room_image_path)
    except FileNotFoundError:
        messagebox.showwarning("Image Warning", f"Image file not found at '{room_image_path}'.")
    except Exception as e:
        messagebox.showwarning("Image Warning", f"{e}")


    pil_image_main_room = pil_image_main_room.resize((ROOM_WIDTH, ROOM_HEIGHT), Image.LANCZOS)

    tk_main_room = ImageTk.PhotoImage(pil_image_main_room)

    mainRoomLabel = tk.Label(startGameFrame, image=tk_main_room, bg=BG_COLOR)
    mainRoomLabel.image = tk_main_room
    mainRoomLabel.pack(pady=10)

    # --- Main Menu Frame ---
    # Using a Frame to better control padding and background for the label
    mainMenuFrame = tk.Frame(root_window, bg=bg_color, padx=20, pady=20)
    mainMenuFrame.pack(expand=True, fill="both") # Expand to fill available space

    
    main_label = tk.Label(mainMenuFrame,
                          text="Vaccines, Please",
                          bg=bg_color,
                          fg=fg_color,
                          font=(font_family, heading_font_size, "bold"))
    main_label.pack(pady=20) # Add some padding

    sub_label = tk.Label(mainMenuFrame,
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
