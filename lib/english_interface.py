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
        heading.place(relx=0.5, rely=0.15, anchor="center")
        
        # Description
        description = ctk.CTkLabel(frame, 
                                text="Find the best jobs and make connections easily!", 
                                font=("Arial", 16))
        description.place(relx=0.5, rely=0.22, anchor="center")
        
        # Name field
        name_label = ctk.CTkLabel(frame, text="Full Name:", font=self.label_data_font)
        name_label.place(relx=0.35, rely=0.32, anchor="e")
        self.name_entry_box = ctk.CTkEntry(frame, width=250, height=35, 
                                          placeholder_text="Enter your full name")
        self.name_entry_box.place(relx=0.4, rely=0.32, anchor="w")

        # Email field
        email_label = ctk.CTkLabel(frame, text="Email:", font=self.label_data_font)
        email_label.place(relx=0.35, rely=0.42, anchor="e")
        self.email_entry = ctk.CTkEntry(frame, width=250, height=35,
                                       placeholder_text="Enter your email address") 
        self.email_entry.place(relx=0.4, rely=0.42, anchor="w")
        
        # Password field
        password_label = ctk.CTkLabel(frame, text="Password:", font=self.label_data_font)
        password_label.place(relx=0.35, rely=0.52, anchor="e")
        self.password_entry = ctk.CTkEntry(frame, width=250, height=35, show="*",
                                          placeholder_text="Enter your password")
        self.password_entry.place(relx=0.4, rely=0.52, anchor="w")
        
        # Confirm password field
        confirm_password_label = ctk.CTkLabel(frame, text="Confirm Password:", font=self.label_data_font)
        confirm_password_label.place(relx=0.35, rely=0.62, anchor="e")
        self.confirm_password_entry = ctk.CTkEntry(frame, width=250, height=35, show="*",
                                                 placeholder_text="Confirm your password")
        self.confirm_password_entry.place(relx=0.4, rely=0.62, anchor="w")

        # User type dropdown
        user_type_label = ctk.CTkLabel(frame, text="User Type:", font=self.label_data_font)
        user_type_label.place(relx=0.35, rely=0.72, anchor="e")
        self.user_type_box = ctk.CTkComboBox(frame, values=user_types, width=250, height=35)
        self.user_type_box.place(relx=0.4, rely=0.72, anchor="w")

        # Sign up button
        signup_button = ctk.CTkButton(frame, text="Sign Up", width=200, height=40, 
                                    command=lambda: self.run_create_user())
        signup_button.place(relx=0.5, rely=0.82, anchor="center")

        # Login link
        login_button = ctk.CTkButton(frame, text="Already have an account? Log In",
                                    command=lambda:self.app.show_page(self.login_page))
        login_button.place(relx=0.5, rely=0.89, anchor="center")

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

    def login_page(self):
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
            print(self.current_user)
            if(user_type=="Tradesperson"):
                self.app.show_page(self.labour_main_dashboard)
            else:
                self.app.show_page(self.employer_main_dashboard)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def logout(self):
            self.current_user=None
            self.current_user_type=None
            self.app.show_page(self.login_page)

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
       
        

        # Then use it in the button:
        back_button = ctk.CTkButton(frame, text="Back", width=200, height=40, 
                                command=self.navigate_dashboard)
        back_button.place(relx=0.5, rely=0.7, anchor="center")
        
        return frame
    
    def navigate_dashboard(self):
            if self.current_user_type == "Tradesperson":
                self.app.show_page(self.labour_main_dashboard)
            else:
                self.app.show_page(self.employer_main_dashboard)

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

        view_profile_button_labour = ctk.CTkButton(frame, text="View Profile", command=lambda:self.app.show_page(self.labour_profile_view_page))
        view_profile_button_labour.place(relx=0.5, rely=0.4, anchor="center")

        # Change password button
        change_password_button = ctk.CTkButton(frame, text="Change Password", command=lambda:self.app.show_page(self.change_password_page))
        change_password_button.place(relx=0.5, rely=0.5, anchor="center")

        # Logout Button
        logout_button = ctk.CTkButton(frame, text="Logout", command=self.logout)
        logout_button.place(relx=0.5, rely=0.6, anchor="center")
        
        return frame
    
