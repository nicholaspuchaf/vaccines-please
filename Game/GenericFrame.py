
import tkinter as tk
from tkinter import messagebox # Import messagebox for custom alerts
from PIL import Image, ImageTk # Import Pillow for image manipulation

from constants import *

class GenericFrame:

    def __init__(self):
        self.frame = None # Frame de Tkinter que esse Obj tera
        self.texts = [] # colecao de texts para mostrar por esse obj
        self.images = [] # colecao de images p mostrar
        self.whichShow = 0 # indica qual foto e text mostrar
        self.label = None # Ponteiro para o label onde esta a imagem
        self.text_label = None # Ponteiro para onde esta guardado o texto
        self.actual_text = None

        self.next_button = None
        self.previuous_button = None

        self.ready = False

    def isReady(self):
        return self.ready

    def add_text_and_image(self, text, image):
        self.texts.append(text)
        self.images.append(image)

    def forget(self):
        self.frame.forget()
        
    def pack_frame(self):
        if self.ready == True:
            self.frame.pack(pady=10, expand=True, fill="both")
            self.show_story_text(0)
        else:
            print("Tried to pack a not ready frame")

    def create_frame_with_image(self,parent,x=WIDTH/6,y=HEIGHT-60):
        self.frame = tk.Frame(parent, bg=BG_COLOR, padx=1, pady=1)
        image = None
        try:
            image = Image.open(self.images[self.whichShow])
        except FileNotFoundError:
            messagebox.showerror(f"Officer file not found at {self.images[self.whichShow]}")
            return None    
        except Exception as e:
            messagebox.showerror(f"Error at Officer loading : {e}")
            return None

        image = image.convert("RGBA")
        image = image.resize((WIDTH, HEIGHT), Image.LANCZOS)

        tk_image = ImageTk.PhotoImage(image)

        self.label = tk.Label(self.frame, image=tk_image)

        self.label.image = tk_image
        self.label.place(x=10,y=10,width=WIDTH-20, height=HEIGHT-20)
        self.label.lower()

        self.text_label = tk.Label(self.frame, bg=COLOR_DARK_CHARCOAL,
                                   relief="sunken", borderwidth=2, anchor="nw",
                                   font=(FONT_FAMILY, 12, "bold"),
                                   fg="white",
                                   wraplength=int(WIDTH*2/3)-10,
                                   padx=5)

        self.text_label.place(x=x, y=y, width=int(WIDTH*2/3), height=TALKING_HEIGHT)
        # self.text_label.config(text=self.texts[self.whichShow])
        self.actual_text = self.texts[self.whichShow]
        self.ready = True

        self.next_page_button()

    def show_story_text(self, index):
        if(index == 0):
            self.text_label.config(text="")
        self.text_label.config(text=self.actual_text[:index])
        if index < len(self.actual_text):
            self.text_label.after(TEXT_DELAY, self.show_story_text, index+1)

    def next_page(self, add):
        if self.whichShow + add < len(self.images) and self.whichShow >= 0:
            self.whichShow = self.whichShow + add
            image = None
            try:
                image = Image.open(self.images[self.whichShow])
            except FileNotFoundError:
                messagebox.showerror(f"Officer file not found at {self.images[self.whichShow]}")
                return None    
            except Exception as e:
                messagebox.showerror(f"Error at Officer loading : {e}")
                return None
            image = image.convert("RGBA")
            image = image.resize((WIDTH, HEIGHT), Image.LANCZOS)
            tk_image = ImageTk.PhotoImage(image)
            self.label.config(image=tk_image)
            self.label.image = tk_image
            self.actual_text = self.texts[self.whichShow]
            self.show_story_text(0)
        
        if self.whichShow + add == len(self.images):
            # start game
            pass

    def next_page_button(self):
        self.next_button = tk.Button(self.frame, text="Proximo", bg=COLOR_DARK_CHARCOAL,
                                    relief="sunken", borderwidth=2, anchor="nw",
                                    font=(FONT_FAMILY, 12, "bold"),
                                    fg="white",
                                    command=lambda:self.next_page(1))
        self.next_button.place(x=10, y=HEIGHT-60)
    
    def previous_page_button(self):
        pass
