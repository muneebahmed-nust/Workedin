import customtkinter as ctk
from tkinter import messagebox 
import utils  
from backend_functions import *

class UrduInterface:
    def __init__(self, app):
        self.app = app
        self.root = app.root
        self.label_data_font = app.label_data_font

    def signup_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        heading = ctk.CTkLabel(frame, text="Urdu Interface Coming Soon", font=("Arial", 24))
        heading.place(relx=0.5, rely=0.5, anchor="center")
        return frame