###############################################################################################################################
###############################################################################################################################

    def labour_profile_view_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        # Header
        heading = ctk.CTkLabel(frame, 
                            text="Labourer Profile", 
                            font=("Arial", 24))
        heading.place(relx=0.5, rely=0.03, anchor="center")
        
        # Starting positions
        y_start = 0.15  # Match data entry page
        y_increment = 0.1

        cnic, profession, phone, experience, dob, city = self.database_view_profile_labour()
        
        # CNIC
        cnic_label = ctk.CTkLabel(frame, text="CNIC:", font=self.label_data_font)
        cnic_label.place(relx=0.35, rely=y_start, anchor="e")
        cnic_value = ctk.CTkLabel(frame, text=cnic, font=self.label_data_font)
        cnic_value.place(relx=0.4, rely=y_start, anchor="w")

        # Profession 
        profession_label = ctk.CTkLabel(frame, text="Profession:", font=self.label_data_font)
        profession_label.place(relx=0.35, rely=y_start + y_increment, anchor="e")
        profession_value = ctk.CTkLabel(frame, text=profession, font=self.label_data_font)
        profession_value.place(relx=0.4, rely=y_start + y_increment, anchor="w")

        # Date of Birth
        dob_label = ctk.CTkLabel(frame, text="Date of Birth:", font=self.label_data_font)
        dob_label.place(relx=0.35, rely=y_start + y_increment*2.5, anchor="e")
        dob_value = ctk.CTkLabel(frame, text=dob, font=self.label_data_font)
        dob_value.place(relx=0.4, rely=y_start + y_increment*2.5, anchor="w")

        # Phone
        phone_label = ctk.CTkLabel(frame, text="Phone:", font=self.label_data_font)
        phone_label.place(relx=0.35, rely=y_start + y_increment*3.5, anchor="e")
        phone_value = ctk.CTkLabel(frame, text=phone, font=self.label_data_font)
        phone_value.place(relx=0.4, rely=y_start + y_increment*3.5, anchor="w")

        # Experience
        experience_label = ctk.CTkLabel(frame, text="Years of Experience:", font=self.label_data_font) 
        experience_label.place(relx=0.35, rely=y_start + y_increment*4.5, anchor="e")
        experience_value = ctk.CTkLabel(frame, text=experience, font=self.label_data_font)
        experience_value.place(relx=0.4, rely=y_start + y_increment*4.5, anchor="w")

        # City
        city_label = ctk.CTkLabel(frame, text="City:", font=self.label_data_font)
        city_label.place(relx=0.35, rely=y_start + y_increment*5.5, anchor="e")
        city_value = ctk.CTkLabel(frame, text=city, font=self.label_data_font)
        city_value.place(relx=0.4, rely=y_start + y_increment*5.5, anchor="w")

        # Buttons
        edit_button = ctk.CTkButton(frame, text="Edit", command=lambda: self.app.show_page(self.labour_data_update_page), width=120, height=35)
        edit_button.place(relx=0.5, rely=y_start + y_increment*6.5, anchor="center")

        back_button = ctk.CTkButton(frame, text="Back", width=120, height=35,
                                   command=lambda: self.app.show_page(self.labour_main_dashboard))
        back_button.place(relx=0.35, rely=y_start + y_increment*6.5, anchor="center")
        
        return frame
    
    def database_view_profile_labour(self):
        dict = self.db.collection(self.current_user_type).document(self.current_user).get().to_dict()
        
        # Check if fields exist and are not None, otherwise return placeholder text
        cnic = dict.get("cnic", "Field not filled")
        profession = dict.get("profession", "Field not filled") 
        phone = dict.get("phone", "Field not filled")
        experience = dict.get("experience", "Field not filled")
        dob = dict.get("dob", "Field not filled")
        city = dict.get("city", "Field not filled")

        return cnic, profession, phone, experience, dob, city

