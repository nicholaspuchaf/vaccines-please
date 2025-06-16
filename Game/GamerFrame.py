import tkinter as tk
from tkinter import messagebox # Import messagebox for custom alerts
from PIL import Image, ImageTk # Import Pillow for image manipulation

import cv2
import threading
import time


from GenericFrame import GenericFrame
from constants import *
from texts import *

class GamerFrame(GenericFrame):

    def __init__(self):
        super().__init__()
        self.gameRoot = None
        
        # cap, video_label, stop_event, qr_decoder, qr_detected
        self.cap = None
        self.video_label = None
        self.qr_decoder = None
        self.qr_detected = None

        self.video_thread :threading.Thread = None
        self.stop_event : threading.Event = threading.Event()

        self.playing_menu_frame = None
        self.btn1 = None
        self.btn2 = None
        self.btn3 = None
        self.btn4 = None

        self.control_button_handle = {
            "officer_pre_talk" : True,
            "vacines_cards_time" : False
        }
    
        self.setEndCallback(self.callback)




    def setRoot(self,root):
        self.gameRoot = root
    
    def update_video_label(self,image):
        
        if self.video_label:
            self.video_label.config(image=image)
            self.video_label.image=image



    def video_stream(self):

        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            messagebox.showerror("Camera Error", "Could not open video stream or file.")
            self.stop_event.set() # Set stop event if camera fails to open
            return

        self.qr_decoder = cv2.QRCodeDetector()

        if not self.qr_decoder:
            messagebox.showerror("QR Code detector Error")
            self.stop_event.set()
            return

        while not self.stop_event.is_set():
            ret, frame = self.cap.read() # Read a frame from the camera
            if not ret:
                messagebox.showerror("Camera Error", "Failed to grab frame.")
                break
            
            

            # QR Code Logic, its working, but needs to implement with the game logic
            data, bbox, _ = self.qr_decoder.detectAndDecode(frame)
            new_state = bool(data)
            if new_state != self.qr_detected:
                self.qr_detected = new_state
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
            self.gameRoot.after(0, lambda: self.update_video_label(tk_image))

            # Small delay to prevent 100% CPU usage, adjust as needed
            time.sleep(0.01)


    def place_camera(self):
        self.video_label = tk.Label(self.frame, bg=BG_COLOR)
        self.video_label.pack(pady=10, expand=False)


    def pack_frame(self):
        self.frame.pack(pady=10, expand=True, fill="both")
        
        try:
            if (self.video_thread is None or not self.video_thread.is_alive()):
                self.stop_event.clear()

                self.video_thread = threading.Thread(target=self.video_stream, args=())
                self.video_thread.daemon = True
                self.video_thread.start()

                print("Video thread running")

        except Exception as e:
            messagebox.showerror(f"Error loading player camera: {e}")
            return None
        return 

    def clear_button(self,button):
        button.config(text="")

    def close_thread(self):
        self.stop_event.set()
        if self.video_thread and self.video_thread.is_alive():
            self.video_thread.join(timeout=1.0)
        if self.cap and self.cap.isOpened():
            self.cap.release()

    def handle_button(self):
        if self.control_button_handle["officer_pre_talk"]:
            self.next_page(1) 
            # Aqui recarrega toda a imagem da cena, precisa mudar depois para atualizar somente o texto e as opceos

            # Mudar futuramente para passar as opcoes para o text.py. Fica mais facil de customizar e aumentar as opcoes depois
            if self.frame_data[self.whichShow]["text"] == "Ei, você! Você não é daqui, não é?":
                self.btn1.config(text="Sim, a viage (mentir)")
                self.btn2.config(text="Não, venho de fora")
                self.clear_button(self.btn3)
                self.clear_button(self.btn4)

            self.control_button_handle["officer_pre_talk"] = False
            self.control_button_handle["vacines_cards_time"] = True
            self.whichShow = 7

        elif self.control_button_handle["vacines_cards_time"]:
            self.next_page(1)

    def callback(self):
        print("Callback não apropriado, mudar depois")

    def place_playing_menu(self):
        
        menuFrame = tk.Frame(
            self.frame,
            bg=BG_COLOR
        )
        menuFrame.place(x=WIDTH-400,y = HEIGHT -200)

        self.playing_menu_frame = menuFrame

        self.btn1 = tk.Button(menuFrame, text="Olá?", command=lambda:self.handle_button(), 
                        bg=COLOR_DARK_CHARCOAL,
                        relief="sunken", borderwidth=2, anchor="nw",
                        font=(FONT_FAMILY, 8, "bold"),
                        fg="white")
        self.btn2 = tk.Button(menuFrame, text="Onde estou?", command=lambda:self.handle_button(),
                         bg=COLOR_DARK_CHARCOAL,
                        relief="sunken", borderwidth=2, anchor="nw",
                        font=(FONT_FAMILY, 8, "bold"),
                        fg="white")
        self.btn3 = tk.Button(menuFrame, text="Fui preso?", command=lambda:self.handle_button(), 
                         bg=COLOR_DARK_CHARCOAL,
                        relief="sunken", borderwidth=2, anchor="nw",
                        font=(FONT_FAMILY, 8, "bold"),
                        fg="white")
        self.btn4 = tk.Button(menuFrame, text="Me solta", command=lambda:self.handle_button(),
                        bg=COLOR_DARK_CHARCOAL,
                        relief="sunken", borderwidth=2, anchor="nw",
                        font=(FONT_FAMILY, 8, "bold"),
                        fg="white")

        self.btn1.grid(row=0, column=0, padx=5,pady=5)
        self.btn2.grid(row=0, column=1, padx=5,pady=5)
        self.btn3.grid(row=1, column=0, padx=5,pady=5)
        self.btn4.grid(row=1, column=1, padx=5,pady=5)


