import customtkinter as ctk
from tkinter import messagebox 
import utils  
from backend_functions import *
from english_interface import *
from urdu_interface import *

#This is the app class which navigates between pages
class App:

    def __init__(self, root):
        self.root = root
        self.x_axis=self.root.winfo_screenwidth()/2
        self.y_axis=self.root.winfo_screenheight()/2
        self.current_frame = self.select_language_page()
        self.label_data_font=("Arial", 16)
        self.heading_label_font=("Arial",24)

    def show_page(self, page_func):
        # Destroy current frame if it exists
        if self.current_frame:
            self.current_frame.destroy()
        # Create new frame
        self.current_frame = page_func()

    def select_language_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        select_language_heading=ctk.CTkLabel(frame, 
                                    text="Select Language \nزبان منتخب کریں", 
                                    font=("Arial", 24))
        select_language_heading.place(relx=0.5, rely=0.20, anchor="center")

        english_language_button=ctk.CTkButton(frame, text="English", command=self.show_english)
        english_language_button.place(relx=0.45, rely=0.3, anchor="e")
        urdu_language_button=ctk.CTkButton(frame, text="اردو", command=self.show_urdu)
        urdu_language_button.place(relx=0.55, rely=0.3, anchor="w")
        return frame

    def show_english(self):
        self.english = EnglishInterface(self)
        self.show_page(self.english.signup_page)

    def show_urdu(self):
        self.urdu = UrduInterface(self)
        self.show_page(self.urdu.signup_page)






def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    root = ctk.CTk()
    root.state("zoomed")
    print(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.geometry("1000x600")
    root.title("Workedin")
    app = App(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