##########################################################################################################################################
##########################################################################################################################################
    
    def labour_data_update_page(self):
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
        self.profession_box = ctk.CTkComboBox(frame, values=professions, width=250, height=35, command=self.on_profession_change)
        self.profession_box.place(relx=0.4, rely=y_start + y_increment, anchor="w")

        # Other Profession Entry
        self.other_profession_entry = ctk.CTkEntry(frame, placeholder_text="Please specify other profession", width=250, height=35)
        self.other_profession_entry.place(relx=0.4, rely=y_start + y_increment*1.5, anchor="w")
        self.other_profession_entry.configure(state="disabled")

        # Date of Birth
        dob_label = ctk.CTkLabel(frame, text="Date of Birth:", font=self.label_data_font)
        dob_label.place(relx=0.35, rely=y_start + y_increment*2.5, anchor="e")
        
        date_frame = ctk.CTkFrame(frame)
        date_frame.place(relx=0.4, rely=y_start + y_increment*2.5, anchor="w")
        
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
                self.calendar_frame.place(relx=0.7, rely=y_start + y_increment*2.5, anchor="w")
                self.cal = Calendar(self.calendar_frame, selectmode='day', date_pattern='dd/mm/yyyy')
                self.cal.pack()
                select_btn = ctk.CTkButton(self.calendar_frame, text="Select", command=get_date)
                select_btn.pack(pady=5)

        calendar_btn = ctk.CTkButton(date_frame, text="📅", width=30, height=35, command=toggle_calendar)
        calendar_btn.pack(side="left")

        # Phone
        phone_label = ctk.CTkLabel(frame, text="Phone:", font=self.label_data_font)
        phone_label.place(relx=0.35, rely=y_start + y_increment*3.5, anchor="e")
        self.phone_entry_box = ctk.CTkEntry(frame, width=250, height=35, placeholder_text="e.g 03001234567")
        self.phone_entry_box.place(relx=0.4, rely=y_start + y_increment*3.5, anchor="w")

        # Experience
        experience_label = ctk.CTkLabel(frame, text="Years of Experience:", font=self.label_data_font)
        experience_label.place(relx=0.35, rely=y_start + y_increment*4.5, anchor="e")
        self.experience_entry_box = ctk.CTkEntry(frame, width=250, height=35, placeholder_text="e.g 10")
        self.experience_entry_box.place(relx=0.4, rely=y_start + y_increment*4.5, anchor="w")

        # City
        city_label = ctk.CTkLabel(frame, text="City:", font=self.label_data_font)
        city_label.place(relx=0.35, rely=y_start + y_increment*5.5, anchor="e")
        self.city_box = ctk.CTkComboBox(frame, values=cities, width=250, height=35)
        self.city_box.place(relx=0.4, rely=y_start + y_increment*5.5, anchor="w")

        # Buttons
        submit_button = ctk.CTkButton(frame, text="Submit", command=self.labour_entry, width=120, height=35)
        submit_button.place(relx=0.5, rely=y_start + y_increment*6.5, anchor="center")

        back_button = ctk.CTkButton(frame, text="Back", width=120, height=35, 
                                   command=lambda: self.app.show_page(self.labour_main_dashboard))
        back_button.place(relx=0.35, rely=y_start + y_increment*6.5, anchor="center")

        return frame
    
    def on_profession_change(self, selected_profession):
        if selected_profession == "Other":
            self.other_profession_entry.configure(state="normal") 
        else:
            self.other_profession_entry.delete(0, "end")
            self.other_profession_entry.configure(state="disabled")
            
    def labour_database_entry(self,cnic,profession,phone,experience,dob,city):
        dict = self.db.collection(self.current_user_type).document(self.current_user).get().to_dict()
     
        dict['profession']= profession
        dict["phone"]= phone
        dict["experience"]= experience
        dict["dob"]= dob
        dict["city"]= city
        dict["cnic"]=cnic
        self.db.collection("City wise Tradesperson data").document(dict["city"]).collection(dict['profession']).document(self.current_user).set(
        {
            "name":dict["name"],
            "phone":dict["phone"],
            "experience":dict["experience"],
        }
        )
        self.db.collection(self.current_user_type).document(self.current_user).set(dict)
        # firebase_database.collection("city2").document("cname").collection("addresses").document("gfdg").set({
#   "street": "123 Main St",
#   "city": "Anytown",
#   "state": "CA",
#   "zip": "12345"
# });

    def labour_entry(self):
        cnic=self.cnic_entry_box.get()
        profession=self.profession_box.get()
        if profession == "Other":
            profession = self.other_profession_entry.get()
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
#docs=firebase_database.collection("City wise Job data").document("Karachi").collection("Carpenter").get()

