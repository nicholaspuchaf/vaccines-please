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

storyLabels = []

def officer_change_text(text, index):
    global talking_label
    talking_label.config(text=text[:index])
    if index < len(text):
        talking_label.after(TEXT_DELAY, officer_change_text,text, index+1)


def show_story_text(label,text,index):

    if(index == 0):
        label.config(text="")

    label.config(text=text[:index])
    if index < len(text):
        label.after(TEXT_DELAY, show_story_text, text, index+1)


def start_game():
    """Placeholder function for starting the game."""
    global mainMenuFrame, startGameFrame, video_thread, stop_event, video_label, root_window

    if mainMenuFrame:
        mainMenuFrame.pack_forget()
    
    if startGameFrame:
        startGameFrame.pack(pady=10, expand=True, fill="both")
        officer_change_text("Você acha que pode entrar no nosso país ? Seu verme, me mostre seus comprovantes de vacina",0)


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
    
    global cap, video_label, stop_event, qr_decoder, qr_detected

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        messagebox.showerror("Camera Error", "Could not open video stream or file.")
        stop_event.set() # Set stop event if camera fails to open
        return
    
    qr_decoder = cv2.QRCodeDetector()

    if not qr_decoder:
        messagebox.showerror("QR Code detector Error")
        stop_event.set()
        return
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while not stop_event.is_set():
        ret, frame = cap.read() # Read a frame from the camera
        if not ret:
            messagebox.showerror("Camera Error", "Failed to grab frame.")
            break
        
        

        # QR Code Logic, its working, but needs to implement with the game logic
        data, bbox, _ = qr_decoder.detectAndDecode(frame)
        new_state = bool(data)
        if new_state != qr_detected:
            qr_detected = new_state
            print(data)


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


        pil_image_reflect = pil_image.transpose(Image.FLIP_LEFT_RIGHT)

        # Convert PIL Image to Tkinter PhotoImage
        tk_image = ImageTk.PhotoImage(image=pil_image_reflect)

        # Update the label with the new image
        # Use root.after to schedule the update on the main Tkinter thread
        # This is crucial because Tkinter widgets can only be modified from the main thread.
        root.after(0, lambda: update_video_label(tk_image))

        # Small delay to prevent 100% CPU usage, adjust as needed
        time.sleep(0.01)


def create_start_game_frame(startGameFrame):
    
    global video_label, talking_label

    
    pil_officer_img = None
    try:
        pil_officer_img = Image.open(OFFICER_PATH)
        
    except FileNotFoundError:
        messagebox.showerror(f"Officer file not found at {OFFICER_PATH}")
        return None    
    except Exception as e:
        messagebox.showerror(f"Error at Officer loading : {e}")
        return None
    
    pil_officer_img = pil_officer_img.convert("RGBA")
    original_officer_width, original_officer_height =  pil_officer_img.size
    new_officer_height = OFFICER_HEIGHT
    new_officer_width = int((new_officer_height/original_officer_height)*original_officer_width)
    pil_officer_img = pil_officer_img.resize((new_officer_width, new_officer_height), Image.LANCZOS)
        
        # --- Room Background ---
    room_image_path = ROOM_PATH
    pil_image_main_room = None
    try:
        pil_image_main_room = Image.open(room_image_path)
    except FileNotFoundError:
        messagebox.showwarning("Image Warning", f"Image file not found at '{room_image_path}'.")
    except Exception as e:
        messagebox.showwarning("Image Warning", f"{e}")

    pil_image_main_room = pil_image_main_room.resize((WIDTH, HEIGHT), Image.LANCZOS)
    # Merge it with the officer
    officer_y_offset = ((HEIGHT - OFFICER_Y_OFFSET))
    officer_x_offset = OFFICER_X_OFFSET
    final_pil_image_main_room = pil_image_main_room.copy()
    final_pil_image_main_room.paste(pil_officer_img,(officer_x_offset, officer_y_offset), pil_officer_img)

    tk_main_room = ImageTk.PhotoImage(final_pil_image_main_room)
    mainRoomLabel = tk.Label(startGameFrame.frame, image=tk_main_room, bg=BG_COLOR)
    mainRoomLabel.image = tk_main_room
    mainRoomLabel.place(x=0, y=0, relwidth=1, relheight=1)
    mainRoomLabel.lower()


    talking_label = tk.Label(startGameFrame.frame, bg=BG_COLOR, 
                            relief="sunken", borderwidth=2, anchor="nw", 
                            font=(FONT_FAMILY, 12, "bold"),
                            fg="white",
                            wraplength=TALKING_WIDTH)
    talking_label.place(x=TALKING_X, y=TALKING_Y, width=TALKING_WIDTH, height=TALKING_HEIGHT)

        # --- Player Camera ---
    video_label = tk.Label(startGameFrame.frame, bg=BG_COLOR)
    video_label.pack(pady=10, expand=False) # Allow label to expand
    officer_change_text("Você acha que pode entrar no nosso país ? Seu verme, me mostre seus comprovantes de vacina",0)
   

