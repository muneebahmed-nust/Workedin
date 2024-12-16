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
   
       
        firebase_database.collection(user_type).document(email).set({
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
                self.app.show_page(self.labour_data_entry_page)

        

    def login_screen(self):
        # Create a frame for the login screen
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.place(relwidth=1, relheight=1)

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
        print(pass_checker)
        if password==pass_checker["password"]:
            self.current_user=username
            if(user_type=="Tradesperson"):
                self.app.show_page(self.labour_data_entry_page)
            else:
                self.app.show_page(self.job_submission_page)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
      
        
   
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
        profession_label.place(relx=0.4, rely=0.20, anchor="e")
        self.profession_box = ctk.CTkComboBox(frame, values=professions)
        self.profession_box.place(relx=0.6, rely=0.20, anchor="w")

        phone_label=ctk.CTkLabel(frame,text="Phone:",font=self.label_data_font,)
        phone_label.place(relx=0.4, rely=0.43, anchor="e")
        self.phone_entry_box=ctk.CTkEntry(frame,width=200,height=30,placeholder_text="e.g 03001234567")
        self.phone_entry_box.place(relx=0.6, rely=0.43, anchor="w")

        experience_label=ctk.CTkLabel(frame,text="Number of years of experience:",font=self.label_data_font)
        experience_label.place(relx=0.4, rely=0.57, anchor="e")
        self.experience_entry_box=ctk.CTkEntry(frame,width=200,height=30,placeholder_text="e.g 10")
        self.experience_entry_box.place(relx=0.6, rely=0.57, anchor="w")

        dob_label = ctk.CTkLabel(frame, text="Date of Birth:", font=self.label_data_font)
        dob_label.place(relx=0.4, rely=0.3, anchor="e")
        
        # Create date frame
        date_frame = ctk.CTkFrame(frame)
        date_frame.place(relx=0.6, rely=0.3, anchor="w")

        # Create entry and button
        self.dob_entry_box = ctk.CTkEntry(date_frame, width=170, height=30)
        self.dob_entry_box.pack(side="left", padx=(0,5))
        
        # Calendar frame will be created/destroyed on toggle
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
                self.calendar_frame.place(relx=0.75, rely=0.3, anchor="w")
                self.cal = Calendar(self.calendar_frame, selectmode='day', date_pattern='dd/mm/yyyy')
                self.cal.pack()
                select_btn = ctk.CTkButton(self.calendar_frame, text="Select", command=get_date)
                select_btn.pack()

        calendar_btn = ctk.CTkButton(date_frame, text="📅", width=25, height=30, command=toggle_calendar)
        calendar_btn.pack(side="left")

        city_label = ctk.CTkLabel(frame, text="City:", font=self.label_data_font)
        city_label.place(relx=0.4, rely=0.7, anchor="e")
        self.city_box = ctk.CTkComboBox(frame, values=cities)
        self.city_box.place(relx=0.6, rely=0.7, anchor="w")
       
        submit_button=ctk.CTkButton(frame,text="Submit",command=lambda:self.app.show_page(self.job_submission_page))
        submit_button.place(relx=0.4, rely=0.75, anchor="center")
       
        return frame
    
    async def labour_database_entry(self,cnic,profession,phone,experience,dob,city):
        await self.db.collection("labour").document(self.current_user).set({
            "profession": profession,
            "phone": phone,
            "experience": experience,
            "dob": dob,
            "city": city,
            "cnic":cnic,
            
        })
        print(self.current_user)

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

            self.labour_database_entry(cnic,profession,phone,experience,dob,city)

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

        return frame

    def on_job_type_change(self, selected_job_type):
        if selected_job_type == "Other":
            self.other_job_entry.configure(state="normal")
        else:
            self.other_job_entry.delete(0, "end")
            self.other_job_entry.configure(state="disabled")
   
    def view_jobs(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.place(relwidth=1, relheight=1)
        """Display available jobs based on selected skill and location"""
        self.title_label = ctk.CTkLabel(frame, text="Available Jobs", font=self.heading_label_font)
        self.title_label.pack(pady=20)

        if self.skill and self.location:
            jobs_text = f"Available jobs for {self.skill} in {self.location}:"
            jobs_text += "\n\n1. Job 1 - Details\n2. Job 2 - Details\n3. Job 3 - Details"
        else:
            jobs_text = "No job available. Please select a skill and location."

        self.jobs_label = ctk.CTkLabel(self.root, text=jobs_text, font=self.data_label_font)
        self.jobs_label.pack(pady=20)
    
   
    def create_labor_main_screen(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.place(relwidth=1, relheight=1)
        """Main screen where laborer can search for jobs."""
 

        # Main screen title
        self.title_label = ctk.CTkLabel(frame, text="Laborer Dashboard", font=self.heading_label_font)
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        # Buttons for searching jobs
        search_jobs_button = ctk.CTkButton(frame, text="Search Jobs", command=self.create_search_jobs_screen)
        search_jobs_button.place(relx=0.5, rely=0.3, anchor="center")

    def create_search_jobs_screen(self):
        """Screen where laborer can search for jobs."""
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.place(relwidth=1, relheight=1)


        # Clear the screen
        for widget in frame.winfo_children():
            widget.destroy()

        # Search Jobs Title
        self.title_label = ctk.CTkLabel(frame, text="Search Jobs", font=self.heading_label_font)
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        # Select Skill
        self.skill_label = ctk.CTkLabel(self.root, text="Select Skill", font=self.heading_label_font)
        self.skill_label.place(relx=0.5, rely=0.2, anchor="center")

        self.skills = ["Driver", "Labour", "Electrician", "Plumber", "Mason",
            "Carpenter", "Painter", "Cleaner", "Cook", "Security Guard", "Other"]
        self.skill_dropdown = ctk.CTkOptionMenu(self.root, values=self.skills)
        self.skill_dropdown.place(relx=0.5, rely=0.25, anchor="center")

        # Select Location
        self.location_label = ctk.CTkLabel(frame, text="Select Location", font=self.heading_label_font)
        self.location_label.place(relx=0.5, rely=0.35, anchor="center")

        self.locations = ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Peshawar", "Multan"  "Abbottabad", "Attock", "Bahawalpur", "Bannu", "Chakwal","Chiniot", "Dera Ghazi Khan", "Ghotki", "Gujranwala", "Gujrat", "Hyderabad", "Jhang", "Jhelum", "Kasur", "Khuzdar", "Kotli", "Larkana", "Mardan", "Mingora", "Mirpur Khas", "Nawabshah", 
        "Okara", "Rahim Yar Khan", "Sargodha", "Sheikhupura", "Sialkot", "Sukkur"]
        self.location_dropdown = ctk.CTkOptionMenu(frame, values=self.locations)
        self.location_dropdown.place(relx=0.5, rely=0.4, anchor="center")

        # Search Button
        search_button = ctk.CTkButton(frame, text="Search Jobs", command=self.search_jobs)
        search_button.place(relx=0.5, rely=0.5, anchor="center")

    def search_jobs(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.place(relwidth=1, relheight=1)
        """Search for jobs based on selected skill and location."""
        skill = self.skill_dropdown.get()
        location = self.location_dropdown.get()

        # Here you would perform a database search or display mock job listings (for demo purposes)
        print(f"Searching jobs: {skill}, {location}")

        # Display results (for demo purposes)
        search_results_label = ctk.CTkLabel(frame, text=f"Jobs available for {skill} in {location}", font=self.heading_label_font)
        search_results_label.place(relx=0.5, rely=0.6, anchor="center")

        # Sample job listings (for demo purposes)
        job_listings = [
            f"Job 1: {skill} required in {location}",
            f"Job 2: {skill} required in {location}",
            f"Job 3: {skill} required in {location}",
        ]
        for i, job in enumerate(job_listings):
            job_label = ctk.CTkLabel(frame, text=job, font=self.heading_label_font)
            job_label.place(relx=0.5, rely=0.7 + (i * 0.05), anchor="center")

    def open_skill_selection_page(self):
     frame = ctk.CTkFrame(self.root, width=1000, height=600)
     frame.place(relwidth=1, relheight=1)
    # Check if all fields are filled before navigating
     if (self.cnic_entry_box.get() and self.profession_box.get() and 
        self.phone_entry_box.get() and self.experience_entry_box.get() and 
        self.city_box.get()):
        self.create_skill_selection_screen()  # Transition to skill selection page
     else:
        error_label = ctk.CTkLabel(frame, text="Please fill in all fields", text_color="red")
        error_label.place(relx=0.5, rely=0.8, anchor="center")     # If data is invalid, show an error message


    def create_skill_selection_screen(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.place(relwidth=1, relheight=1)
        # Create the skill selection page title
        self.title_label = ctk.CTkLabel(frame, text="Select Your Skill", font=self.heading_label_font)
        self.title_label.pack(pady=10)

        # Load images for each profession
        self.image_paths = {
            "Carpenter": "./resources/carpenter.png",
            "Electrician": "./resources/electrician.png",
            "Plumber": "./resources/plumber.png",
            "Painter": "./resources/painter.png",
            "Mason": "./resources/mason.png",
            "Driver": "./resources/driver.png",
            "Cook": "./resources/cook.png",
            "Labor": "./resources/labour.png",
            "Security Guard": "./resources/security_guard.png"
        }

        # Scrollable frame for skills
        self.skills_frame = ctk.CTkScrollableFrame(frame, width=700, height=600)
        self.skills_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Add skills using grid layout
        self.add_skill_buttons()


    def add_skill_buttons(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.place(relwidth=1, relheight=1)
        row, col = 0, 0  # Initial grid position
        for skill, path in self.image_paths.items():
            try:
                # Load and resize the image
                image = ctk.CTkImage(light_image=Image.open(path), size=(300, 200))

                # Create an image label
                image_label = ctk.CTkLabel(frame.skills_frame, text="", image=image)
                image_label.grid(row=row, column=col, padx=20, pady=10)

                # Create a button below the image
                button = ctk.CTkButton(frame.skills_frame, text=f"Select {skill}", command=lambda s=skill: self.on_skill_selected(s))
                button.grid(row=row + 1, column=col, padx=20, pady=5)

                # Update grid position
                col += 1
                if col > 2:  # 3 columns per row
                    col = 0
                    row += 2  # Move to the next set of rows

            except Exception as e:
                print(f"Error loading image for {skill}: {e}")


    def on_skill_selected(self, skill_name):
        """Handle the skill selection"""
        self.skill = skill_name
        print(f"Selected skill: {self.skill}")

        # Clear the current screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Transition to location selection screen
        self.create_location_selection_screen()


    def create_location_selection_screen(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.place(relwidth=1, relheight=1)
        """Create the location selection screen with images and buttons."""
        # Load images for locations
        self.image_paths = {
            "Karachi": "./resources/karachi.png",
            "Lahore": "./resources/lahore.png",
            "Islamabad": "./resources/islamabad.png",
            "Faisalabad": "./resources/faisalabad.png",
            "Peshawar": "./resources/peshawar.png",
            "Multan": "./resources/multan.png",
            "Rawalpindi": "./resources/rawalpindi.png",
            "Quetta": "./resources/quetta.png",
            "Sialkot": "./resources/sialkot.png",
        }

        # Cities for dropdown menu
        self.dropdown_cities = [
            "Abbottabad", "Attock", "Bahawalpur", "Bannu", "Chakwal",
            "Chiniot", "Dera Ghazi Khan", "Ghotki", "Gujranwala", "Gujrat", 
            "Hyderabad", "Jhang", "Jhelum", "Kasur", "Khuzdar", "Kotli", 
            "Larkana", "Mardan", "Mingora", "Mirpur Khas", "Nawabshah", 
            "Okara", "Rahim Yar Khan", "Sargodha", "Sheikhupura", "Sialkot", "Sukkur"
        ]

        # Create the location selection page title
        self.title_label = ctk.CTkLabel(frame, text="Select location", font=self.heading_label_font)
        self.title_label.pack(pady=10)

        # Dropdown menu for selecting location
        self.selected_location = ctk.StringVar(value="Select a city")
        self.location_dropdown = ctk.CTkOptionMenu(frame, variable=self.selected_location, values=self.dropdown_cities)
        self.location_dropdown.pack(pady=10)

        # Bind the command to be called when a selection is made
        self.location_dropdown.configure(command=self.on_location_selected)

        # Scrollable frame for locations with images
        self.location_frame = ctk.CTkScrollableFrame(frame, width=700, height=600)
        self.location_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Add location buttons using grid layout for cities with images
        self.add_location_buttons()


    def add_location_buttons(self):
        row, col = 0, 0  # Initial grid position
        for location, path in self.image_paths.items():
            try:
                # Load and resize the image
                image = ctk.CTkImage(light_image=Image.open(path), size=(300, 200))

                # Create an image label
                image_label = ctk.CTkLabel(self.location_frame, text="", image=image)
                image_label.grid(row=row, column=col, padx=20, pady=10)

                # Create a button below the image
                button = ctk.CTkButton(self.location_frame, text=f"Select {location}", command=lambda l=location: self.on_location_selected(l))
                button.grid(row=row + 1, column=col, padx=20, pady=5)

                # Update grid position
                col += 1
                if col > 2:  # 3 columns per row
                    col = 0
                    row += 2  # Move to the next set of rows

            except Exception as e:
                print(f"Error loading image for {location}: {e}")


    def on_location_selected(self, location_name):
        """Handle the location selection"""
        self.location = location_name
        print(f"Selected location: {self.location}")

        # Clear the screen before showing jobs
        for widget in self.root.winfo_children():
            widget.destroy()

        # Transition to the jobs screen
        self.create_labor_main_screen()


    def create_employer_main_screen(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.place(relwidth=1, relheight=1)
        """Display job listings based on selected skill and location"""
        self.jobs_button = ctk.CTkButton(frame, text="View Jobs", command=self.view_jobs)
        self.jobs_button.pack(pady=20)

