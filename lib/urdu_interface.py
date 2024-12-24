import customtkinter as ctk
from tkinter import messagebox 
import utils  
from lib.backend_functions import *
from lib.authentication_firebase import *
from firebase_admin import auth
from tkcalendar import Calendar
from lib.data_resource import *
from PIL import Image

class UrduInterface:
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
                            text="ورکڈن: روزگار کو آسان بنائیں", 
                            font=("Arial", 24))
        heading.place(relx=0.5, rely=0.15, anchor="center")
        
        # Description
        description = ctk.CTkLabel(frame, 
                                text="! بہترین نوکریاں تلاش کریں اور آسانی سے روابط قائم کریں ", 
                                font=("Arial", 16))
        description.place(relx=0.5, rely=0.22, anchor="center")
        
        # Name field
        name_label = ctk.CTkLabel(frame, text=":پورا نام", font=self.label_data_font)
        name_label.place(relx=0.35, rely=0.32, anchor="e")
        self.name_entry_box = ctk.CTkEntry(frame, width=250, height=35, 
                                          placeholder_text="اپنا پورا نام درج کریں")
        self.name_entry_box.place(relx=0.4, rely=0.32, anchor="w")

        # Email field
        email_label = ctk.CTkLabel(frame, text=":ای میل", font=self.label_data_font)
        email_label.place(relx=0.35, rely=0.42, anchor="e")
        self.email_entry = ctk.CTkEntry(frame, width=250, height=35,
                                       placeholder_text="اپنا ای میل ایڈریس درج کریں ") 
        self.email_entry.place(relx=0.4, rely=0.42, anchor="w")
        
        # Password field
        password_label = ctk.CTkLabel(frame, text=":پاس ورڈ", font=self.label_data_font)
        password_label.place(relx=0.35, rely=0.52, anchor="e")
        self.password_entry = ctk.CTkEntry(frame, width=250, height=35, show="*",
                                          placeholder_text="اپنا پاس ورڈ درج کریں ")
        self.password_entry.place(relx=0.4, rely=0.52, anchor="w")
        
        # Confirm password field
        confirm_password_label = ctk.CTkLabel(frame, text=":پاس ورڈ کی تصدیق", font=self.label_data_font)
        confirm_password_label.place(relx=0.35, rely=0.62, anchor="e")
        self.confirm_password_entry = ctk.CTkEntry(frame, width=250, height=35, show="*",
                                                 placeholder_text="اپنا پاس ورڈ تصدیق کریں ")
        self.confirm_password_entry.place(relx=0.4, rely=0.62, anchor="w")

        # User type dropdown
        user_type_label = ctk.CTkLabel(frame, text=":صارف کی قسم", font=self.label_data_font)
        user_type_label.place(relx=0.35, rely=0.72, anchor="e")
        self.user_type_box = ctk.CTkComboBox(frame, values=user_types, width=250, height=35)
        self.user_type_box.place(relx=0.4, rely=0.72, anchor="w")

        # Sign up button
        signup_button = ctk.CTkButton(frame, text="سائن اپ", width=200, height=40, 
                                    command=lambda: self.create_user())
        signup_button.place(relx=0.5, rely=0.82, anchor="center")

        # Login link
        login_button = ctk.CTkButton(frame, text="کیا آپ کا پہلے سے اکاؤنٹ ہے؟ لاگ ان کریں",
                                    command=lambda:self.app.show_page(self.login_page))
        login_button.place(relx=0.5, rely=0.89, anchor="center")

        return frame
    
    def handle_signup(self, email, password, user_type, name):
     
        self.db.collection(user_type).document(email).set({
                "name": name, 
                "password":password,
            })
        
    
        
    # def create_user(self):
    #     email=self.email_entry.get()
    #     password=self.password_entry.get()
    #     confirm_password=self.confirm_password_entry.get()
    #     user_type=self.user_type_box.get()
    #     name=self.name_entry_box.get()

        
    #     if(is_empty(email) or is_empty(password) or is_empty(confirm_password) or is_empty( user_type)  or is_empty(name)):
    #         messagebox.showerror("ان پٹ کی خرابی", "براہ کرم تمام فیلڈز کو پُر کریں")
    #         return
    #     else:    
    #         if (not_letter(name)):
    #             messagebox.showerror("خرابی", "نام میں صرف حروف ہونے چاہئیں")
    #             return
    #         if (password!=confirm_password):
    #             messagebox.showerror("خرابی", "پاس ورڈ اور تصدیق شدہ پاس ورڈ میل نہیں کھاتے")
    #             return
    #         if(is_invalid_email(email)):
    #             messagebox.showerror("خرابی", "غلط ای میل")
    #             return
    #         else:
    #             self.handle_signup(email,password,user_type,name)
            
    #         if(user_type=="Tradesperson"):
    #             self.app.show_page(self.labour_main_dashboard)
    #         else:
    #             self.app.show_page(self.employer_main_dashboard)
    def create_user(self):
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
                self.handle_signup(email,password,user_type,name)
                self.current_user=email
                self.current_user_type=user_type
            
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
        title_label = ctk.CTkLabel(frame, text="لاگ ان", font=self.heading_label_font)
        title_label.place(relx=0.5, rely=0.2, anchor="center")  

        # Dropdown for selecting user type (Tradesperson or Employer)
        self.user_type_dropdown = ctk.CTkOptionMenu(frame, values=user_types)
        self.user_type_dropdown.place(relx=0.5, rely=0.3, anchor="center")  

        # Label and Entry for username
        email_label = ctk.CTkLabel(frame, text="Email", font=self.heading_label_font)
        email_label.place(relx=0.5, rely=0.4, anchor="center")  

        self.email_entry_login = ctk.CTkEntry(frame, placeholder_text="Enter your username")
        self.email_entry_login.place(relx=0.5, rely=0.45, anchor="center") 

        # Label and Entry for password
        password_label = ctk.CTkLabel(frame, text=":پاس ورڈ", font=self.heading_label_font)
        password_label.place(relx=0.5, rely=0.55, anchor="center")  

        self.password_entry = ctk.CTkEntry(frame, placeholder_text="اپنا پاس ورڈ درج کریں", show="*")
        self.password_entry.place(relx=0.5, rely=0.6, anchor="center")  

        # login-in button
        Login_button = ctk.CTkButton(frame, text="لاگ ان ", command=self.log_in)
        Login_button.place(relx=0.5, rely=0.7, anchor="center")  

        signup_button=ctk.CTkButton(frame,text="کیا آپ کا اکاؤنٹ نہیں ہے؟ سائن اپ کریں",command=lambda:self.app.show_page(self.signup_page))
        signup_button.place(relx=0.5, rely=0.8, anchor="center")

        return frame
    
    
    def login_database_retrieve(self, username, user_type):
        try:
            return self.db.collection(user_type).document(username).get()
        except Exception as e:
            print(f"Database error: {str(e)}")
            return None

    def log_in(self):
        email = self.email_entry_login.get()
        password = self.password_entry.get()
        user_type=self.user_type_dropdown.get()
        
        try:
            # Get user document
            pass_checker = self.db.collection(user_type).document(email).get().to_dict()
            
            # Check if user exists
            if not pass_checker:
                messagebox.showerror("Error", "User not found")
                return
                
            # Check password
            if password == pass_checker.get("password"):
                self.current_user = email
                self.current_user_type = user_type 
                if user_type == "Tradesperson":
                    self.app.show_page(self.labour_main_dashboard)
                else:
                    self.app.show_page(self.employer_main_dashboard)
            else:
                messagebox.showerror("Error", "Incorrect password")
                
        except Exception as e:
            print(f"Login error: {e}")
            messagebox.showerror("Error", "Login failed")

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
                            text=  " پاس ورڈ کی تبدیل  ", 
                            font=("Arial", 24))
        heading.place(relx=0.5, rely=0.03, anchor="center")
        
        # Current Password field
        current_password_label = ctk.CTkLabel(frame, text="موجودہ پاس ورڈ", font=self.label_data_font)
        current_password_label.place(relx=0.4, rely=0.2, anchor="e")
        self.current_password_entry = ctk.CTkEntry(frame, width=300, height=30, show="*", placeholder_text="موجودہ پاس ورڈ درج کریں")
        self.current_password_entry.place(relx=0.6, rely=0.2, anchor="w")
        
        # New Password field
        new_password_label = ctk.CTkLabel(frame, text="نیا پاس ورڈ", font=self.label_data_font)
        new_password_label.place(relx=0.4, rely=0.3, anchor="e")
        self.new_password_entry = ctk.CTkEntry(frame, width=300, height=30, show="*", placeholder_text="نیا پاس ورڈ درج کریں")
        self.new_password_entry.place(relx=0.6, rely=0.3, anchor="w")
        
        # Confirm New Password field
        confirm_new_password_label = ctk.CTkLabel(frame, text="نئے پاس ورڈ کی تصدیق", font=self.label_data_font)
        confirm_new_password_label.place(relx=0.4, rely=0.4, anchor="e")
        self.confirm_new_password_entry = ctk.CTkEntry(frame, width=300, height=30, show="*", placeholder_text="نئے پاس ورڈ کی تصدیق کریں")
        self.confirm_new_password_entry.place(relx=0.6, rely=0.4, anchor="w")
        
        # Save button
        save_button = ctk.CTkButton(frame, text="تبدیلیاں محفوظ کریں", width=200, height=40, fg_color="#2C7CDB", hover_color="#1C5FAF", command=self.save_password_changes)
        save_button.place(relx=0.5, rely=0.6, anchor="center")
       
        

        # Then use it in the button:
        back_button = ctk.CTkButton(frame, text="واپس", width=200, height=40, 
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
        self.title_label = ctk.CTkLabel(frame, text="مزدور ڈیش بورڈ", font=self.heading_label_font)
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        # Buttons for searching jobs 
        search_jobs_button = ctk.CTkButton(frame, text="نوکریاں تلاش کریں", command=lambda:self.app.show_page(self.job_show_page))
        search_jobs_button.place(relx=0.5, rely=0.3, anchor="center")

        view_profile_button_labour = ctk.CTkButton(frame, text="پروفائل دیکھیں", command=lambda:self.app.show_page(self.labour_profile_view_page))
        view_profile_button_labour.place(relx=0.5, rely=0.4, anchor="center")

        # Change password button
        change_password_button = ctk.CTkButton(frame, text="پاس ورڈ تبدیل کریں", command=lambda:self.app.show_page(self.change_password_page))
        change_password_button.place(relx=0.5, rely=0.5, anchor="center")

        # Logout Button
        logout_button = ctk.CTkButton(frame, text="لاگ آؤٹ", command=self.logout)
        logout_button.place(relx=0.5, rely=0.6, anchor="center")
        
        return frame
    
###############################################################################################################################
###############################################################################################################################

    def labour_profile_view_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        # Header
        heading = ctk.CTkLabel(frame, 
                            text="مزدور کا پروفائل", 
                            font=("Arial", 24))
        heading.place(relx=0.5, rely=0.03, anchor="center")
        
        # Starting positions
        y_start = 0.15  # Match data entry page
        y_increment = 0.1

        cnic, profession, phone, experience, dob, city = self.database_view_profile_labour()
        
        # CNIC
        cnic_label = ctk.CTkLabel(frame, text=": سی این آئی سی ", font=self.label_data_font)
        cnic_label.place(relx=0.35, rely=y_start, anchor="e")
        cnic_value = ctk.CTkLabel(frame, text=cnic, font=self.label_data_font)
        cnic_value.place(relx=0.4, rely=y_start, anchor="w")

        # Profession 
        profession_label = ctk.CTkLabel(frame, text=":پیشہ", font=self.label_data_font)
        profession_label.place(relx=0.35, rely=y_start + y_increment, anchor="e")
        profession_value = ctk.CTkLabel(frame, text=profession, font=self.label_data_font)
        profession_value.place(relx=0.4, rely=y_start + y_increment, anchor="w")

        # Date of Birth
        dob_label = ctk.CTkLabel(frame, text=":تاریخ پیدائش", font=self.label_data_font)
        dob_label.place(relx=0.35, rely=y_start + y_increment*2.5, anchor="e")
        dob_value = ctk.CTkLabel(frame, text=dob, font=self.label_data_font)
        dob_value.place(relx=0.4, rely=y_start + y_increment*2.5, anchor="w")

        # Phone
        phone_label = ctk.CTkLabel(frame, text="فون:", font=self.label_data_font)
        phone_label.place(relx=0.35, rely=y_start + y_increment*3.5, anchor="e")
        phone_value = ctk.CTkLabel(frame, text=phone, font=self.label_data_font)
        phone_value.place(relx=0.4, rely=y_start + y_increment*3.5, anchor="w")

        # Experience
        experience_label = ctk.CTkLabel(frame, text=" :تجربے کے سال ", font=self.label_data_font) 
        experience_label.place(relx=0.35, rely=y_start + y_increment*4.5, anchor="e")
        experience_value = ctk.CTkLabel(frame, text=experience, font=self.label_data_font)
        experience_value.place(relx=0.4, rely=y_start + y_increment*4.5, anchor="w")

        # City
        city_label = ctk.CTkLabel(frame, text=":شہر", font=self.label_data_font)
        city_label.place(relx=0.35, rely=y_start + y_increment*5.5, anchor="e")
        city_value = ctk.CTkLabel(frame, text=city, font=self.label_data_font)
        city_value.place(relx=0.4, rely=y_start + y_increment*5.5, anchor="w")

        # Buttons
        edit_button = ctk.CTkButton(frame, text="ترمیم", command=lambda: self.app.show_page(self.labour_data_update_page), width=120, height=35)
        edit_button.place(relx=0.5, rely=y_start + y_increment*6.5, anchor="center")

        back_button = ctk.CTkButton(frame, text="واپس", width=120, height=35,
                                   command=lambda: self.app.show_page(self.labour_main_dashboard))
        back_button.place(relx=0.35, rely=y_start + y_increment*6.5, anchor="center")
        
        return frame
    
    def database_view_profile_labour(self):
        print(self.current_user)
        print(self.current_user_type)
        # if self.current_user == None or self.current_user_type==None:
        #     messagebox.showerror("Error", "User not logged in")
        #     return None, None, None, None, None, None
            
        try:
            dict = self.db.collection(self.current_user_type).document(self.current_user).get().to_dict()
            return (
                dict.get("cnic", "N/A"),
                dict.get("profession", "N/A"), 
                dict.get("phone", "N/A"),
                dict.get("experience", "N/A"),
                dict.get("dob", "N/A"),
                dict.get("city", "N/A")
            )
        except Exception as e:
            print(f"Error retrieving profile: {e}")
            return None, None, None, None, None, None

##########################################################################################################################################
##########################################################################################################################################
    
    def labour_data_update_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)

        # Header
        heading = ctk.CTkLabel(frame, text="ورکڈن", font=self.heading_label_font)
        heading.place(relx=0.5, rely=0.05, anchor="center")

        # Form fields with consistent spacing
        y_start = 0.15  # Starting y position
        y_increment = 0.1  # Space between fields

        # CNIC
        cnic_label = ctk.CTkLabel(frame, text=":سی این آئی سی", font=self.label_data_font)
        cnic_label.place(relx=0.35, rely=y_start, anchor="e")
        self.cnic_entry_box = ctk.CTkEntry(frame, width=250, height=35, placeholder_text="e.g 4210112345678")
        self.cnic_entry_box.place(relx=0.4, rely=y_start, anchor="w")

        # Profession
        profession_label = ctk.CTkLabel(frame, text=":پیشہ", font=self.label_data_font)
        profession_label.place(relx=0.35, rely=y_start + y_increment, anchor="e")
        self.profession_box = ctk.CTkComboBox(frame, values=professions, width=250, height=35, command=self.on_profession_change)
        self.profession_box.place(relx=0.4, rely=y_start + y_increment, anchor="w")

        # Other Profession Entry
        self.other_profession_entry = ctk.CTkEntry(frame, placeholder_text="براہ کرم دیگر پیشہ کی وضاحت کریں", width=250, height=35)
        self.other_profession_entry.place(relx=0.4, rely=y_start + y_increment*1.5, anchor="w")
        self.other_profession_entry.configure(state="disabled")

        # Date of Birth
        dob_label = ctk.CTkLabel(frame, text=":تاریخ پیدائش", font=self.label_data_font)
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
                select_btn = ctk.CTkButton(self.calendar_frame, text="منتخب کریں", command=get_date)
                select_btn.pack(pady=5)

        calendar_btn = ctk.CTkButton(date_frame, text="📅", width=30, height=35, command=toggle_calendar)
        calendar_btn.pack(side="left")

        # Phone
        phone_label = ctk.CTkLabel(frame, text=":فون", font=self.label_data_font)
        phone_label.place(relx=0.35, rely=y_start + y_increment*3.5, anchor="e")
        self.phone_entry_box = ctk.CTkEntry(frame, width=250, height=35, placeholder_text="e.g 03001234567")
        self.phone_entry_box.place(relx=0.4, rely=y_start + y_increment*3.5, anchor="w")

        # Experience
        experience_label = ctk.CTkLabel(frame, text=":تجربے کے سال", font=self.label_data_font)
        experience_label.place(relx=0.35, rely=y_start + y_increment*4.5, anchor="e")
        self.experience_entry_box = ctk.CTkEntry(frame, width=250, height=35, placeholder_text="e.g 10")
        self.experience_entry_box.place(relx=0.4, rely=y_start + y_increment*4.5, anchor="w")

        # City
        city_label = ctk.CTkLabel(frame, text=":شہر", font=self.label_data_font)
        city_label.place(relx=0.35, rely=y_start + y_increment*5.5, anchor="e")
        self.city_box = ctk.CTkComboBox(frame, values=cities, width=250, height=35)
        self.city_box.place(relx=0.4, rely=y_start + y_increment*5.5, anchor="w")

        # Buttons
        submit_button = ctk.CTkButton(frame, text="جمع کرائیں", command=self.labour_entry, width=120, height=35)
        submit_button.place(relx=0.5, rely=y_start + y_increment*6.5, anchor="center")

        back_button = ctk.CTkButton(frame, text="واپس", width=120, height=35, 
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
            messagebox.showerror("خرابی، براہ کرم تمام فیلڈز کو پُر کریں")
            return
        else:
            if(is_invalid_cnic(cnic)):
                messagebox.showerror("ان پٹ کی غلطی، براہ کرم ایک درست سی این آئی سی نمبر درج کریں")
                return
            if (is_invalid_phone(phone)):
                messagebox.showerror("ان پٹ کی غلطی، براہ کرم ایک درست فون نمبر درج کریں")
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
                return [{"name": "کوئی ڈیٹا نہیں",
             "phone": "نہيں دستیاب", 
             "address": "نہيں دستیاب",
             "description": "کوئی ملازمت نہیں ملی",
             "job price": "نہيں دستیاب"}]


            for doc in docs:
                data = doc.to_dict()
                if data:  # Check if document data exists
                    job_data_list.append(data)
                
            return job_data_list if job_data_list else [{"name": "کوئی ڈیٹا نہیں",
                                             "phone": "نہیں دستیاب",
                                             "address": "نہیں دستیاب", 
                                             "description": "کوئی نوکری نہیں ملی",
                                             "job price": "نہیں دستیاب"}]
        except:
           return [{"name": "کوئی ڈیٹا نہیں",
             "phone": "نہیں دستیاب",
             "address": "نہیں دستیاب",
             "description": "نوکری حاصل کرنے میں خرابی",
             "job price": "نہیں دستیاب"}]


    def job_show_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        # Header
        heading = ctk.CTkLabel(frame, 
                            text="دستیاب نوکریاں", 
                            font=("Arial", 24))
        heading.place(relx=0.5, rely=0.05, anchor="center")
        
        # City Filter
        city_label = ctk.CTkLabel(frame, text="شہر کے لحاظ سے فلٹر", font=self.label_data_font)
        city_label.place(relx=0.3, rely=0.1, anchor="e")
        self.job_city_filter = ctk.CTkComboBox(frame, values=cities, width=250)
        self.job_city_filter.place(relx=0.4, rely=0.1, anchor="w")

        # Profession Filter
        profession_label = ctk.CTkLabel(frame, text="پیشہ کے لحاظ سے فلٹر", font=self.label_data_font)
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
        self.other_job_type_filter = ctk.CTkEntry(frame, placeholder_text="براہ کرم دوسرا پیشہ بتائیں", width=250)
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
                
                # Display job information in Urdu
                name_label = ctk.CTkLabel(job_frame, text=f"رابطہ نام: {job['name']}", font=("Arial", 16))
                name_label.place(relx=0.05, rely=0.2, anchor="w")
                
                price_label = ctk.CTkLabel(job_frame, text=f"نوکری کی قیمت: Rs. {job['job price']}", font=("Arial", 14))
                price_label.place(relx=0.05, rely=0.5, anchor="w")
                
                phone_label = ctk.CTkLabel(job_frame, text=f"فون: {job['phone']}", font=("Arial", 14))
                phone_label.place(relx=0.05, rely=0.8, anchor="w")
                
                address_label = ctk.CTkLabel(job_frame, text=f"پتہ: {job['address']}", font=("Arial", 14))
                address_label.place(relx=0.4, rely=0.3, anchor="w")
                
                description_label = ctk.CTkLabel(job_frame, text=f"تفصیل: {job['description']}", font=("Arial", 14))
                description_label.place(relx=0.4, rely=0.7, anchor="w")

# Add search button with Urdu text
        search_button = ctk.CTkButton(frame, text="تلاش کریں", width=120, height=32, command=display_jobs)
        search_button.place(relx=0.7, rely=0.15, anchor="center")

# Back Button with Urdu text
        back_button = ctk.CTkButton(frame, text="واپس", width=120, height=32, command=lambda: self.app.show_page(self.labour_main_dashboard))
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
                            text="ملازمت دینے والے کا ڈیش بورڈ", 
                            font=("Arial", 24))
        heading.place(relx=0.5, rely=0.03, anchor="center")
        
        # Description
        description = ctk.CTkLabel(frame, 
                                text="اپنی نوکری کی پوسٹنگز کا انتظام کریں اور درخواستیں دیکھیں", 
                                font=("Arial", 16))
        description.place(relx=0.5, rely=0.1, anchor="center")

        # Available Tradespersons Button
        available_labour_button_dashboard = ctk.CTkButton(frame, text="دستیاب ہنر مند", width=200, height=40,
                                                        command=lambda: self.app.show_page(self.available_labour_page))
        available_labour_button_dashboard.place(relx=0.5, rely=0.3, anchor="center")
        
        # Create Job Button  
        create_job_button = ctk.CTkButton(frame, text="نوکری کی پوسٹنگ کریں", width=200, height=40,
                                        command=lambda: self.app.show_page(self.job_submission_page))
        create_job_button.place(relx=0.5, rely=0.4, anchor="center")
        
        # Delete Job Button
        delete_job_button = ctk.CTkButton(frame, text="نوکری کی پوسٹنگ حذف کریں", width=200, height=40,
                                        command=lambda: self.app.show_page(self.delete_old_jobs_page))
        delete_job_button.place(relx=0.5, rely=0.5, anchor="center")
        
        # Change Password Button
        change_password_button = ctk.CTkButton(frame, text="پاس ورڈ تبدیل کریں", width=200, height=40,
                                             command=lambda: self.app.show_page(self.change_password_page))
        change_password_button.place(relx=0.5, rely=0.6, anchor="center")
        
        # Profile Button  
        profile_button = ctk.CTkButton(frame, text="پروفائل", width=200, height=40,
                                     command=lambda: self.app.show_page(self.employer_profile_view_page))
        profile_button.place(relx=0.5, rely=0.7, anchor="center")
        
        # Logout Button
        logout_button = ctk.CTkButton(frame, text="لاگ آؤٹ", width=200, height=40,
                                    command=self.logout)
        logout_button.place(relx=0.5, rely=0.8, anchor="center")
        
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
            phone = "فیلڈ بھرا نہیں گیا۔ براہ کرم اپنا پروفائل اپ ڈیٹ کریں"
        if address is None:    
            address = "فیلڈ بھرا نہیں گیا۔ براہ کرم اپنا پروفائل اپ ڈیٹ کریں"
        if city is None:
            city = "فیلڈ بھرا نہیں گیا۔ براہ کرم اپنا پروفائل اپ ڈیٹ کریں"
        return phone, address, city
         
    def employer_profile_view_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        # Header
        heading = ctk.CTkLabel(frame, 
                    text="ملازمت دینے والے کا پروفائل", 
                    font=("Arial", 24))
        heading.place(relx=0.5, rely=0.03, anchor="center")
        # Starting positions
        y_start = 0.2
        y_increment = 0.1

        phone,address,city=self.database_view_profile_employer()
        # Phone
        phone_label = ctk.CTkLabel(frame, text="فون", font=self.label_data_font)
        phone_label.place(relx=0.4, rely=y_start, anchor="e")
        phone_entry = ctk.CTkEntry(frame, width=300, height=30)
        phone_entry.insert(0,phone)
        phone_entry.configure(state="disabled")
        phone_entry.place(relx=0.6, rely=y_start, anchor="w")
        
        # Address
        address_label = ctk.CTkLabel(frame, text="پتہ", font=self.label_data_font)
        address_label.place(relx=0.4, rely=y_start + y_increment, anchor="e")
        address_entry = ctk.CTkEntry(frame, width=300, height=30)
        address_entry.insert(0,address)
        address_entry.configure(state="disabled")
        address_entry.place(relx=0.6, rely=y_start + y_increment, anchor="w")
        
        # City 
        city_label = ctk.CTkLabel(frame, text="شہر", font=self.label_data_font)
        city_label.place(relx=0.4, rely=y_start + y_increment*2, anchor="e")
        city_entry = ctk.CTkEntry(frame, width=300, height=30)
        city_entry.insert(0,city)
        city_entry.configure(state="disabled")
        city_entry.place(relx=0.6, rely=y_start + y_increment*2, anchor="w")

        edit_button = ctk.CTkButton(frame, text="ترمیم کریں", width=120, height=35,
                        command=lambda: self.app.show_page(self.employer_profile_update_page))
        edit_button.place(relx=0.5, rely=0.8, anchor="center")

        back_button = ctk.CTkButton(frame, text="واپس", width=120, height=35,command=lambda: self.app.show_page(self.employer_main_dashboard))
        back_button.place(relx=0.3, rely=0.8, anchor="center")

        return frame
