import tkinter as tk
from tkinter import messagebox # Import messagebox for custom alerts
from PIL import Image, ImageTk # Import Pillow for image manipulation

from constants import *

class GenericFrame:
    def __init__(self):
        self.frame = None  # Frame de Tkinter que esse Obj terá
        self.frame_data = []  # Agora armazenamos os dicionários completos dos frames
        self.whichShow = 0  # indica qual frame mostrar
        self.label = None  # Ponteiro para o label onde está a imagem
        self.text_label = None  # Ponteiro para onde está guardado o texto
        self.actual_text = None
        self.character_labels = []  # Para armazenar referências aos personagens

        self.next_button = None
        self.previous_button = None
        self.ready = False
        self.nextFrame = None

    def isReady(self):
        return self.ready

    def add_frame_data(self, frame_dict):
        """Adiciona um dicionário completo de frame"""
        self.frame_data.append(frame_dict)

    def forget(self):
        self.frame.forget()
        
    def pack_frame(self):
        if self.ready:
            self.frame.pack(pady=10, expand=True, fill="both")
            if self.text_label is not None:
                self.show_story_text(0)
        else:
            print("Tried to pack a not ready frame")

    def create_frame_with_image(self, parent, x=WIDTH/6, y=HEIGHT-60):
        self.frame = tk.Frame(parent, bg=BG_COLOR, padx=1, pady=1)
        
        # Carrega background
        current_frame = self.frame_data[self.whichShow]
        try:
            bg_image = Image.open(current_frame["background"])
            bg_image = bg_image.convert("RGBA")
            bg_image = bg_image.resize((WIDTH, HEIGHT), Image.LANCZOS)
            tk_bg_image = ImageTk.PhotoImage(bg_image)
            
            self.label = tk.Label(self.frame, image=tk_bg_image)
            self.label.image = tk_bg_image
            self.label.place(x=10, y=10, width=WIDTH-20, height=HEIGHT-20)
            self.label.lower()
        except Exception as e:
            messagebox.showerror(f"Error loading background: {e}")
            return None

        # Carrega personagens
        self.clear_characters()
        for char_img in current_frame.get("characters", []):
            try:
                char_image = Image.open(char_img)
                char_image = char_image.convert("RGBA")
                # Ajuste o tamanho conforme necessário para personagens
                char_image = char_image.resize((200, 400), Image.LANCZOS)
                tk_char_image = ImageTk.PhotoImage(char_image)
                
                char_label = tk.Label(self.frame, image=tk_char_image, bg=BG_COLOR)
                char_label.image = tk_char_image
                char_label.place(x=50, y=HEIGHT-400)  # Posição ajustável
                self.character_labels.append(char_label)
            except Exception as e:
                messagebox.showerror(f"Error loading character: {e}")

        # Configura área de texto
        self.text_label = tk.Label(
            self.frame, bg=COLOR_DARK_CHARCOAL,
            relief="sunken", borderwidth=2, anchor="nw",
            font=(FONT_FAMILY, 12, "bold"),
            fg="white",
            wraplength=int(WIDTH*2/3)-10,
            padx=5
        )
        self.text_label.place(x=x, y=y, width=int(WIDTH*2/3), height=TALKING_HEIGHT)
        self.actual_text = current_frame["text"]
        self.ready = True

        self.next_page_button()

    def clear_characters(self):
        """Remove todos os personagens da tela"""
        for label in self.character_labels:
            label.destroy()
        self.character_labels = []

    def create_empty_frame(self, parent, color=BG_COLOR, label=None):    
        if self.frame is None:
            self.frame = tk.Frame(parent, bg=color, padx=1, pady=1)
            self.ready = True    
        else:
            print("Trying to recreate a frame")

    def configure_next_frame(self, next_frame):
        self.nextFrame = next_frame

    def show_story_text(self, index):
        if index == 0:
            self.text_label.config(text="")
        self.text_label.config(text=self.actual_text[:index])
        if index < len(self.actual_text):
            self.text_label.after(TEXT_DELAY, self.show_story_text, index+1)

    def next_page(self, add):
        if 0 <= self.whichShow + add < len(self.frame_data):
            self.whichShow += add
            current_frame = self.frame_data[self.whichShow]
            
            # Atualiza background
            try:
                bg_image = Image.open(current_frame["background"])
                bg_image = bg_image.convert("RGBA")
                bg_image = bg_image.resize((WIDTH, HEIGHT), Image.LANCZOS)
                tk_bg_image = ImageTk.PhotoImage(bg_image)
                self.label.config(image=tk_bg_image)
                self.label.image = tk_bg_image
            except Exception as e:
                messagebox.showerror(f"Error loading background: {e}")
                return None

            # Atualiza personagens
            self.clear_characters()
            for char_img in current_frame.get("characters", []):
                try:
                    char_image = Image.open(char_img)
                    char_image = char_image.convert("RGBA")
                    char_image = char_image.resize((200, 400), Image.LANCZOS)
                    tk_char_image = ImageTk.PhotoImage(char_image)
                    
                    char_label = tk.Label(self.frame, image=tk_char_image, bg=BG_COLOR)
                    char_label.image = tk_char_image
                    char_label.place(x=50, y=HEIGHT-400)
                    self.character_labels.append(char_label)
                except Exception as e:
                    messagebox.showerror(f"Error loading character: {e}")

            self.actual_text = current_frame["text"]
            self.show_story_text(0)

        else:   ## FAZER ENTRAR EM GAMERFRAME QUANDO TODAS AS PAGINAS FOREM VISUALIZADAS
            self=self.nextFrame
        
        if self.nextFrame == None and self.whichShow + add >= len(self.image):
            return self.nextFrame

    def next_page_button(self):
        self.next_button = tk.Button(
            self.frame, text="Próximo", bg=COLOR_DARK_CHARCOAL,
            relief="sunken", borderwidth=2, anchor="nw",
            font=(FONT_FAMILY, 12, "bold"),
            fg="white",
            command=lambda: self.next_page(1)
        )
        self.next_button.place(x=10, y=HEIGHT-60)
    
    def previous_page_button(self):
        pass