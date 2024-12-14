import customtkinter as ctk
from PIL import Image, ImageTk

class EmployerJobApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x800")  # Increased window size to fit the content
        self.language = "English"  # Default language is English
        self.screen_stack = []  # Stack to manage screens
        self.create_employer_main_screen()

    def create_employer_main_screen(self):
        """Main screen where employer can choose to post job or search for laborers."""
        self.screen_stack.append("employer_main_screen")

        # Main screen title
        self.title_label = ctk.CTkLabel(self.root, text=self.get_text("Employer Dashboard"), font=("Arial", 24))
        self.title_label.pack(pady=20)

        # Buttons for posting job and searching laborers
        post_job_button = ctk.CTkButton(self.root, text=self.get_text("Post a Job"), command=self.create_post_job_screen)
        post_job_button.pack(pady=20)

        search_labor_button = ctk.CTkButton(self.root, text=self.get_text("Search for Laborers"), command=self.create_search_labor_screen)
        search_labor_button.pack(pady=20)

        # Back button to return to the main menu
        back_button = ctk.CTkButton(self.root, text=self.get_text("Back"), command=self.go_back)
        back_button.pack(pady=20)

    def create_post_job_screen(self):
        """Screen where employer can post a job."""
        self.screen_stack.append("post_job_screen")

        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Job Posting Form Title
        self.title_label = ctk.CTkLabel(self.root, text=self.get_text("Post a Job"), font=("Arial", 24))
        self.title_label.pack(pady=20)

        # Select Skill
        self.skill_label = ctk.CTkLabel(self.root, text=self.get_text("Select Skill"), font=("Arial", 16))
        self.skill_label.pack(pady=10)

        self.skills = ["Carpenter", "Electrician", "Plumber", "Painter"]
        self.skill_dropdown = ctk.CTkOptionMenu(self.root, values=self.skills)
        self.skill_dropdown.pack(pady=10)

        # Select Location
        self.location_label = ctk.CTkLabel(self.root, text=self.get_text("Select Location"), font=("Arial", 16))
        self.location_label.pack(pady=10)

        self.locations = ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Peshawar", "Multan"]
        self.location_dropdown = ctk.CTkOptionMenu(self.root, values=self.locations)
        self.location_dropdown.pack(pady=10)

        # Job Description
        self.job_description_label = ctk.CTkLabel(self.root, text=self.get_text("Job Description"), font=("Arial", 16))
        self.job_description_label.pack(pady=10)

        self.job_description_entry = ctk.CTkEntry(self.root, placeholder_text=self.get_text("Enter job details here"))
        self.job_description_entry.pack(pady=10)

        # Submit Job Button
        submit_job_button = ctk.CTkButton(self.root, text=self.get_text("Post Job"), command=self.submit_job)
        submit_job_button.pack(pady=20)

        # Back Button
        back_button = ctk.CTkButton(self.root, text=self.get_text("Back"), command=self.go_back)
        back_button.pack(pady=20)

    def submit_job(self):
        """Submit the job posting."""
        skill = self.skill_dropdown.get()
        location = self.location_dropdown.get()
        job_description = self.job_description_entry.get()

        # Here you would save this data to a database or show a confirmation message
        print(f"Job Posted: {skill}, {location}, {job_description}")

        # Show confirmation message (for demo purposes)
        confirmation_label = ctk.CTkLabel(self.root, text=self.get_text("Job Posted Successfully!"), font=("Arial", 16))
        confirmation_label.pack(pady=10)

    def create_search_labor_screen(self):
        """Screen where employer can search for laborers based on skill and location."""
        self.screen_stack.append("search_labor_screen")

        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Search Laborers Title
        self.title_label = ctk.CTkLabel(self.root, text=self.get_text("Search for Laborers"), font=("Arial", 24))
        self.title_label.pack(pady=20)

        # Select Skill
        self.skill_label = ctk.CTkLabel(self.root, text=self.get_text("Select Skill"), font=("Arial", 16))
        self.skill_label.pack(pady=10)

        self.skills = ["Carpenter", "Electrician", "Plumber", "Painter"]
        self.skill_dropdown = ctk.CTkOptionMenu(self.root, values=self.skills)
        self.skill_dropdown.pack(pady=10)

        # Select Location
        self.location_label = ctk.CTkLabel(self.root, text=self.get_text("Select Location"), font=("Arial", 16))
        self.location_label.pack(pady=10)

        self.locations = ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Peshawar", "Multan"]
        self.location_dropdown = ctk.CTkOptionMenu(self.root, values=self.locations)
        self.location_dropdown.pack(pady=10)

        # Search Button
        search_button = ctk.CTkButton(self.root, text=self.get_text("Search Laborers"), command=self.search_laborers)
        search_button.pack(pady=20)

        # Back Button
        back_button = ctk.CTkButton(self.root, text=self.get_text("Back"), command=self.go_back)
        back_button.pack(pady=20)

    def search_laborers(self):
        """Search for laborers based on selected skill and location."""
        skill = self.skill_dropdown.get()
        location = self.location_dropdown.get()

        # Here you would perform a database search or display mock laborers (for demo purposes)
        print(f"Searching laborers: {skill}, {location}")

        # Display results (for demo purposes)
        search_results_label = ctk.CTkLabel(self.root, text=f"Laborers available for {skill} in {location}", font=("Arial", 16))
        search_results_label.pack(pady=10)

        # Sample laborer profiles (for demo purposes)
        laborer_profiles = [
            "John Doe - Carpenter",
            "Jane Smith - Electrician",
            "Michael Johnson - Plumber",
        ]
        for profile in laborer_profiles:
            laborer_label = ctk.CTkLabel(self.root, text=profile, font=("Arial", 14))
            laborer_label.pack(pady=5)

    def go_back(self):
        """Navigate back to the previous screen."""
        if self.screen_stack:
            last_screen = self.screen_stack.pop()
            for widget in self.root.winfo_children():
                widget.destroy()

            # Navigate to the previous screen
            if last_screen == "employer_main_screen":
                self.create_employer_main_screen()
            elif last_screen == "post_job_screen":
                self.create_employer_main_screen()
            elif last_screen == "search_labor_screen":
                self.create_employer_main_screen()

    def get_text(self, text):
        """This function returns the translated text based on the selected language."""
        translations = {
            "Employer Dashboard": {"English": "Employer Dashboard", "Urdu": "ملازمت دینے والا ڈیش بورڈ"},
            "Post a Job": {"English": "Post a Job", "Urdu": "ملازمت پوسٹ کریں"},
            "Search for Laborers": {"English": "Search for Laborers", "Urdu": "مزدوروں کو تلاش کریں"},
            "Select Skill": {"English": "Select Skill", "Urdu": "مہارت منتخب کریں"},
            "Select Location": {"English": "Select Location", "Urdu": "مقام منتخب کریں"},
            "Job Description": {"English": "Job Description", "Urdu": "ملازمت کی تفصیل"},
            "Enter job details here": {"English": "Enter job details here", "Urdu": "یہاں ملازمت کی تفصیل درج کریں"},
            "Post Job": {"English": "Post Job", "Urdu": "ملازمت پوسٹ کریں"},
            "Search Laborers": {"English": "Search Laborers", "Urdu": "مزدوروں کو تلاش کریں"},
            "Job Posted Successfully!": {"English": "Job Posted Successfully!", "Urdu": "ملازمت کامیابی سے پوسٹ ہو گئی!"},
            "Back": {"English": "Back", "Urdu": "پیچھے"},
        }
        return translations.get(text, {}).get(self.language, text)

if __name__ == "__main__":
    root = ctk.CTk()
    app = EmployerJobApp(root)
    root.mainloop()
