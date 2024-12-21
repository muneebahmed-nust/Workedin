import customtkinter as ctk
from tkinter import messagebox 
import utils  
from lib.backend_functions import *
from lib.authentication_firebase import *
from firebase_admin import auth
import asyncio
from tkcalendar import Calendar
from lib.data_resource import *
from PIL import Image

class EnglishInterface:
    def __init__(self, app):
        self.app = app
        self.root = app.root
        self.label_data_font = app.label_data_font
        self.heading_label_font = app.heading_label_font  # Add this line
        self.db=app.db
        self.current_user=None
        self.current_user_type=None

########################################################################################################
#########################################################################################################        
   
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

        

        email_label = ctk.CTkLabel(frame, text="Email:", font=self.label_data_font)
        email_label.place(relx=0.4, rely=0.3, anchor="e")
        self.email_entry = ctk.CTkEntry(frame, width=200, height=30)
        self.email_entry.place(relx=0.6, rely=0.3, anchor="w")
        
        password_label = ctk.CTkLabel(frame, text="Password:", font=self.label_data_font)
        password_label.place(relx=0.4, rely=0.4, anchor="e")
        self.password_entry = ctk.CTkEntry(frame, width=200, height=30, show="*")
        self.password_entry.place(relx=0.6, rely=0.4, anchor="w")
        
        confirm_password_label = ctk.CTkLabel(frame, text="Confirm Password:", font=self.label_data_font)
        confirm_password_label.place(relx=0.4, rely=0.5, anchor="e")
        self.confirm_password_entry = ctk.CTkEntry(frame, width=200, height=30, show="*")
        self.confirm_password_entry.place(relx=0.6, rely=0.5, anchor="w")

        user_type_label = ctk.CTkLabel(frame, text="User Type:", font=self.label_data_font)
        user_type_label.place(relx=0.4, rely=0.6, anchor="e")
        self.user_type_box = ctk.CTkComboBox(frame, values=user_types)
        self.user_type_box.place(relx=0.6, rely=0.6, anchor="w")

        signup_button = ctk.CTkButton(frame, text="Sign Up", width=120, height=32, 
                                    command=lambda: self.run_create_user())
        signup_button.place(relx=0.5, rely=0.8, anchor="center")

        login_button=ctk.CTkButton(frame,text="Already have an account? Log In",command=lambda:self.app.show_page(self.login_screen))
        login_button.place(relx=0.5, rely=0.85, anchor="center")

        return frame
    
    async def handle_signup(self, email, password, user_type, name):
        # Run the asynchronous create_user method
        print(email,password,user_type,name)
     
        print("Starting auth")
    #    auth.create_user(email=email,password=password)
        print("auth Sucees user created")
        
        print("database user name entered")
   
       
        self.db.collection(user_type).document(email).set({
                "name": name, 
                "password":password,
            })
        
    def run_create_user(self):
        # Run the create_user coroutine in an event loop
        asyncio.run(self.create_user())
        
        
    async def create_user(self):
        email=self.email_entry.get()
        password=self.password_entry.get()
        confirm_password=self.confirm_password_entry.get()
        user_type=self.user_type_box.get()
        name=self.name_entry_box.get()

        
        if(is_empty(email) or is_empty(password) or is_empty(confirm_password) or is_empty( user_type)  or is_empty(name)):
            messagebox.showerror("Input Error", "Please fill out all fields")
            return
        else:    
            if (not_letter(name)):
                messagebox.showerror("Error","Name must contain only letters")
                return
            if (password!=confirm_password):
                messagebox.showerror("Error","Password and confirm password do not match")
                return
            if(is_invalid_email(email)):
                messagebox.showerror("Error","Invalid email")
                return
            else:
                await self.handle_signup(email,password,user_type,name)
            
            if(user_type=="Tradesperson"):
                self.app.show_page(self.labour_main_dashboard)
            else:
                self.app.show_page(self.employer_main_dashboard)

    #####################################################################################################
    #####################################################################################################    

    def login_screen(self):
        # Create a frame for the login screen
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        # Label for login screen
        title_label = ctk.CTkLabel(frame, text="Log In", font=self.heading_label_font)
        title_label.place(relx=0.5, rely=0.2, anchor="center")  

        # Dropdown for selecting user type (Tradesperson or Employer)
        self.user_type_dropdown = ctk.CTkOptionMenu(frame, values=user_types)
        self.user_type_dropdown.place(relx=0.5, rely=0.3, anchor="center")  

        # Label and Entry for username
        username_label = ctk.CTkLabel(frame, text="Username", font=self.heading_label_font)
        username_label.place(relx=0.5, rely=0.4, anchor="center")  

        self.username_entry = ctk.CTkEntry(frame, placeholder_text="Enter your username")
        self.username_entry.place(relx=0.5, rely=0.45, anchor="center") 

        # Label and Entry for password
        password_label = ctk.CTkLabel(frame, text="Password", font=self.heading_label_font)
        password_label.place(relx=0.5, rely=0.55, anchor="center")  

        self.password_entry = ctk.CTkEntry(frame, placeholder_text="Enter your password", show="*")
        self.password_entry.place(relx=0.5, rely=0.6, anchor="center")  

        # login-in button
        Login_button = ctk.CTkButton(frame, text="Log In", command=self.log_in)
        Login_button.place(relx=0.5, rely=0.7, anchor="center")  

        signup_button=ctk.CTkButton(frame,text="Don't have an account? Sign Up",command=lambda:self.app.show_page(self.signup_page))
        signup_button.place(relx=0.5, rely=0.8, anchor="center")

        return frame
    
    
    def login_database_retrieve(self,username,user_type):
       return self.db.collection(user_type).document(username).get()
          

    def log_in(self):
        """Method to handle the login action"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_type=self.user_type_dropdown.get()
        
        pass_checker=self.login_database_retrieve(username,user_type).to_dict()

        if password==pass_checker["password"]:
            self.current_user=username
            self.current_user_type=user_type
            if(user_type=="Tradesperson"):
                self.app.show_page(self.labour_main_dashboard)
            else:
                self.app.show_page(self.employer_main_dashboard)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def logout(self):
            self.current_user=None
            self.current_user_type=None
            self.app.show_page(self.login_screen)
    ##########################################################################################################
    ##########################################################################################################
    

    ##########################################################################################################
    ##########################################################################################################

    def change_password_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        # Header
        heading = ctk.CTkLabel(frame, 
                            text="Change Password", 
                            font=("Arial", 24))
        heading.place(relx=0.5, rely=0.03, anchor="center")
        
        # Current Password field
        current_password_label = ctk.CTkLabel(frame, text="Current Password", font=self.label_data_font)
        current_password_label.place(relx=0.4, rely=0.2, anchor="e")
        self.current_password_entry = ctk.CTkEntry(frame, width=300, height=30, show="*", placeholder_text="Enter current password")
        self.current_password_entry.place(relx=0.6, rely=0.2, anchor="w")
        
        # New Password field
        new_password_label = ctk.CTkLabel(frame, text="New Password", font=self.label_data_font)
        new_password_label.place(relx=0.4, rely=0.3, anchor="e")
        self.new_password_entry = ctk.CTkEntry(frame, width=300, height=30, show="*", placeholder_text="Enter new password")
        self.new_password_entry.place(relx=0.6, rely=0.3, anchor="w")
        
        # Confirm New Password field
        confirm_new_password_label = ctk.CTkLabel(frame, text="Confirm New Password", font=self.label_data_font)
        confirm_new_password_label.place(relx=0.4, rely=0.4, anchor="e")
        self.confirm_new_password_entry = ctk.CTkEntry(frame, width=300, height=30, show="*", placeholder_text="Confirm new password")
        self.confirm_new_password_entry.place(relx=0.6, rely=0.4, anchor="w")
        
        # Save button
        save_button = ctk.CTkButton(frame, text="Save Changes", width=200, height=40, fg_color="#2C7CDB", hover_color="#1C5FAF", command=self.save_password_changes)
        save_button.place(relx=0.5, rely=0.6, anchor="center")
        
        # Back button
        back_button = ctk.CTkButton(frame, text="Back", width=200, height=40, fg_color="#DB2C2C", hover_color="#AF1C1C")
        back_button.place(relx=0.5, rely=0.7, anchor="center")
        
        return frame
    
    def new_password_database_entry(self,new_password):
        dict = self.db.collection(self.current_user_type).document(self.current_user).get().to_dict()
        dict['password']= new_password
        self.db.collection(self.current_user_type).document(self.current_user).set(dict)

    def save_password_changes(self):
        current_password = self.current_password_entry.get()
        new_password = self.new_password_entry.get()
        confirm_new_password = self.confirm_new_password_entry.get()

        if is_empty(current_password) or is_empty(new_password) or is_empty(confirm_new_password):
            messagebox.showerror("Error", "Please fill out all fields.")
            return
        
        if new_password != confirm_new_password:    
            messagebox.showerror("Error", "New password and confirm password do not match.")
            return
        
        # Save changes to database
        self.new_password_database_entry(new_password)
        if(self.current_user_type=="Tradesperson"):
            self.app.show_page(self.labour_main_dashboard)
        else:
            self.app.show_page(self.employer_main_dashboard)

########################################################################################################################
########################################################################################################################
    
    def labour_main_dashboard(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)

        # Main screen title
        self.title_label = ctk.CTkLabel(frame, text="Laborer Dashboard", font=self.heading_label_font)
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        # Buttons for searching jobs 
        search_jobs_button = ctk.CTkButton(frame, text="Search Jobs", command=lambda:self.app.show_page(self.job_show_page))
        search_jobs_button.place(relx=0.5, rely=0.3, anchor="center")

        update_profile_button = ctk.CTkButton(frame, text="Update Profile", command=lambda:self.app.show_page(self.labour_data_entry_page))
        update_profile_button.place(relx=0.5, rely=0.4, anchor="center")

        # Change password button
        change_password_button = ctk.CTkButton(frame, text="Change Password", command=lambda:self.app.show_page(self.change_password_page))
        change_password_button.place(relx=0.5, rely=0.5, anchor="center")

        # Logout Button
        logout_button = ctk.CTkButton(frame, text="Logout", command=self.logout)
        logout_button.place(relx=0.95, rely=0.05, anchor="center")
        
        return frame
    
###############################################################################################################################
###############################################################################################################################

    
    def labour_data_entry_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)

        # Header
        heading = ctk.CTkLabel(frame, text="Workedin", font=self.heading_label_font)
        heading.place(relx=0.5, rely=0.05, anchor="center")

        # Form fields with consistent spacing
        y_start = 0.15  # Starting y position
        y_increment = 0.1  # Space between fields

        # CNIC
        cnic_label = ctk.CTkLabel(frame, text="CNIC:", font=self.label_data_font)
        cnic_label.place(relx=0.35, rely=y_start, anchor="e")
        self.cnic_entry_box = ctk.CTkEntry(frame, width=250, height=35, placeholder_text="e.g 4210112345678")
        self.cnic_entry_box.place(relx=0.4, rely=y_start, anchor="w")

        # Profession
        profession_label = ctk.CTkLabel(frame, text="Profession:", font=self.label_data_font)
        profession_label.place(relx=0.35, rely=y_start + y_increment, anchor="e")
        self.profession_box = ctk.CTkComboBox(frame, values=professions, width=250, height=35)
        self.profession_box.place(relx=0.4, rely=y_start + y_increment, anchor="w")

        # Date of Birth
        dob_label = ctk.CTkLabel(frame, text="Date of Birth:", font=self.label_data_font)
        dob_label.place(relx=0.35, rely=y_start + y_increment*2, anchor="e")
        
        date_frame = ctk.CTkFrame(frame)
        date_frame.place(relx=0.4, rely=y_start + y_increment*2, anchor="w")
        
        self.dob_entry_box = ctk.CTkEntry(date_frame, width=215, height=35)
        self.dob_entry_box.pack(side="left", padx=(0,5))
        
        self.calendar_frame = None
        
        def get_date():
            self.dob_entry_box.delete(0, "end")
            self.dob_entry_box.insert(0, self.cal.get_date())
            if self.calendar_frame:
                self.calendar_frame.destroy()
                self.calendar_frame = None
            
        def toggle_calendar():
            if self.calendar_frame:
                self.calendar_frame.destroy()
                self.calendar_frame = None
            else:
                self.calendar_frame = ctk.CTkFrame(frame)
                self.calendar_frame.place(relx=0.7, rely=y_start + y_increment*2, anchor="w")
                self.cal = Calendar(self.calendar_frame, selectmode='day', date_pattern='dd/mm/yyyy')
                self.cal.pack()
                select_btn = ctk.CTkButton(self.calendar_frame, text="Select", command=get_date)
                select_btn.pack(pady=5)

        calendar_btn = ctk.CTkButton(date_frame, text="📅", width=30, height=35, command=toggle_calendar)
        calendar_btn.pack(side="left")

        # Phone
        phone_label = ctk.CTkLabel(frame, text="Phone:", font=self.label_data_font)
        phone_label.place(relx=0.35, rely=y_start + y_increment*3, anchor="e")
        self.phone_entry_box = ctk.CTkEntry(frame, width=250, height=35, placeholder_text="e.g 03001234567")
        self.phone_entry_box.place(relx=0.4, rely=y_start + y_increment*3, anchor="w")

        # Experience
        experience_label = ctk.CTkLabel(frame, text="Years of Experience:", font=self.label_data_font)
        experience_label.place(relx=0.35, rely=y_start + y_increment*4, anchor="e")
        self.experience_entry_box = ctk.CTkEntry(frame, width=250, height=35, placeholder_text="e.g 10")
        self.experience_entry_box.place(relx=0.4, rely=y_start + y_increment*4, anchor="w")

        # City
        city_label = ctk.CTkLabel(frame, text="City:", font=self.label_data_font)
        city_label.place(relx=0.35, rely=y_start + y_increment*5, anchor="e")
        self.city_box = ctk.CTkComboBox(frame, values=cities, width=250, height=35)
        self.city_box.place(relx=0.4, rely=y_start + y_increment*5, anchor="w")

        # Buttons
        submit_button = ctk.CTkButton(frame, text="Submit", command=self.labour_entry, width=120, height=35)
        submit_button.place(relx=0.5, rely=y_start + y_increment*6, anchor="center")

        back_button = ctk.CTkButton(frame, text="Back", width=120, height=35, 
                                   command=lambda: self.app.show_page(self.labour_main_dashboard))
        back_button.place(relx=0.35, rely=y_start + y_increment*6, anchor="center")

        return frame
    
    def labour_database_entry(self,cnic,profession,phone,experience,dob,city):
        dict = self.db.collection(self.current_user_type).document(self.current_user).get().to_dict()
     
        dict['profession']= profession
        dict["phone"]= phone
        dict["experience"]= experience
        dict["dob"]= dob
        dict["city"]= city
        dict["cnic"]=cnic
        self.db.collection(self.current_user_type).document(self.current_user).set(dict)
        

    def labour_entry(self):
        cnic=self.cnic_entry_box.get()
        profession=self.profession_box.get()
        phone=self.phone_entry_box.get()
        experience=self.experience_entry_box.get()
        dob=self.dob_entry_box.get()
        city=self.city_box.get()

        if(is_empty(cnic) or is_empty(profession) or is_empty(phone) or is_empty(experience) or is_empty(dob) or is_empty(city)):
            messagebox.showerror("Error","Please fill out all fields")
            return
        else:
            if(is_invalid_cnic(cnic)):
                messagebox.showerror("Input Error","Please enter a valid cnic number")
                return
            if (is_invalid_phone(phone)):
                messagebox.showerror("Input Error","Please enter a valid phone number")
                return
            self.labour_database_entry(cnic,profession,phone,experience,dob,city)
    
            self.app.show_page(self.labour_main_dashboard)

###############################################################################################################################
###############################################################################################################################

    def job_show_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        # Header
        heading = ctk.CTkLabel(frame, 
                            text="Available Jobs", 
                            font=("Arial", 24))
        heading.place(relx=0.5, rely=0.05, anchor="center")
        
        # City Filter
        city_label = ctk.CTkLabel(frame, text="Filter by City", font=self.label_data_font)
        city_label.place(relx=0.3, rely=0.1, anchor="e")
        city_filter = ctk.CTkComboBox(frame, values=["All"] + ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Peshawar", "Multan", "Abbottabad", "Attock", "Bahawalpur", "Bannu", "Chakwal", "Chiniot", "Dera Ghazi Khan", "Ghotki", "Gujranwala", "Gujrat", "Hyderabad", "Jhang", "Jhelum", "Kasur", "Khuzdar", "Kotli", "Larkana", "Mardan", "Mingora", "Mirpur Khas", "Nawabshah", "Okara", "Rahim Yar Khan", "Sargodha", "Sheikhupura", "Sialkot", "Sukkur"])
        city_filter.place(relx=0.4, rely=0.1, anchor="w")
        
        # Scrollable Frame for Job List
        scrollable_frame = ctk.CTkScrollableFrame(frame, width=900, height=450)
        scrollable_frame.place(relx=0.5, rely=0.2, anchor="n")
        
        # Job List
        job_list = [
            {"title": "Software Engineer", "company": "Tech Corp", "location": "Lahore", "description": "Develop and maintain software applications."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Project Manager", "company": "Project Solutions", "location": "Islamabad", "description": "Manage and oversee project development."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            {"title": "Data Analyst", "company": "Data Inc.", "location": "Karachi", "description": "Analyze and interpret complex data sets."},
            
            # Add more job data as needed
        ]
        
        # Display Jobs
        def display_jobs(city):
            for widget in scrollable_frame.winfo_children():
                widget.destroy()
            
            filtered_job_list = [job for job in job_list if city == "All" or job["location"] == city]
            
            for index, job in enumerate(filtered_job_list):
                job_frame = ctk.CTkFrame(scrollable_frame, width=880, height=100, border_width=1, border_color="gray")
                job_frame.pack(pady=10)
                
                job_title = ctk.CTkLabel(job_frame, text=job["title"], font=("Arial", 18))
                job_title.place(relx=0.05, rely=0.2, anchor="w")
                
                job_company = ctk.CTkLabel(job_frame, text=f"Company: {job['company']}", font=("Arial", 14))
                job_company.place(relx=0.05, rely=0.5, anchor="w")
                
                job_location = ctk.CTkLabel(job_frame, text=f"Location: {job['location']}", font=("Arial", 14))
                job_location.place(relx=0.05, rely=0.8, anchor="w")
                
                job_description = ctk.CTkLabel(job_frame, text=job["description"], font=("Arial", 12))
                job_description.place(relx=0.5, rely=0.5, anchor="center")
        
        city_filter.set("All")
        city_filter.bind("<<ComboboxSelected>>", lambda event: display_jobs(city_filter.get()))
        
        display_jobs("All")
        
        # Back Button
        back_button = ctk.CTkButton(frame, text="Back", width=120, height=32, command=lambda: self.app.show_page(self.app.labour_main_dashboard))
        back_button.place(relx=0.5, rely=0.9, anchor="center")
        
        return frame
#####################################################################################################################
###############################################################################################################################
    def employer_main_dashboard(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        # Header
        heading = ctk.CTkLabel(frame, 
                            text="Employer Dashboard", 
                            font=("Arial", 24))
        heading.place(relx=0.5, rely=0.03, anchor="center")
        
        # Description
        description = ctk.CTkLabel(frame, 
                                text="Manage your job postings and view applications", 
                                font=("Arial", 16))
        description.place(relx=0.5, rely=0.1, anchor="center")
        
        # Job Postings Button
        job_postings_button = ctk.CTkButton(frame, text="View Job Postings", width=200, height=40, )
        job_postings_button.place(relx=0.5, rely=0.3, anchor="center")
        
        # Create Job Posting Button
        create_job_button = ctk.CTkButton(frame, text="Create Job Posting", width=200, height=40, 
                                        command=lambda: self.app.show_page(self.job_submission_page))
        create_job_button.place(relx=0.5, rely=0.4, anchor="center")
        
        # Change Password Button
        change_password_button = ctk.CTkButton(frame, text="Change Password", width=200, height=40,
                                             command=lambda: self.app.show_page(self.change_password_page))
        change_password_button.place(relx=0.5, rely=0.5, anchor="center")
        
        # Profile Button
        profile_button = ctk.CTkButton(frame, text="Profile", width=200, height=40)
        profile_button.place(relx=0.5, rely=0.6, anchor="center")
        
        # Logout Button
        logout_button = ctk.CTkButton(frame, text="Logout", width=200, height=40, 
                                    command=lambda: self.logout())
        logout_button.place(relx=0.5, rely=0.7, anchor="center")
        
        return frame
   
####################################################################################################################
#############################################################################################################################  
    
    def job_submission_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)

        heading = ctk.CTkLabel(frame, text="Job Submission", font=self.heading_label_font)
        heading.place(relx=0.5, rely=0.1, anchor="center")

        city_label = ctk.CTkLabel(frame, text="City", font=self.label_data_font)
        city_label.place(relx=0.35, rely=0.25, anchor="e")
        city_box = ctk.CTkOptionMenu(frame, values=cities)
        city_box.place(relx=0.4, rely=0.3, anchor="w")

        job_type_label = ctk.CTkLabel(frame, text="Job Type", font=self.label_data_font)
        job_type_label.place(relx=0.35, rely=0.35, anchor="e")

        job_type_box = ctk.CTkOptionMenu(frame, values= professions, command=self.on_job_type_change)
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
        back_button = ctk.CTkButton(frame, text="Back", width=120, height=32, 
                                command=lambda: self.app.show_page(self.employer_main_dashboard))
        back_button.place(relx=0.4, rely=0.8, anchor="center")

        return frame

    def on_job_type_change(self, selected_job_type):
        if selected_job_type == "Other":
            self.other_job_entry.configure(state="normal")
        else:
            self.other_job_entry.delete(0, "end")
            self.other_job_entry.configure(state="disabled")

##########################################################################################################################################################
###################################################################################################################################################
    
    def available_labour_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        # Header
        heading = ctk.CTkLabel(frame, 
                            text="Available Labour", 
                            font=("Arial", 24))
        heading.place(relx=0.5, rely=0.03, anchor="center")
        
        # City Filter
        city_label = ctk.CTkLabel(frame, text="Filter by City", font=self.label_data_font)
        city_label.place(relx=0.3, rely=0.1, anchor="e")
        city_filter = ctk.CTkComboBox(frame, values=["All"] + ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Peshawar", "Multan", "Abbottabad", "Attock", "Bahawalpur", "Bannu", "Chakwal", "Chiniot", "Dera Ghazi Khan", "Ghotki", "Gujranwala", "Gujrat", "Hyderabad", "Jhang", "Jhelum", "Kasur", "Khuzdar", "Kotli", "Larkana", "Mardan", "Mingora", "Mirpur Khas", "Nawabshah", "Okara", "Rahim Yar Khan", "Sargodha", "Sheikhupura", "Sialkot", "Sukkur"])
        city_filter.place(relx=0.4, rely=0.1, anchor="w")
        
        # Scrollable Frame for Labour List
        scrollable_frame = ctk.CTkScrollableFrame(frame, width=900, height=500)
        scrollable_frame.place(relx=0.5, rely=0.2, anchor="n")
        
        # Labour List

        labour_list = [
            {"name": "Aslam Ahmed", "profession": "Electrician", "phone": "1234567890", "experience": "5 years", "dob": "1990-01-01", "city": "Lahore"},
            {"name": "Bilal Khan", "profession": "Plumber", "phone": "0987654321", "experience": "3 years", "dob": "1992-02-02", "city": "Karachi"},
            {"name": "Catherine Zeta", "profession": "Painter", "phone": "1122334455", "experience": "2 years", "dob": "1995-03-03", "city": "Islamabad"},
                        {"name": "Catherine Zeta", "profession": "Painter", "phone": "1122334455", "experience": "2 years", "dob": "1995-03-03", "city": "Islamabad"},
                        {"name": "Catherine Zeta", "profession": "Painter", "phone": "1122334455", "experience": "2 years", "dob": "1995-03-03", "city": "Islamabad"},
                        {"name": "Catherine Zeta", "profession": "Painter", "phone": "1122334455", "experience": "2 years", "dob": "1995-03-03", "city": "Islamabad"},
                        {"name": "Catherine Zeta", "profession": "Painter", "phone": "1122334455", "experience": "2 years", "dob": "1995-03-03", "city": "Islamabad"},
                        {"name": "Catherine Zeta", "profession": "Painter", "phone": "1122334455", "experience": "2 years", "dob": "1995-03-03", "city": "Islamabad"},
                        {"name": "Catherine Zeta", "profession": "Painter", "phone": "1122334455", "experience": "2 years", "dob": "1995-03-03", "city": "Islamabad"},
                        {"name": "Catherine Zeta", "profession": "Painter", "phone": "1122334455", "experience": "2 years", "dob": "1995-03-03", "city": "Islamabad"},
                        {"name": "Catherine Zeta", "profession": "Painter", "phone": "1122334455", "experience": "2 years", "dob": "1995-03-03", "city": "Islamabad"},
                        {"name": "Catherine Zeta", "profession": "Painter", "phone": "1122334455", "experience": "2 years", "dob": "1995-03-03", "city": "Islamabad"},
                        {"name": "Catherine Zeta", "profession": "Painter", "phone": "1122334455", "experience": "2 years", "dob": "1995-03-03", "city": "Islamabad"},  
            # Add more labour data as needed
        ]
        
        # Display Labour
        def display_labour(city):
            for widget in scrollable_frame.winfo_children():
                widget.destroy()
            
            filtered_labour_list = [labour for labour in labour_list if city == "All" or labour["city"] == city]
            
            for index, labour in enumerate(filtered_labour_list):
                labour_frame = ctk.CTkFrame(scrollable_frame, width=880, height=100, border_width=1, border_color="gray")
                labour_frame.pack(pady=10)
                
                labour_name = ctk.CTkLabel(labour_frame, text=f"Name: {labour['name']}", font=("Arial", 18))
                labour_name.place(relx=0.05, rely=0.2, anchor="w")
                
                labour_profession = ctk.CTkLabel(labour_frame, text=f"Profession: {labour['profession']}", font=("Arial", 14))
                labour_profession.place(relx=0.05, rely=0.5, anchor="w")
                
                labour_phone = ctk.CTkLabel(labour_frame, text=f"Phone: {labour['phone']}", font=("Arial", 14))
                labour_phone.place(relx=0.05, rely=0.8, anchor="w")
                
                labour_experience = ctk.CTkLabel(labour_frame, text=f"Experience: {labour['experience']}", font=("Arial", 12))
                labour_experience.place(relx=0.5, rely=0.5, anchor="center")
                
                labour_dob = ctk.CTkLabel(labour_frame, text=f"DOB: {labour['dob']}", font=("Arial", 12))
                labour_dob.place(relx=0.75, rely=0.5, anchor="center")
        
        city_filter.set("All")
        city_filter.bind("<<ComboboxSelected>>", lambda event: display_labour(city_filter.get()))
        
        display_labour("All")
        
        # Back Button
        back_button = ctk.CTkButton(frame, text="Back", width=120, height=32, command=lambda: self.app.show_page(self.app.select_language_page))
        back_button.place(relx=0.5, rely=0.9, anchor="center")
        
        return frame


###########################################################################################################################################################
############################################################################################################################################################


   
    
    

    


  
  