#############################################################################################################################
########################################################################################################################################

    def employer_profile_update_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        # Header
        heading = ctk.CTkLabel(frame, 
                            text="ملازمت دینے والے کا پروفائل", 
                            font=("Arial", 24))
        heading.place(relx=0.5, rely=0.03, anchor="center")
        # Starting positions
        y_start = 0.2
        y_increment = 0.1

        # Phone
        phone_label = ctk.CTkLabel(frame, text="فون", font=self.label_data_font)
        phone_label.place(relx=0.4, rely=y_start, anchor="e")
        self.phone_entry_employer = ctk.CTkEntry(frame, width=300, height=30)
        self.phone_entry_employer.place(relx=0.6, rely=y_start, anchor="w")
        
        # Address
        address_label = ctk.CTkLabel(frame, text="پتہ", font=self.label_data_font)
        address_label.place(relx=0.4, rely=y_start + y_increment, anchor="e")
        self.address_entry_employer = ctk.CTkEntry(frame, width=300, height=30)
        self.address_entry_employer.place(relx=0.6, rely=y_start + y_increment, anchor="w")
        
        # City 
        city_label = ctk.CTkLabel(frame, text="شہر", font=self.label_data_font)
        city_label.place(relx=0.4, rely=y_start + y_increment*2, anchor="e")
        self.city_box_employer = ctk.CTkComboBox(frame, values=cities, width=300, height=30)
        self.city_box_employer.place(relx=0.6, rely=y_start + y_increment*2, anchor="w")

        update_button = ctk.CTkButton(frame, text="اپ ڈیٹ کریں", width=120, height=35,command=self.employer_profile_entry)
        update_button.place(relx=0.5, rely=0.8, anchor="center")

        back_button = ctk.CTkButton(frame, text="واپس", width=120, height=35,command=lambda: self.app.show_page(self.employer_profile_view_page))
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
            messagebox.showerror("غلطی براہ کرم تمام فیلڈز کو پُر کریں")
            return
        else:
            if (is_invalid_phone(phone)):
                messagebox.showerror("ان پٹ کی غلطی براہ کرم ایک درست فون نمبر درج کریں")
                return
            self.employer_profile_database_entry(phone,address,city)
            self.app.show_page(self.employer_profile_view_page)
