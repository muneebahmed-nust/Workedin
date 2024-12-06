import customtkinter as ctk
from tkinter import messagebox 
import utils  
from backend_functions import *

class EnglishInterface:
    def __init__(self, app):
        self.app = app
        self.root = app.root
        self.label_data_font = app.label_data_font
        self.heading_label_font = app.heading_label_font  # Add this line

    def signup_page(self):
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
        
        name_label = ctk.CTkLabel(frame, text="Full Name:", font=self.label_data_font)
        name_label.place(relx=0.4, rely=0.2, anchor="e")
        name_entry_box = ctk.CTkEntry(frame, width=200, height=30, placeholder_text="e.g Aslam Ahmed")
        name_entry_box.place(relx=0.6, rely=0.2, anchor="w")

        age_label = ctk.CTkLabel(frame, text="Age:", font=self.label_data_font)
        age_label.place(relx=0.4, rely=0.3, anchor="e")
        age_entry_box = ctk.CTkEntry(frame, width=200, height=30)
        age_entry_box.place(relx=0.6, rely=0.3, anchor="w")

        user_name_label = ctk.CTkLabel(frame, text="User Name:", font=self.label_data_font)
        user_name_label.place(relx=0.4, rely=0.4, anchor="e")
        user_name_entry = ctk.CTkEntry(frame, width=200, height=30)
        user_name_entry.place(relx=0.6, rely=0.4, anchor="w")
        
        password_label = ctk.CTkLabel(frame, text="Password:", font=self.label_data_font)
        password_label.place(relx=0.4, rely=0.5, anchor="e")
        password_entry = ctk.CTkEntry(frame, width=200, height=30, show="*")
        password_entry.place(relx=0.6, rely=0.5, anchor="w")
        
        confirm_password_label = ctk.CTkLabel(frame, text="Confirm Password:", font=self.label_data_font)
        confirm_password_label.place(relx=0.4, rely=0.6, anchor="e")
        confirm_password_entry = ctk.CTkEntry(frame, width=200, height=30, show="*")
        confirm_password_entry.place(relx=0.6, rely=0.6, anchor="w")

        city_label = ctk.CTkLabel(frame, text="City:", font=self.label_data_font)
        city_label.place(relx=0.4, rely=0.7, anchor="e")
        city_box = ctk.CTkComboBox(frame, values=[
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
        city_box.place(relx=0.6, rely=0.7, anchor="w")

        signup_button = ctk.CTkButton(frame, text="Sign Up", width=120, height=32, 
                                    command=lambda: self.app.show_page(self.labour_data_entry_page))
        signup_button.place(relx=0.5, rely=0.8, anchor="center")

        return frame

    def labour_data_entry_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        
        frame.pack(fill="both", expand=True)
        heading=ctk.CTkLabel(frame,text="Workedin",font=self.heading_label_font)
        heading.place(relx=0.5, rely=0.03, anchor="center")


        cnic_label=ctk.CTkLabel(frame,text="CNIC:",font=self.label_data_font)
        cnic_label.place(relx=0.4, rely=0.15, anchor="e")
        cnic_entry_box=ctk.CTkEntry(frame,width=200,height=30,placeholder_text="e.g 42101-1234567-8")
        cnic_entry_box.place(relx=0.6, rely=0.15, anchor="w")

        profession_label=ctk.CTkLabel(frame,text="Profession:",font=self.label_data_font)
        profession_label.place(relx=0.4, rely=0.29, anchor="e")
        profession_box = ctk.CTkComboBox(frame, values=[
            "Driver", "Labour", "Electrician", "Plumber", "Mason",
            "Carpenter", "Painter", "Cleaner", "Cook", "Security Guard", "Other"
        ])
        profession_box.place(relx=0.6, rely=0.29, anchor="w")

        phone_label=ctk.CTkLabel(frame,text="Phone:",font=self.label_data_font)
        phone_label.place(relx=0.4, rely=0.43, anchor="e")
        phone_entry_box=ctk.CTkEntry(frame,width=200,height=30)
        phone_entry_box.place(relx=0.6, rely=0.43, anchor="w")

        experience_label=ctk.CTkLabel(frame,text="Number of years of experience:",font=self.label_data_font)
        experience_label.place(relx=0.4, rely=0.57, anchor="e")
        experience_entry_box=ctk.CTkEntry(frame,width=200,height=30,placeholder_text="e.g 10")
        experience_entry_box.place(relx=0.6, rely=0.57, anchor="w")

        submit_button=ctk.CTkButton(frame,text="Submit",command=lambda:self.app.show_page(self.job_submission_page))
        submit_button.place(relx=0.4, rely=0.75, anchor="center")
       
        return frame

    def job_submission_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)

        heading = ctk.CTkLabel(frame, text="Job Submission", font=self.heading_label_font)
        heading.place(relx=0.5, rely=0.1, anchor="center")

        city_label = ctk.CTkLabel(frame, text="City", font=self.label_data_font)
        city_label.place(relx=0.35, rely=0.25, anchor="e")
        city_box = ctk.CTkComboBox(frame, values=[
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
        city_box.place(relx=0.4, rely=0.3, anchor="w")

        job_type_label = ctk.CTkLabel(frame, text="Job Type", font=self.label_data_font)
        job_type_label.place(relx=0.35, rely=0.35, anchor="e")

        job_type_box = ctk.CTkComboBox(frame, values=[
            "Driver", "Labour", "Electrician", "Plumber", "Mason",
            "Carpenter", "Painter", "Cleaner", "Cook", "Security Guard", "Other"
        ], command=self.on_job_type_change)
        job_type_box.place(relx=0.4, rely=0.35, anchor="w")

        self.other_job_entry = ctk.CTkEntry(frame, placeholder_text="Please specify", width=200, height=30)
        self.other_job_entry.place(relx=0.4, rely=0.45, anchor="w")
        self.other_job_entry.configure(state="disabled")

        user_name_label = ctk.CTkLabel(frame, text="User Name", font=self.label_data_font)
        user_name_label.place(relx=0.35, rely=0.55, anchor="e")

        user_name_entry = ctk.CTkEntry(frame, placeholder_text="e.g Aslam Ahmed", width=200, height=30)
        user_name_entry.place(relx=0.4, rely=0.55, anchor="w")

        job_description_label = ctk.CTkLabel(frame, text="Job Description", font=self.label_data_font)
        job_description_label.place(relx=0.35, rely=0.65, anchor="e")

        job_description_entry = ctk.CTkTextbox(frame, width=300, height=120)
        job_description_entry.insert("0.0", "")  # Add placeholder text
        job_description_entry.place(relx=0.4, rely=0.65, anchor="w")

        submit_button = ctk.CTkButton(frame, text="Submit", command=lambda: self.app.show_page(self.job_submission_page))
        submit_button.place(relx=0.5, rely=0.9, anchor="center")

        return frame

    def on_job_type_change(self, selected_job_type):
        if selected_job_type == "Other":
            self.other_job_entry.configure(state="normal")
        else:
            self.other_job_entry.configure(state="disabled")