def generic_story_frame(imagePath, text):

    global storyFrame1, storyFrame2, storyFrameUsing

    # text = "Essa é a Mexicolândia, um país assolado por miséria e doença. Eles ficaram nessa condição pois seu presidente não acreditou nas vacinas."

    # imagePath = "static/Mexicolandia.png"
    image = None
    try:
        image = Image.open(imagePath)
        
    except FileNotFoundError:
        messagebox.showerror(f"Officer file not found at {imagePath}")
        return None    
    except Exception as e:
        messagebox.showerror(f"Error at Officer loading : {e}")
        return None


    image = image.convert("RGBA")
    image = image.resize((WIDTH, HEIGHT), Image.LANCZOS)

    tk_image = ImageTk.PhotoImage(image)

    imageLabel = None

    if (storyFrameUsing == 1):
        imageLabel = tk.Label(storyFrame1, image=tk_image)
    else:
        imageLabel = tk.Label(storyFrame2, image=tk_image)


    imageLabel.image = tk_image
    imageLabel.place(x=10, y=10, width=WIDTH-20, height=HEIGHT-20)
    imageLabel.lower()

    text_label = None

    if(storyFrameUsing == 1):
        text_label = tk.Label(storyFrame1, bg=COLOR_DARK_CHARCOAL,
                          relief="sunken", borderwidth=2, anchor="nw",
                          font=(FONT_FAMILY, 12, "bold"),
                          fg="white",
                          wraplength=int(WIDTH*2/3)
                        )
    else:
        text_label = tk.Label(storyFrame2, bg=COLOR_DARK_CHARCOAL,
                          relief="sunken", borderwidth=2, anchor="nw",
                          font=(FONT_FAMILY, 12, "bold"),
                          fg="white",
                          wraplength=int(WIDTH*2/3)
                        )
    text_label.place(x=WIDTH/6, y=HEIGHT - 50, width=int(WIDTH*2/3), height=TALKING_HEIGHT)
    text_label.config(text=text)

    return text_label


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

    root_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(root_window))

    # --- Create Menu Bar ---
    menu_bar = tk.Menu(root_window, bg=bg_color, fg=fg_color,
                       activebackground=accent_color, activeforeground=fg_color,
                       font=(font_family, font_size))
    root_window.config(menu=menu_bar) # Attach the menu bar to the root_window window

    ##### ADICIONA OS FRAMES DE HISTÓRIA #####
    # Adicionando os frames (agora como dicionários completos)
    for frame_dict in storyFrames[:17]:  # Adiciona os frames
        startFrame.add_frame_data(frame_dict)

    # Criando o frame na janela
    startFrame.create_frame_with_image(root_window)

    # Adicionando os frames
    for frame_dict in storyFrames[:17]:  # Adiciona os frames
        startFrame.add_frame_data(frame_dict)

    # Criando o frame na janela
    startFrame.create_frame_with_image(root_window)

    # Adicionando o frame de jogo


    ############################################
    menu_bar.add_command(label="Start", command=lambda:handle_frames(startFrame))
    menu_bar.add_command(label="Options", command=show_options)
    menu_bar.add_command(label="Quit", command=lambda:on_closing(root_window))
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
