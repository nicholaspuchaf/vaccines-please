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


    def close_thread(self):
        self.stop_event.set()
        if self.video_thread and self.video_thread.is_alive():
            self.video_thread.join(timeout=1.0)
        if self.cap and self.cap.isOpened():
            self.cap.release()


    def place_playing_menu(self):
        pass

