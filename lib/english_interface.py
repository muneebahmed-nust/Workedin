import customtkinter as ctk
from tkinter import messagebox 
import utils  
from lib.backend_functions import *
from lib.authentication_firebase import *
from firebase_admin import auth


class EnglishInterface:
    def __init__(self, app):
        self.app = app
        self.root = app.root
        self.label_data_font = app.label_data_font
        self.heading_label_font = app.heading_label_font  # Add this line
        self.db=app.db

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
        self.name_entry_box = ctk.CTkEntry(frame, width=200, height=30, placeholder_text="e.g Aslam Ahmed")
        self.name_entry_box.place(relx=0.6, rely=0.2, anchor="w")

        dob_label = ctk.CTkLabel(frame, text="Date of Birth:", font=self.label_data_font)
        dob_label.place(relx=0.4, rely=0.3, anchor="e")
        
        # Create date picker frame
        date_frame = ctk.CTkFrame(frame)
        date_frame.place(relx=0.6, rely=0.3, anchor="w")
        
        # Create calendar button
        self.dob_entry_box = ctk.CTkEntry(date_frame, width=170, height=30)
        self.dob_entry_box.pack(side="left", padx=(0,5))
        
        def open_calendar():
            # Create calendar popup
            from tkcalendar import Calendar
            top = ctk.CTkToplevel(frame)
            top.geometry("300x250")
            cal = Calendar(top, selectmode='day', date_pattern='dd/mm/yyyy')
            cal.pack(pady=10)
            
            def get_date():
                self.dob_entry_box.delete(0, "end")
                self.dob_entry_box.insert(0, cal.get_date())
                top.destroy()
                
            select_btn = ctk.CTkButton(top, text="Select", command=get_date)
            select_btn.pack()
            
        calendar_btn = ctk.CTkButton(date_frame, text="📅", width=25, height=30, command=open_calendar)
        calendar_btn.pack(side="left")

        email_label = ctk.CTkLabel(frame, text="Email:", font=self.label_data_font)
        email_label.place(relx=0.4, rely=0.4, anchor="e")
        self.email_entry = ctk.CTkEntry(frame, width=200, height=30)
        self.email_entry.place(relx=0.6, rely=0.4, anchor="w")
        
        password_label = ctk.CTkLabel(frame, text="Password:", font=self.label_data_font)
        password_label.place(relx=0.4, rely=0.5, anchor="e")
        self.password_entry = ctk.CTkEntry(frame, width=200, height=30, show="*")
        self.password_entry.place(relx=0.6, rely=0.5, anchor="w")
        
        confirm_password_label = ctk.CTkLabel(frame, text="Confirm Password:", font=self.label_data_font)
        confirm_password_label.place(relx=0.4, rely=0.6, anchor="e")
        self.confirm_password_entry = ctk.CTkEntry(frame, width=200, height=30, show="*")
        self.confirm_password_entry.place(relx=0.6, rely=0.6, anchor="w")

        user_type_label = ctk.CTkLabel(frame, text="User Type:", font=self.label_data_font)
        user_type_label.place(relx=0.4, rely=0.7, anchor="e")
        self.user_type_box = ctk.CTkComboBox(frame, values=["Employer", "Labour"])
        self.user_type_box.place(relx=0.6, rely=0.7, anchor="w")

        signup_button = ctk.CTkButton(frame, text="Sign Up", width=120, height=32, 
                                    command=lambda: self.create_user())
        signup_button.place(relx=0.5, rely=0.8, anchor="center")

        return frame

    async def create_user(self):
        email=self.email_entry.get()
        password=self.password_entry.get()
        user_type=self.user_type_box.get()
        dob=self.dob_entry_box.get()
        name=self.name_entry_box.get()
        if (not_letter(name)):
            messagebox.showerror("Error","Name must contain only letters")
            return
        
        
        try :
            user=auth.create_user(email=email,password=password)
            print(user)
            print("Sucees user created")
        except:
            pass
        
        
        self.db.collection(user_type).document(email).set({
        "name": name,
        "dob": dob,        
        })

        self.app.show_page(self.labour_data_entry_page)
        
    def login_screen(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        # Create the back button
        back_button = ctk.CTkButton(frame, text=self.get_text("Back"), command=self.go_back)
        back_button.pack(pady=10, anchor="w", padx=10)

        # Label for sign-in screen
        self.title_label = ctk.CTkLabel(frame, text=self.get_text("Sign In"), font=("Arial", 24))
        self.title_label.pack(pady=20)

        # Dropdown for selecting user type (Tradesperson or Employer)
        self.user_type_dropdown = ctk.CTkOptionMenu(frame, values=[self.get_text("Tradesperson"), self.get_text("Employer")])
        self.user_type_dropdown.pack(pady=10)

        # Language selection (English or Urdu)
        language_label = ctk.CTkLabel(frame, text=self.get_text("Select Language"), font=("Arial", 16))
        language_label.pack(pady=10)

        self.language_dropdown = ctk.CTkOptionMenu(frame, values=[self.get_text("English"), self.get_text("Urdu")], command=self.change_language)
        self.language_dropdown.pack(pady=10)

        # Label and Entry for username
        self.username_label = ctk.CTkLabel(frame, text=self.get_text("Username"), font=("Arial", 16))
        self.username_label.pack(pady=5)

        self.username_entry = ctk.CTkEntry(frame, placeholder_text=self.get_text("Enter your username"))
        self.username_entry.pack(pady=5)

        # Label and Entry for password
        self.password_label = ctk.CTkLabel(frame, text=self.get_text("Password"), font=("Arial", 16))
        self.password_label.pack(pady=5)

        self.password_entry = ctk.CTkEntry(frame, placeholder_text=self.get_text("Enter your password"), show="*")
        self.password_entry.pack(pady=5)

        # Sign-in button
        signin_button = ctk.CTkButton(frame, text=self.get_text("Sign In"), command=self.sign_in)
        signin_button.pack(pady=20)

        return frame
    
    def labour_data_entry_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        
        frame.pack(fill="both", expand=True)
        heading=ctk.CTkLabel(frame,text="Workedin",font=self.heading_label_font)
        heading.place(relx=0.5, rely=0.03, anchor="center")


        cnic_label=ctk.CTkLabel(frame,text="CNIC:",font=self.label_data_font)
        cnic_label.place(relx=0.4, rely=0.15, anchor="e")
        self.cnic_entry_box=ctk.CTkEntry(frame,width=200,height=30,placeholder_text="e.g 42101-1234567-8")
        self.cnic_entry_box.place(relx=0.6, rely=0.15, anchor="w")

        profession_label=ctk.CTkLabel(frame,text="Profession:",font=self.label_data_font)
        profession_label.place(relx=0.4, rely=0.29, anchor="e")
        self.profession_box = ctk.CTkComboBox(frame, values=[
            "Driver", "Labour", "Electrician", "Plumber", "Mason",
            "Carpenter", "Painter", "Cleaner", "Cook", "Security Guard", "Other"
        ])
        self.profession_box.place(relx=0.6, rely=0.29, anchor="w")

        phone_label=ctk.CTkLabel(frame,text="Phone:",font=self.label_data_font)
        phone_label.place(relx=0.4, rely=0.43, anchor="e")
        self.phone_entry_box=ctk.CTkEntry(frame,width=200,height=30)
        self.phone_entry_box.place(relx=0.6, rely=0.43, anchor="w")

        experience_label=ctk.CTkLabel(frame,text="Number of years of experience:",font=self.label_data_font)
        experience_label.place(relx=0.4, rely=0.57, anchor="e")
        self.experience_entry_box=ctk.CTkEntry(frame,width=200,height=30,placeholder_text="e.g 10")
        self.experience_entry_box.place(relx=0.6, rely=0.57, anchor="w")
       
        city_label = ctk.CTkLabel(frame, text="City:", font=self.label_data_font)
        city_label.place(relx=0.4, rely=0.7, anchor="e")
        self.city_box = ctk.CTkComboBox(frame, values=[
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
        self.city_box.place(relx=0.6, rely=0.7, anchor="w")
       
        submit_button=ctk.CTkButton(frame,text="Submit",command=lambda:self.app.show_page(self.job_submission_page))
        submit_button.place(relx=0.4, rely=0.75, anchor="center")
       
        return frame
    
    async def labour_database_entry(self):
        cnic=self.cnic
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