#####################################################################################################################################
####################################################################################################################################    
    
    def job_submission_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)

        # Header
        heading = ctk.CTkLabel(frame, text="نوکری کی جمع کرائی", font=self.heading_label_font)
        heading.place(relx=0.5, rely=0.05, anchor="center")

        # Starting vertical position and spacing
        y_start = 0.2
        y_increment = 0.1

        # City Selection
        city_label = ctk.CTkLabel(frame, text=":شہر", font=self.label_data_font)
        city_label.place(relx=0.35, rely=y_start, anchor="e")
        self.city_box_job_sub = ctk.CTkOptionMenu(frame, values=cities, width=250)
        self.city_box_job_sub.place(relx=0.4, rely=y_start, anchor="w")

        # Job Type Selection
        job_type_label = ctk.CTkLabel(frame, text=":نوکری کی قسم", font=self.label_data_font)
        job_type_label.place(relx=0.35, rely=y_start + y_increment, anchor="e")
        self.job_type_box_sub = ctk.CTkOptionMenu(frame, values=professions, width=250, command=self.on_job_type_change)
        self.job_type_box_sub.place(relx=0.4, rely=y_start + y_increment, anchor="w")

        # Other Job Type Entry
        self.other_job_entry = ctk.CTkEntry(frame, placeholder_text="براہ کرم دوسری نوکری کی قسم بتائیں", width=250)
        self.other_job_entry.place(relx=0.4, rely=y_start + y_increment*2, anchor="w")
        self.other_job_entry.configure(state="disabled")

        # User Name Entry
        job_price_label = ctk.CTkLabel(frame, text=":نوکری کی اجرت", font=self.label_data_font)
        job_price_label.place(relx=0.35, rely=y_start + y_increment*3, anchor="e")
        self.job_price_entry = ctk.CTkEntry(frame, placeholder_text="e.g 1000", width=250)
        self.job_price_entry.place(relx=0.4, rely=y_start + y_increment*3, anchor="w")

        # Job Description
        job_description_label = ctk.CTkLabel(frame, text=":نوکری کی تفصیل", font=self.label_data_font)
        job_description_label.place(relx=0.35, rely=y_start + y_increment*4, anchor="e")
        self.job_description_entry = ctk.CTkTextbox(frame, width=400, height=150)
        self.job_description_entry.place(relx=0.4, rely=y_start + y_increment*4.5, anchor="w")
        
        # Add placeholder text
        self.job_description_entry.insert("0.0", "...یہاں تفصیلی نوکری کی وضاحت درج کریں")
        self.job_description_entry.configure(text_color="gray")
        
        def on_focus_in(event):
            if self.job_description_entry.get("0.0", "end-1c") == "...یہاں تفصیلی نوکری کی وضاحت درج کریں":
                self.job_description_entry.delete("0.0", "end")
                self.job_description_entry.configure(text_color="white")
            
        def on_focus_out(event):
            if self.job_description_entry.get("0.0", "end-1c").strip() == "":
                self.job_description_entry.insert("0.0", "...یہاں تفصیلی نوکری کی وضاحت درج کریں")
                self.job_description_entry.configure(text_color="gray")
            
        self.job_description_entry.bind("<FocusIn>", on_focus_in)
        self.job_description_entry.bind("<FocusOut>", on_focus_out)

        # Buttons at the bottom
        back_button = ctk.CTkButton(frame, text="واپس", width=120, height=35,
                                   command=lambda: self.app.show_page(self.employer_main_dashboard))
        back_button.place(relx=0.4, rely=0.9, anchor="center")

        submit_button = ctk.CTkButton(frame, text="جمع کریں", width=120, height=35,
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
        try:
            doc_ref = self.db.collection("City wise Job data").document(city).collection(job_type).document()
            unique_id = doc_ref.id

            employer_data = self.db.collection(self.current_user_type).document(self.current_user).get().to_dict()
            
            # Check if employer profile is complete
            if not all([employer_data.get("phone"), employer_data.get("address"), employer_data.get("city")]):
                messagebox.showerror("Error", "Please complete your profile before posting a job")
                self.app.show_page(self.employer_profile_update_page)
                return False

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
            })
            return True

        except Exception as e:
            print(f"Error posting job: {str(e)}")
            messagebox.showerror("Error", "Failed to post job. Please try again.")
            return False

    def job_submission(self):
        try:
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
                if self.job_database_entry(city,job_type,price,job_description):
                    self.app.show_page(self.employer_main_dashboard)

        except Exception as e:
            print(f"Error in job submission: {str(e)}")
            messagebox.showerror("Error", "Job submission failed. Please try again.")