# for doc in docs:
#   print(doc)  # Get document identifier
#   data = doc.to_dict()  # Get
#   print(data)
    def database_available_jobs_get(self,city,job_title):
        try:
            docs = self.db.collection("City wise Job data").document(city).collection(job_title).get()
            job_data_list = []
            
            if not docs:  # If no documents returned
                return [{"name": "No Data",
                        "phone": "N/A", 
                        "address": "N/A",
                        "description": "No jobs found",
                        "job price": "N/A"}]

            for doc in docs:
                data = doc.to_dict()
                if data:  # Check if document data exists
                    job_data_list.append(data)
                
            return job_data_list if job_data_list else [{"name": "No Data",
                                                        "phone": "N/A",
                                                        "address": "N/A", 
                                                        "description": "No jobs found",
                                                        "job price": "N/A"}]
        except:
            return [{"name": "No Data",
                    "phone": "N/A",
                    "address": "N/A",
                    "description": "Error retrieving jobs",
                    "job price": "N/A"}]

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
        self.job_city_filter = ctk.CTkComboBox(frame, values=cities, width=250)
        self.job_city_filter.place(relx=0.4, rely=0.1, anchor="w")

        # Profession Filter
        profession_label = ctk.CTkLabel(frame, text="Filter by Profession", font=self.label_data_font)
        profession_label.place(relx=0.3, rely=0.15, anchor="e")
        
        def on_job_filter_change(choice):
            if choice == "Other":
                self.other_job_type_filter.configure(state="normal")
            else:
                self.other_job_type_filter.delete(0, "end")
                self.other_job_type_filter.configure(state="disabled")
                
        self.job_profession_filter = ctk.CTkComboBox(frame, values=professions, width=250, command=on_job_filter_change)
        self.job_profession_filter.place(relx=0.4, rely=0.15, anchor="w")

        # Other Profession Entry
        self.other_job_type_filter = ctk.CTkEntry(frame, placeholder_text="Please specify other profession", width=250)
        self.other_job_type_filter.place(relx=0.4, rely=0.2, anchor="w")
        self.other_job_type_filter.configure(state="disabled")
        
        # Scrollable Frame for Job List
        scrollable_frame = ctk.CTkScrollableFrame(frame, width=900, height=400)
        scrollable_frame.place(relx=0.5, rely=0.25, anchor="n")
        
        def display_jobs():
            # Clear previous entries
            for widget in scrollable_frame.winfo_children():
                widget.destroy()
                
            city = self.job_city_filter.get()
            profession = self.job_profession_filter.get()
            if profession == "Other":
                profession = self.other_job_type_filter.get()
            
            # Get filtered job list from database
            job_list = self.database_available_jobs_get(city, profession)
            
            for job in job_list:
                # Create frame for each job entry
                job_frame = ctk.CTkFrame(scrollable_frame, width=880, height=100, border_width=1, border_color="gray")
                job_frame.pack(pady=10, fill="x", padx=5)
                
                # Configure frame to maintain size
                job_frame.pack_propagate(False)
                
                # Display job information
                name_label = ctk.CTkLabel(job_frame, text=f"Contact Name: {job['name']}", font=("Arial", 16))
                name_label.place(relx=0.05, rely=0.2, anchor="w")
                
                price_label = ctk.CTkLabel(job_frame, text=f"Job Price: Rs. {job['job price']}", font=("Arial", 14))
                price_label.place(relx=0.05, rely=0.5, anchor="w")
                
                phone_label = ctk.CTkLabel(job_frame, text=f"Phone: {job['phone']}", font=("Arial", 14))
                phone_label.place(relx=0.05, rely=0.8, anchor="w")
                
                address_label = ctk.CTkLabel(job_frame, text=f"Address: {job['address']}", font=("Arial", 14))
                address_label.place(relx=0.4, rely=0.3, anchor="w")
                
                description_label = ctk.CTkLabel(job_frame, text=f"Description: {job['description']}", font=("Arial", 14))
                description_label.place(relx=0.4, rely=0.7, anchor="w")

        # Add search button
        search_button = ctk.CTkButton(frame, text="Search", width=120, height=32, 
                                    command=display_jobs)
        search_button.place(relx=0.7, rely=0.15, anchor="center")
        
        # Back Button
        back_button = ctk.CTkButton(frame, text="Back", width=120, height=32, command=lambda: self.app.show_page(self.labour_main_dashboard))
        back_button.place(relx=0.5, rely=0.9, anchor="center")
        
        return frame
