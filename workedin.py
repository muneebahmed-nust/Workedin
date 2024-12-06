import customtkinter as ctk
from tkinter import messagebox 
import utils  

#This is the app class which navigates between pages

class App:
    def __init__(self, root):
        self.root = root
        self.x_axis=self.root.winfo_screenwidth()/2
        self.y_axis=self.root.winfo_screenheight()/2
        self.current_frame = self.select_language_page()
        self.label_data_font=("Arial", 16)
        
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

        english_language_button=ctk.CTkButton(frame, text="English", command= self.user_language_option_english)
        english_language_button.place(relx=0.45, rely=0.3, anchor="e")
        urdu_language_button=ctk.CTkButton(frame, text="اردو", command= self.user_language_option_urdu) 
        urdu_language_button.place(relx=0.55, rely=0.3, anchor="w")
        return frame
        
    def user_language_option_urdu(self):
        pass

    def user_language_option_english(self):
        self.show_page(self.signup_page_english)
        

    
    
    def signup_page_english(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        # Header
        heading = ctk.CTkLabel(frame, 
                            text="Workedin: Employment Made Easy", 
                            font=("Arial", 24))
        heading.place(relx=0.5, rely=0.03, anchor="center")
        
        # Description
        description = ctk.CTkLabel(frame, 
                                text="Find the best jobs and make connections easily!", 
                                font=("Arial", 16))
        description.place(relx=0.5, rely=0.1, anchor="center")
        
        user_name_label = ctk.CTkLabel(frame, text="User Name:", font=self.label_data_font)
        user_name_label.place(relx=0.5, rely=0.3, anchor="e")
        
        user_name_entry = ctk.CTkEntry(frame, width=200, height=30)
        user_name_entry.place(relx=0.55, rely=0.3, anchor="w")
        
        password_label = ctk.CTkLabel(frame, text="Password:", font=self.label_data_font)
        password_label.place(relx=0.5, rely=0.4, anchor="e")
        
        password_entry = ctk.CTkEntry(frame, width=200, height=30, show="*")
        password_entry.place(relx=0.55, rely=0.4, anchor="w")
        
        confirm_password_label = ctk.CTkLabel(frame, text="Confirm Password:", font=self.label_data_font)
        confirm_password_label.place(relx=0.5, rely=0.5, anchor="e")
        
        confirm_password_entry = ctk.CTkEntry(frame, width=200, height=30, show="*")
        confirm_password_entry.place(relx=0.55, rely=0.5, anchor="w")
        signup_button = ctk.CTkButton(frame, text="Sign Up", width=120, height=32, command=lambda:self.show_page(self.labour_data_entry_page))
        signup_button.place(relx=0.5, rely=0.6, anchor="center")

        return frame
    
    def labour_data_entry_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        heading=ctk.CTkLabel(frame,text="Workedin",font=("Arial",24))
        heading.place(relx=0.5, rely=0.03, anchor="center")

        name_label=ctk.CTkLabel(frame,text="Full Name:",font=("Arial",16))
        name_label.place(relx=0.4, rely=0.15, anchor="e")
        name_entry_box=ctk.CTkEntry(frame,width=200,height=30,placeholder_text="e.g Aslam Ahmed")
        name_entry_box.place(relx=0.6, rely=0.15, anchor="w")

        age_label=ctk.CTkLabel(frame,text="Age:",font=("Arial",16))
        age_label.place(relx=0.4, rely=0.22, anchor="e")
        age_entry_box=ctk.CTkEntry(frame,width=200,height=30)
        age_entry_box.place(relx=0.6, rely=0.22, anchor="w")

        phone_label=ctk.CTkLabel(frame,text="Phone:",font=("Arial",16))
        phone_label.place(relx=0.4, rely=0.29, anchor="e")
        phone_entry_box=ctk.CTkEntry(frame,width=200,height=30)
        phone_entry_box.place(relx=0.6, rely=0.29, anchor="w")

        cnic_label=ctk.CTkLabel(frame,text="CNIC:",font=("Arial",16))
        cnic_label.place(relx=0.4, rely=0.36, anchor="e")
        cnic_entry_box=ctk.CTkEntry(frame,width=200,height=30,placeholder_text="e.g 1234567890123")
        cnic_entry_box.place(relx=0.6, rely=0.36, anchor="w")

        experience_label=ctk.CTkLabel(frame,text="Number of years of experience:",font=("Arial",16))
        experience_label.place(relx=0.4, rely=0.43, anchor="e")
        experience_entry_box=ctk.CTkEntry(frame,width=200,height=30,placeholder_text="e.g 10")
        experience_entry_box.place(relx=0.6, rely=0.43, anchor="w")

        city_label=ctk.CTkLabel(frame,text="City:",font=("Arial",16))
        city_label.place(relx=0.4, rely=0.50, anchor="e")
        city_entry_box=ctk.CTkEntry(frame,width=200,height=30)
        city_entry_box.place(relx=0.6, rely=0.50, anchor="w")

        submit_button=ctk.CTkButton(frame,text="Submit",command=lambda:self.show_page(self.job_submission_page))
        submit_button.place(relx=0.4, rely=0.60, anchor="center")
       
        return frame
        
    def job_submission_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        heading=ctk.CTkLabel(frame,text="Job Submission",font=("Arial",24))
        heading.place(relx=0.5, rely=0.03, anchor="center")
        
        city_label =ctk.CTkLabel(frame, text="City",font=("Arial",16))
        city_label.place(relx=0.4, rely=0.15, anchor="e")
        city_box= ctk.CTkComboBox(frame, values= [
    # Main Cities
    "Karachi", "Lahore", "Islamabad", "Rawalpindi", "Faisalabad",
    "Peshawar", "Quetta", "Multan",
    
    # Other Cities in Alphabetical Order
    "Abbottabad", "Attock", "Bahawalpur", "Bannu", "Chakwal",
    "Chiniot", "Dera Ghazi Khan", "Ghotki", "Gujranwala", 
    "Gujrat", "Hyderabad", "Jhang", "Jhelum", "Kasur", 
    "Khuzdar", "Kotli", "Larkana", "Mardan", "Mingora",
    "Mirpur Khas", "Nawabshah", "Okara", "Rahim Yar Khan", 
    "Sargodha", "Sheikhupura", "Sialkot", "Sukkur"
    ])
    
        city_box.place(relx=0.6, rely=0.15, anchor="w")

        job_type_label = ctk.CTkLabel(frame, text="Job Type",font=("Arial",16))
        job_type_label.place(relx=0.4, rely=0.22, anchor="e")
        job_type_box= ctk.CTkComboBox(frame, values=["Driver","Labour","Electrician","Plumber","Mason","Carpenter","Painter","Cleaner","Cook","Security Guard","Other"], command=self.on_job_type_change)
        job_type_box.place(relx=0.6, rely=0.22, anchor="w")
        
        self.other_job_entry = ctk.CTkEntry(frame,placeholder_text="Please specify", width=200, height=30)
        self.other_job_entry.place(relx=0.6, rely=0.29, anchor="w")
        self.other_job_entry.configure(state="disabled")
        
        user_name_label = ctk.CTkLabel(frame, text="User Name",font=("Arial",16))
        user_name_label.place(relx=0.4, rely=0.36, anchor="e")
        user_name_entry = ctk.CTkEntry(frame,placeholder_text="e.g Aslam Ahmed", width=200, height=30)
        user_name_entry.place(relx=0.6, rely=0.36, anchor="w")

        job_description_label = ctk.CTkLabel(frame, text="Job Description",font=("Arial",16))
        job_description_label.place(relx=0.4, rely=0.43, anchor="ne")
        job_description_entry = ctk.CTkTextbox(frame, width=250, height=100)
        job_description_entry.insert("0.0", "")  # Add placeholder text
        job_description_entry.place(relx=0.6, rely=0.43, anchor="nw")

        submit_button=ctk.CTkButton(frame,text="Submit",command=lambda:self.show_page(self.job_submission_page))
        return frame

    def on_job_type_change(self, selected_job_type):
        if selected_job_type == "Other":
            # Show the entry
            self.other_job_entry.configure(state="normal")
        else:
            self.other_job_entry.configure(state="disabled")

    def validate_input(self):
        # Getting input from user
        name = self.name_entry.get()
        contact = self.contact_entry.get() 
        skill = self.skill_var.get()
        location = self.location_entry.get()

        # Checking if all the required fields are filled
        if not name or not contact or not skill or not location:
            messagebox.showwarning("Input error", "Please fill all required fields")
            return False

        # Checking if name contains only alphabets (for English) or Arabic/Urdu letters
        if not (name.isalpha() or all('\u0600' <= c <= '\u06ff' for c in name)):
            messagebox.showwarning("Input error", "Name should contain only alphabets or Urdu letters")
            return False

        # Checking if contact contains only numbers
        if not contact.isnumeric():
            messagebox.showwarning("Input error", "Contact should contain only numbers")
            return False

        # Checking if skill contains only alphabets or Urdu letters
        if not (skill.isalpha() or all('\u0600' <= c <= '\u06ff' for c in skill)):
            messagebox.showwarning("Input error", "Skill should contain only alphabets or Urdu letters")
            return False

        return True

    def clear_form(self):
        # Clear the form after successful submission
        self.name_entry.delete(0, len(self.name_entry.get()))
        self.contact_entry.delete(0, len(self.contact_entry.get()))
        self.skill_var.set("Plumber")  # Reset dropdown to default value
        self.location_entry.delete(0, len(self.location_entry.get()))

    def submit_signup(self):
        # If validation passes, display success message
        if self.validate_input():
            name = self.name_entry.get()
            messagebox.showinfo("Success", f"Sign-up successful for {name}")
            self.clear_form()  # Clear the form after successful sign-up

    def show_sign_in(self):
        # This method can show a sign-in form or a message box indicating a redirect
        messagebox.showinfo("Sign In", "Redirecting to the Sign In Page...")
    
    

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