##########################################################################################################################################################
##########################################################################################################################################################

    def available_labour_database_get(self,city,profession):
        try:
            data = self.db.collection("City wise Tradesperson data").document(city).collection(profession).get()
            labour_list = list()
            
            if not data:  # If no data is returned
                return [{
            "name": "کوئی ڈیٹا نہیں",
            "experience": "کوئی کارکن نہیں ملا",
            "phone": "نہیں دستیاب",
            "email": "موجودہ فلٹرز کی بنیاد پر کوئی نتیجہ نہیں"
        }]
            for doc in data:
                dict = doc.to_dict()
                dict["email"] = doc.id
                print(dict)
                labour_list.append(dict)

            return labour_list if labour_list else [{
                "name": "کوئی ڈیٹا نہیں",
                "experience": "کوئی کارکن نہیں ملا",
                "phone": "نہیں دستیاب", 
                "email": "موجودہ فلٹرز کی بنیاد پر کوئی نتیجہ نہیں"
            }]
        except:
            return [{
                "name": "کوئی ڈیٹا نہیں",
                "experience": "کوئی کارکن نہیں ملا",
                "phone": "نہیں دستیاب",
                "email": "موجودہ فلٹرز کی بنیاد پر کوئی نتیجہ نہیں"
            }]


            
    def available_labour_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        # Header
        heading = ctk.CTkLabel(frame, 
                            text="دستیاب محنت", 
                            font=("Arial", 24))
        heading.place(relx=0.5, rely=0.03, anchor="center")
        
        # City Filter
        available_labour_city_label = ctk.CTkLabel(frame, text="شہر کے حساب سے فلٹر", font=self.label_data_font)
        available_labour_city_label.place(relx=0.3, rely=0.1, anchor="e")
        self.available_labour_city_filter = ctk.CTkComboBox(frame, values=cities, width=250)
        self.available_labour_city_filter.place(relx=0.4, rely=0.1, anchor="w")

        # Profession Filter
        available_labour_profession_label = ctk.CTkLabel(frame, text="پیشہ کے حساب سے فلٹر", font=self.label_data_font)
        available_labour_profession_label.place(relx=0.3, rely=0.15, anchor="e")
        self.available_labour_profession_filter = ctk.CTkComboBox(frame, values=professions, width=250, command=self.on_profession_change)
        self.available_labour_profession_filter.place(relx=0.4, rely=0.15, anchor="w")
        # Other Profession Entry
        self.other_profession_filter = ctk.CTkEntry(frame, placeholder_text="براہ کرم دوسرا پیشہ مخصوص کریں", width=250)
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
                name_label = ctk.CTkLabel(labour_frame, text=f":نام {labour['name']}", font=("Arial", 16))
                name_label.place(relx=0.05, rely=0.2, anchor="w")
                
                experience_label = ctk.CTkLabel(labour_frame, text=f":تجربہ {labour['experience']} years", font=("Arial", 14))
                experience_label.place(relx=0.05, rely=0.5, anchor="w")
                
                phone_label = ctk.CTkLabel(labour_frame, text=f":فون {labour['phone']}", font=("Arial", 14))
                phone_label.place(relx=0.05, rely=0.8, anchor="w")
                
                email_label = ctk.CTkLabel(labour_frame, text=f":ای میل {labour['email']}", font=("Arial", 14))
                email_label.place(relx=0.5, rely=0.5, anchor="center")

        # Add search button
        search_button = ctk.CTkButton(frame, text="تلاش کریں", width=120, height=32, 
                                    command=display_labour)
        search_button.place(relx=0.7, rely=0.15, anchor="center")
        
        # Back Button
        back_button = ctk.CTkButton(frame, text="واپس", width=120, height=32, 
                                   command=lambda: self.app.show_page(self.employer_main_dashboard))
        back_button.place(relx=0.5, rely=0.9, anchor="center")
        
        return frame
    
    def on_profession_change(self, selected_profession):
        if selected_profession == "Other":
            self.other_profession_filter.configure(state="normal")
        else:
            self.other_profession_filter.delete(0, "end") 
            self.other_profession_filter.configure(state="disabled")