########################################################################################################################################################
########################################################################################################################################################

##########################################################################################################################################################
#####################################################################################################################################################
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
        available_labour_button_dashboard = ctk.CTkButton(frame, text="Available Tradespersons", width=200, height=40,command=lambda: self.app.show_page(self.available_labour_page))
        available_labour_button_dashboard.place(relx=0.5, rely=0.2, anchor="center")
        
        # Create Job Posting Button
        create_job_button = ctk.CTkButton(frame, text="Create Job Posting", width=200, height=40, 
                                        command=lambda: self.app.show_page(self.job_submission_page))
        create_job_button.place(relx=0.5, rely=0.4, anchor="center")
        
        # Change Password Button
        change_password_button = ctk.CTkButton(frame, text="Change Password", width=200, height=40,
                                             command=lambda: self.app.show_page(self.change_password_page))
        change_password_button.place(relx=0.5, rely=0.5, anchor="center")
        
        # Profile Button
        profile_button = ctk.CTkButton(frame, text="Profile", width=200, height=40, command=lambda: self.app.show_page(self.employer_profile_view_page))
        profile_button.place(relx=0.5, rely=0.6, anchor="center")
        
        # Logout Button
        logout_button = ctk.CTkButton(frame, text="Logout", width=200, height=40, 
                                    command=lambda: self.logout())
        logout_button.place(relx=0.5, rely=0.7, anchor="center")
        
        return frame
   
####################################################################################################################
#############################################################################################################################  
    def database_view_profile_employer(self):
        dict = self.db.collection(self.current_user_type).document(self.current_user).get().to_dict()
        print(dict)
        print(type(dict))

        # Check if fields exist and are not None, otherwise return placeholder text
        phone = dict.get("phone", None) 
        address = dict.get("address", None)
        city = dict.get("city", None)

        if phone is None:
            phone = "Field not filled. Please update your profile"
        if address is None:    
            address = "Field not filled. Please update your profile"
        if city is None:
            city = "Field not filled. Please update your profile"

        return phone, address, city
         
    def employer_profile_view_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        # Header
        heading = ctk.CTkLabel(frame, 
                    text="Employer Profile", 
                    font=("Arial", 24))
        heading.place(relx=0.5, rely=0.03, anchor="center")
        # Starting positions
        y_start = 0.2
        y_increment = 0.1

        phone,address,city=self.database_view_profile_employer()
        # Phone
        phone_label = ctk.CTkLabel(frame, text="Phone", font=self.label_data_font)
        phone_label.place(relx=0.4, rely=y_start, anchor="e")
        phone_entry = ctk.CTkEntry(frame, width=300, height=30)
        phone_entry.insert(0,phone)
        phone_entry.configure(state="disabled")
        phone_entry.place(relx=0.6, rely=y_start, anchor="w")
        
        # Address
        address_label = ctk.CTkLabel(frame, text="Address", font=self.label_data_font)
        address_label.place(relx=0.4, rely=y_start + y_increment, anchor="e")
        address_entry = ctk.CTkEntry(frame, width=300, height=30)
        address_entry.insert(0,address)
        address_entry.configure(state="disabled")
        address_entry.place(relx=0.6, rely=y_start + y_increment, anchor="w")
        
        # City 
        city_label = ctk.CTkLabel(frame, text="City", font=self.label_data_font)
        city_label.place(relx=0.4, rely=y_start + y_increment*2, anchor="e")
        city_entry = ctk.CTkEntry(frame, width=300, height=30)
        city_entry.insert(0,city)
        city_entry.configure(state="disabled")
        city_entry.place(relx=0.6, rely=y_start + y_increment*2, anchor="w")

        edit_button = ctk.CTkButton(frame, text="Edit", width=120, height=35,
                        command=lambda: self.app.show_page(self.employer_profile_update_page))
        edit_button.place(relx=0.5, rely=0.8, anchor="center")

        back_button = ctk.CTkButton(frame, text="Back", width=120, height=35,command=lambda: self.app.show_page(self.employer_main_dashboard))
        back_button.place(relx=0.3, rely=0.8, anchor="center")

        return frame
