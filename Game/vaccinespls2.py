import cv2
import tkinter as tk
from PIL import Image, ImageTk

class QRImageSwitcher:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Activated Image Viewer")
        
        # Load images
        self.image0 = ImageTk.PhotoImage(Image.open("image0.jpg"))
        self.image1 = ImageTk.PhotoImage(Image.open("image1.jpg"))
        
        # Create display label
        self.label = tk.Label(root)
        self.label.pack()
        
        # Initialize webcam and QR detector
        self.cap = cv2.VideoCapture(0)
        self.qr_decoder = cv2.QRCodeDetector()
        self.qr_detected = False
        
        # Start detection loop
        self.detect_qr()
    
    def detect_qr(self):
        ret, frame = self.cap.read()
        if ret:
            # QR detection
            data, bbox, _ = self.qr_decoder.detectAndDecode(frame)
            new_state = bool(data)
            
            # Update image if state changed
            if new_state != self.qr_detected:
                self.qr_detected = new_state
                self.label.config(image=self.image1 if self.qr_detected else self.image0)
        
        # Repeat every 100ms
        self.root.after(100, self.detect_qr)

    def __del__(self):
        self.cap.release()

# Setup and run
root = tk.Tk()
app = QRImageSwitcher(root)
root.mainloop()