##########################################################################################################################################################
##########################################################################################################################################################

    def delete_old_jobs_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        # Header
        heading = ctk.CTkLabel(frame, text="ملازمت کی اشاعتیں حذف کریں", font=("Arial", 24))
        heading.place(relx=0.5, rely=0.05, anchor="center")

        # Get posted job IDs from employer's data
        employer_data = self.db.collection(self.current_user_type).document(self.current_user).get().to_dict()
        job_ids = employer_data.get("posted job ids", [])

        # Create scrollable frame for job listings
        scrollable_frame = ctk.CTkScrollableFrame(frame, width=900, height=400)
        scrollable_frame.place(relx=0.5, rely=0.25, anchor="n")

        # Display each job posting
        for i, job_id in enumerate(job_ids, 1):
            # Get job details
            job_type_city = self.db.collection("Job ids").document(job_id).get().to_dict()
            if job_type_city:
                city = job_type_city.get("city")
                job_type = job_type_city.get("job type")
                
                # Create frame for each job
                job_frame = ctk.CTkFrame(scrollable_frame, width=880, height=100)
                job_frame.pack(pady=10, fill="x", padx=5)
                job_frame.pack_propagate(False)
                
                # Job info
                info_label = ctk.CTkLabel(job_frame, 
                                        text=f"ملازمت #{i}\nشہر: {city}\nقسم: {job_type}",
                                        font=("Arial", 14))
                info_label.place(relx=0.1, rely=0.5, anchor="w")
                
                # Delete button
                delete_btn = ctk.CTkButton(job_frame, text="حذف کریں",
                                         command=lambda id=job_id, type=job_type, city=city: self.delete_job(id, type, city))
                delete_btn.place(relx=0.9, rely=0.5, anchor="e")

        # Back button
        back_button = ctk.CTkButton(frame, text="واپس", width=120, height=32,
                                   command=lambda: self.app.show_page(self.employer_main_dashboard))
        back_button.place(relx=0.5, rely=0.9, anchor="center")
        
        return frame

    def retrive_job_for_job_deletion_page(self, job_id):
        try:
            job_type_city = self.db.collection("Job ids").document(job_id).get()
            
            if not job_type_city.exists:
                print(f":ملازمت کی شناخت کے لئے کوئی دستاویز نہیں ملی {job_id}")
                return None, None
                
            job_data = job_type_city.to_dict()
            if not job_data:
                print(f":دستاویز موجود ہے لیکن ملازمت کی شناخت کے لئے کوئی ڈیٹا نہیں ملا {job_id}")
                return None, None
                
            city = job_data.get("city")
            job_type = job_data.get("job type")
            
            if not city or not job_type:
                print(f":ملازمت کی شناخت کے لئے ضروری فیلڈز غائب ہیں {job_id}")
                return None, None
                
            return city, job_type
            
        except Exception as e:
            print(f":ملازمت کا ڈیٹا حاصل کرنے میں خرابی {str(e)}")
            return None, None


    def delete_job(self, job_id, job_type, city):
        # Delete from City wise Job data
        self.db.collection("City wise Job data").document(city).collection(job_type).document(job_id).delete()
        
        # Update employer's posted job ids
        employer_data = self.db.collection(self.current_user_type).document(self.current_user).get().to_dict()
        if "posted job ids" in employer_data:
            employer_data["posted job ids"].remove(job_id)
            self.db.collection(self.current_user_type).document(self.current_user).set(employer_data)
        
        # Refresh page
        self.app.show_page(self.delete_old_jobs_page)