#############################################################################################################################
########################################################################################################################################

    def employer_profile_update_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        # Header
        heading = ctk.CTkLabel(frame, 
                            text="Employer Profile", 
                            font=("Arial", 24))
        heading.place(relx=0.5, rely=0.03, anchor="center")
        # Starting positions
        y_start = 0.2
        y_increment = 0.1

        # Phone
        phone_label = ctk.CTkLabel(frame, text="Phone", font=self.label_data_font)
        phone_label.place(relx=0.4, rely=y_start, anchor="e")
        self.phone_entry_employer = ctk.CTkEntry(frame, width=300, height=30)
        self.phone_entry_employer.place(relx=0.6, rely=y_start, anchor="w")
        
        # Address
        address_label = ctk.CTkLabel(frame, text="Address", font=self.label_data_font)
        address_label.place(relx=0.4, rely=y_start + y_increment, anchor="e")
        self.address_entry_employer = ctk.CTkEntry(frame, width=300, height=30)
        self.address_entry_employer.place(relx=0.6, rely=y_start + y_increment, anchor="w")
        
        # City 
        city_label = ctk.CTkLabel(frame, text="City", font=self.label_data_font)
        city_label.place(relx=0.4, rely=y_start + y_increment*2, anchor="e")
        self.city_box_employer = ctk.CTkComboBox(frame, values=cities, width=300, height=30)
        self.city_box_employer.place(relx=0.6, rely=y_start + y_increment*2, anchor="w")

        update_button = ctk.CTkButton(frame, text="Update", width=120, height=35,command=self.employer_profile_entry)
        update_button.place(relx=0.5, rely=0.8, anchor="center")

        back_button = ctk.CTkButton(frame, text="Back", width=120, height=35,command=lambda: self.app.show_page(self.employer_profile_view_page))
        back_button.place(relx=0.3, rely=0.8, anchor="center")
    
        return frame
 
    def employer_profile_database_entry(self,phone,address,city):
        dict = self.db.collection(self.current_user_type).document(self.current_user).get().to_dict()
        dict['phone']= phone
        dict["address"]= address
        dict["city"]= city
        self.db.collection(self.current_user_type).document(self.current_user).set(dict)

    def employer_profile_entry(self):
        phone=self.phone_entry_employer.get()
        address=self.address_entry_employer.get()
        city=self.city_box_employer.get()

        if(is_empty(phone) or is_empty(address) or is_empty(city)):
            messagebox.showerror("Error","Please fill out all fields")
            return
        else:
            if (is_invalid_phone(phone)):
                messagebox.showerror("Input Error","Please enter a valid phone number")
                return
            self.employer_profile_database_entry(phone,address,city)
            self.app.show_page(self.employer_profile_view_page)
