import tkinter as tk
from tkinter import messagebox # Import messagebox for custom alerts
from PIL import Image, ImageTk # Import Pillow for image manipulation

import cv2
import threading
import time


from GenericFrame import GenericFrame
from constants import *
from texts import *

from Pyshock import shock

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

        self.control_button_handle = { # variavel de controle do jogo usado no handle_button
            "officer_pre_talk" : True,
            "vacines_cards_time" : False,
            "waiting_player": False
        }

        self.setEndCallback(self.callback)

        # Manuseio do couter: count down: relogio
        self.counter_value = 0
        self.counter_label = None

        # Manuseio da resposta em qr_code do jogador
        self.player_qr_code = None
        self.player_life = PLAYER_LIFE
        self.heart_frame_number_label = None
        self.heart_label = None

        self.false_counter = 0
        self.falseLabel = None

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
                self.qr_detected = bool(data)
                # print(data)
                if self.qr_detected and self.control_button_handle["waiting_player"]:
                    print(data)
                    self.handle_button(str(data))


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

                # print("Video thread running")

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

    def handle_button(self, data=None):
        if self.control_button_handle["officer_pre_talk"]:
            self.next_page(1) 
            # Aqui recarrega toda a imagem da cena, precisa mudar depois para atualizar somente o texto e as opceos
            frame_dict = self.frame_data[self.whichShow]
            try:
                btn1Text = frame_dict["opcoes"][0]
                btn2Text = frame_dict["opcoes"][1]
                btn3Text = frame_dict["opcoes"][2]
                btn4Text = frame_dict["opcoes"][3]
            except Exception as e:
                btn1Text = RESPOSTA_PADRAO_1
                btn2Text = RESPOSTA_PADRAO_2
                btn3Text = RESPOSTA_PADRAO_3
                btn4Text = RESPOSTA_PADRAO_4

            self.btn1.config(text=btn1Text)
            self.btn2.config(text=btn2Text)
            self.btn3.config(text=btn3Text)
            self.btn4.config(text=btn4Text)
        
            if self.frame_data[self.whichShow]["flag"] == "startGame":
                self.control_button_handle["officer_pre_talk"] = False
                self.control_button_handle["vacines_cards_time"] = True

        elif self.control_button_handle["vacines_cards_time"]:
            
            self.next_page(1)
            frame_dict = self.frame_data[self.whichShow]
            btn1Text = frame_dict["opcoes"][0]
            btn2Text = frame_dict["opcoes"][1]
            btn3Text = frame_dict["opcoes"][2]
            btn4Text = frame_dict["opcoes"][3]
            self.btn1.config(text=btn1Text)
            self.btn2.config(text=btn2Text)
            self.btn3.config(text=btn3Text)
            self.btn4.config(text=btn4Text)

            self.counter_value = COUNTDOWN_TIME
            self.start_countdown()

            self.control_button_handle["vacines_cards_time"] = False
            self.control_button_handle["waiting_player"] = True

        elif self.control_button_handle["waiting_player"]:
            
            # data = self.player_qr_code
            frame_dict = self.frame_data[self.whichShow]
            
            if data == None: # jogador escolheu n mostrar nenhum comprovante, e tomar a vacina
                try:
                    # print("Chamando a funcao shock do salvador")
                    shock()
                except Exception as e:
                    messagebox.showerror(f"Error ao chamaro shock {e}")
                
                self.counter_value = 0
                self.control_button_handle["vacines_cards_time"] = True
                self.control_button_handle["waiting_player"] = False
            elif data == frame_dict["vacinaCorreta"]:
                # print("Acertou a vacina")
                
                self.counter_value = 0
                self.control_button_handle["vacines_cards_time"] = True
                self.control_button_handle["waiting_player"] = False
            elif data in frame_dict["outras"]: # mostoru uma vacina falsa
                # print("Vacina falsa mostrada")

                self.false_counter += 1
                self.update_false_counter()
                self.counter_value = 0
                self.control_button_handle["vacines_cards_time"] = True
                self.control_button_handle["waiting_player"] = False
            else:
                
                print("Errou a vacina")
                # self.player_life -= 1
                # self.update_life()
                # if self.player_life == 0:
                #     self.text_label.config(text="Fim de Jogo : Perdeu")
                if self.actual_text != f"Comprovante errado seu animal, quero {frame_dict['vacina']}": 
                    self.actual_text = f"Comprovante errado seu animal, quero {frame_dict['vacina']}"    
                    self.show_story_text(0)

        else:
            print("Fim do Jogo")

    def callback(self):
        
        print("Fim do Jogo")
        self.control_button_handle["officer_pre_talk"] = False
        self.control_button_handle["vacines_cards_time"] = False

        # ending = ending_frames[0]
        if self.place_false_counter == 0:
            ending = ending_frames[0] # Good entding
        else:
            # Não entrou
            ending = ending_frames[1] # Bad Ending
    
        bg_image = None
        try:
            bg_image = Image.open(ending["background"])
            bg_image = bg_image.convert("RGBA")
            bg_image = bg_image.resize((WIDTH, HEIGHT), Image.LANCZOS)

        except Exception as e:
            messagebox.showerror(f"Error loading background: {e}")
            return None

        tk_final_image = ImageTk.PhotoImage(bg_image)
        self.label.config(image=tk_final_image)
        self.label.image = tk_final_image
        self.actual_text = ending["text"]

        self.heart_label.destroy()
        self.counter_label.destroy()
        self.playing_menu_frame.destroy()


        self.show_story_text(0)        

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

    def place_counter(self):
        
        self.counter_label = tk.Label(
            self.frame,
            text=f"Tempo : {self.counter_value}",
            bg=COLOR_DARK_CHARCOAL,
            relief="sunken", borderwidth=2, anchor="nw",
            font=(FONT_FAMILY, 24, "bold"),
            fg="white"
        )
        self.counter_label.place(x=WIDTH-200, y=90, anchor="nw")

    def start_countdown(self):

        if self.counter_value > 0:
            self.counter_value -= 1
            self.counter_label.config(text=f"Tempo : {self.counter_value}")
            self.counter_label.after(1000, self.start_countdown)
        else:
            self.player_qr_code = "Acabou o tempo"
            self.handle_button()    

    def place_lifebox(self):
        
        heart_frame = tk.Frame(self.frame,
                            bg=BG_COLOR )

        
        try:
            heart_image = Image.open("static/heart.png")
            heart_image = heart_image.convert("RGBA")
            heart_image = heart_image.resize((HEART_WIDTH, HEART_HEIGHT), Image.LANCZOS)
            
        except Exception as e:
            messagebox.showerror("Erro ao carregar o coracao")
        
        heart_tk = ImageTk.PhotoImage(heart_image)
        heart_label = tk.Label(heart_frame, image=heart_tk, bg=BG_COLOR)
        heart_label.image = heart_tk
        
        number_label = tk.Label(
            heart_frame,
            text=self.player_life,
            bg=COLOR_DARK_CHARCOAL,
            relief="sunken", borderwidth=2, anchor="nw",
            font=(FONT_FAMILY, 18, "bold"),
            fg="white"
        )
        
        number_label.pack(side=tk.LEFT)
        heart_label.pack(side=tk.RIGHT)

        heart_frame.place(x = WIDTH-200, y = 10, anchor="nw")
        self.heart_frame_number_label = number_label
        self.heart_label = heart_frame

    def update_life(self):
        self.heart_frame_number_label.config(self.player_life)

    def place_false_counter(self):

        falseLabel = tk.Label(self.frame,
                            text=f"Vacinas falsas usadas:{self.false_counter}",
                            bg=COLOR_DARK_CHARCOAL,
                            relief="sunken", borderwidth=2, anchor="nw",
                            font=(FONT_FAMILY, 14, "bold"),
                            fg="white")
        
        falseLabel.place(x = WIDTH-300, y = 10)
        self.falseLabel = falseLabel

    def update_false_counter(self):
        self.falseLabel.config(text=f"Vacinas falsas usadas:{self.false_counter}")