#####################################################################################################################################
####################################################################################################################################    
    
    def job_submission_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)

        # Header
        heading = ctk.CTkLabel(frame, text="Job Submission", font=self.heading_label_font)
        heading.place(relx=0.5, rely=0.05, anchor="center")

        # Starting vertical position and spacing
        y_start = 0.2
        y_increment = 0.1

        # City Selection
        city_label = ctk.CTkLabel(frame, text="City:", font=self.label_data_font)
        city_label.place(relx=0.35, rely=y_start, anchor="e")
        self.city_box_job_sub = ctk.CTkOptionMenu(frame, values=cities, width=250)
        self.city_box_job_sub.place(relx=0.4, rely=y_start, anchor="w")

        # Job Type Selection
        job_type_label = ctk.CTkLabel(frame, text="Job Type:", font=self.label_data_font)
        job_type_label.place(relx=0.35, rely=y_start + y_increment, anchor="e")
        self.job_type_box_sub = ctk.CTkOptionMenu(frame, values=professions, width=250, command=self.on_job_type_change)
        self.job_type_box_sub.place(relx=0.4, rely=y_start + y_increment, anchor="w")

        # Other Job Type Entry
        self.other_job_entry = ctk.CTkEntry(frame, placeholder_text="Please specify other job type", width=250)
        self.other_job_entry.place(relx=0.4, rely=y_start + y_increment*2, anchor="w")
        self.other_job_entry.configure(state="disabled")

        # User Name Entry
        job_price_label = ctk.CTkLabel(frame, text="Job Wage:", font=self.label_data_font)
        job_price_label.place(relx=0.35, rely=y_start + y_increment*3, anchor="e")
        self.job_price_entry = ctk.CTkEntry(frame, placeholder_text="e.g 1000", width=250)
        self.job_price_entry.place(relx=0.4, rely=y_start + y_increment*3, anchor="w")

        # Job Description
        job_description_label = ctk.CTkLabel(frame, text="Job Description:", font=self.label_data_font)
        job_description_label.place(relx=0.35, rely=y_start + y_increment*4, anchor="e")
        self.job_description_entry = ctk.CTkTextbox(frame, width=400, height=150)
        self.job_description_entry.place(relx=0.4, rely=y_start + y_increment*4.5, anchor="w")
        
        # Add placeholder text
        self.job_description_entry.insert("0.0", "Enter detailed job description here...")
        self.job_description_entry.configure(text_color="gray")
        
        def on_focus_in(event):
            if self.job_description_entry.get("0.0", "end-1c") == "Enter detailed job description here...":
                self.job_description_entry.delete("0.0", "end")
                self.job_description_entry.configure(text_color="white")
            
        def on_focus_out(event):
            if self.job_description_entry.get("0.0", "end-1c").strip() == "":
                self.job_description_entry.insert("0.0", "Enter detailed job description here...")
                self.job_description_entry.configure(text_color="gray")
            
        self.job_description_entry.bind("<FocusIn>", on_focus_in)
        self.job_description_entry.bind("<FocusOut>", on_focus_out)

        # Buttons at the bottom
        back_button = ctk.CTkButton(frame, text="Back", width=120, height=35,
                                   command=lambda: self.app.show_page(self.employer_main_dashboard))
        back_button.place(relx=0.4, rely=0.9, anchor="center")

        submit_button = ctk.CTkButton(frame, text="Submit", width=120, height=35,
                                     command=self.job_submission)
        submit_button.place(relx=0.6, rely=0.9, anchor="center")

        return frame

    def on_job_type_change(self, selected_job_type):
        if selected_job_type == "Other":
            self.other_job_entry.configure(state="normal")
        else:
            self.other_job_entry.delete(0, "end")
            self.other_job_entry.configure(state="disabled")

 
    def job_database_entry(self,city,job_type,price,job_description):
        doc_ref = self.db.collection("City wise Job data").document(city).collection(job_type).document()
        unique_id = doc_ref.id
        print(unique_id)

        employer_data = self.db.collection(self.current_user_type).document(self.current_user).get().to_dict()
        if not employer_data.get("posted job ids"):
            employer_data["posted job ids"]=[unique_id]
        else:
            employer_data["posted job ids"].append(unique_id)
        self.db.collection(self.current_user_type).document(self.current_user).set(employer_data)

        self.db.collection("Job ids").document(unique_id).set({
            "city": city,
            "job type": job_type,
        })

        doc_ref.set({
            "name": employer_data["name"],
            "phone": employer_data["phone"],
            "address": employer_data["address"],
            "description": job_description,
            "job price": price,
               # Store ID in document itself
        })

    def job_submission(self):
        city = self.city_box_job_sub.get()
        job_type = self.job_type_box_sub.get()
        if job_type == "Other":
            job_type = self.other_job_entry.get()
        price = self.job_price_entry.get()
        job_description = self.job_description_entry.get("0.0", "end-1c")

        if(is_empty(price) or is_empty(job_description)):
            messagebox.showerror("Error","Please fill out all fields")
            return
        else:
            self.job_database_entry(city,job_type,price,job_description)
            self.app.show_page(self.employer_main_dashboard)

##########################################################################################################################################################
##########################################################################################################################################################

    def available_labour_database_get(self,city,profession):
        try:
            data = self.db.collection("City wise Tradesperson data").document(city).collection(profession).get()
            labour_list = list()
            
            if not data:  # If no data is returned
                return [{"name": "No Data", 
                        "experience": "No workers found", 
                        "phone": "N/A",
                        "email": "No results based on current filters"}]
                
            for doc in data:
                dict = doc.to_dict()
                dict["email"] = doc.id
                print(dict)
                labour_list.append(dict)
                
            return labour_list if labour_list else [{"name": "No Data", 
                                                   "experience": "No workers found",
                                                   "phone": "N/A", 
                                                   "email": "No results based on current filters"}]
        except:
            return [{"name": "No Data",
                    "experience": "No workers found",
                    "phone": "N/A",
                    "email": "No results based on current filters"}]


    def available_labour_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        # Header
        heading = ctk.CTkLabel(frame, 
                            text="Available Labour", 
                            font=("Arial", 24))
        heading.place(relx=0.5, rely=0.03, anchor="center")
        
        # City Filter
        available_labour_city_label = ctk.CTkLabel(frame, text="Filter by City", font=self.label_data_font)
        available_labour_city_label.place(relx=0.3, rely=0.1, anchor="e")
        self.available_labour_city_filter = ctk.CTkComboBox(frame, values=cities, width=250)
        self.available_labour_city_filter.place(relx=0.4, rely=0.1, anchor="w")

        # Profession Filter
        available_labour_profession_label = ctk.CTkLabel(frame, text="Filter by Profession", font=self.label_data_font)
        available_labour_profession_label.place(relx=0.3, rely=0.15, anchor="e")
        self.available_labour_profession_filter = ctk.CTkComboBox(frame, values=professions, width=250, command=self.on_profession_change)
        self.available_labour_profession_filter.place(relx=0.4, rely=0.15, anchor="w")
        # Other Profession Entry
        self.other_profession_filter = ctk.CTkEntry(frame, placeholder_text="Please specify other profession", width=250)
        self.other_profession_filter.place(relx=0.4, rely=0.2, anchor="w")
        self.other_profession_filter.configure(state="disabled")
        
        # Scrollable Frame for Labour List
        scrollable_frame = ctk.CTkScrollableFrame(frame, width=900, height=400)
        scrollable_frame.place(relx=0.5, rely=0.25, anchor="n")
        
        def display_labour():
            # Clear previous entries
            for widget in scrollable_frame.winfo_children():
                widget.destroy()
                
            city = self.available_labour_city_filter.get()
            profession = self.available_labour_profession_filter.get()
            
            # Get filtered labour list from database
            labour_list = self.available_labour_database_get(city, profession)
            
            for labour in labour_list:
                # Create frame for each labour entry
                labour_frame = ctk.CTkFrame(scrollable_frame, width=880, height=100, border_width=1, border_color="gray")
                labour_frame.pack(pady=10, fill="x", padx=5)
                
                # Configure frame to maintain size
                labour_frame.pack_propagate(False)
                
                # Display labour information
                name_label = ctk.CTkLabel(labour_frame, text=f"Name: {labour['name']}", font=("Arial", 16))
                name_label.place(relx=0.05, rely=0.2, anchor="w")
                
                experience_label = ctk.CTkLabel(labour_frame, text=f"Experience: {labour['experience']} years", font=("Arial", 14))
                experience_label.place(relx=0.05, rely=0.5, anchor="w")
                
                phone_label = ctk.CTkLabel(labour_frame, text=f"Phone: {labour['phone']}", font=("Arial", 14))
                phone_label.place(relx=0.05, rely=0.8, anchor="w")
                
                email_label = ctk.CTkLabel(labour_frame, text=f"Email: {labour['email']}", font=("Arial", 14))
                email_label.place(relx=0.5, rely=0.5, anchor="center")

        # Add search button
        search_button = ctk.CTkButton(frame, text="Search", width=120, height=32, 
                                    command=display_labour)
        search_button.place(relx=0.7, rely=0.15, anchor="center")
        
        # Back Button
        back_button = ctk.CTkButton(frame, text="Back", width=120, height=32, 
                                   command=lambda: self.app.show_page(self.employer_main_dashboard))
        back_button.place(relx=0.5, rely=0.9, anchor="center")
        
        return frame
    
    def on_profession_change(self, selected_profession):
        if selected_profession == "Other":
            self.other_profession_filter.configure(state="normal")
        else:
            self.other_profession_filter.delete(0, "end") 
            self.other_profession_filter.configure(state="disabled")