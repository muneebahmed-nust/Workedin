import customtkinter as ctk
from PIL import Image, ImageTk

class LaborEmploymentApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x800")  # Set a manageable window size
        self.language = "English"  # Default language is English
        self.screen_stack = []  # Stack to manage screens
        self.skill = None
        self.location = None
        self.create_skill_selection_screen()

    def create_skill_selection_screen(self):
        # Save the current screen to stack (this will be the root screen)
        self.screen_stack.append("skill_selection_screen")

        # Create the skill selection page title
        self.title_label = ctk.CTkLabel(self.root, text=self.get_text("Select Your Skill"), font=("Arial", 24))
        self.title_label.pack(pady=20)

        # Load images for each profession (resize images to 600x600 for better fit)
        self.carpenter_img = self.load_image("carpenter.png")
        self.electrician_img = self.load_image("electrician.png")
        self.plumber_img = self.load_image("plumber.png")
        self.painter_img = self.load_image("painter.png")

        # Create a frame to arrange the images and buttons
        self.skills_frame = ctk.CTkFrame(self.root)
        self.skills_frame.pack(pady=20)

        # Carpenter selection (top row, first column)
        carpenter_button = ctk.CTkButton(self.skills_frame, image=self.carpenter_img, text=self.get_text("Select Carpenter"), compound="top", command=lambda: self.on_skill_selected("Carpenter"))
        carpenter_button.grid(row=0, column=0, padx=20, pady=10)

        # Electrician selection (top row, second column)
        electrician_button = ctk.CTkButton(self.skills_frame, image=self.electrician_img, text=self.get_text("Select Electrician"), compound="top", command=lambda: self.on_skill_selected("Electrician"))
        electrician_button.grid(row=0, column=1, padx=20, pady=10)

        # Plumber selection (bottom row, first column)
        plumber_button = ctk.CTkButton(self.skills_frame, image=self.plumber_img, text=self.get_text("Select Plumber"), compound="top", command=lambda: self.on_skill_selected("Plumber"))
        plumber_button.grid(row=1, column=0, padx=20, pady=10)

        # Painter selection (bottom row, second column)
        painter_button = ctk.CTkButton(self.skills_frame, image=self.painter_img, text=self.get_text("Select Painter"), compound="top", command=lambda: self.on_skill_selected("Painter"))
        painter_button.grid(row=1, column=1, padx=20, pady=10)

        # Back button to return to the main menu
        back_button = ctk.CTkButton(self.root, text=self.get_text("Back"), command=self.go_back)
        back_button.pack(pady=20)

    def load_image(self, image_name):
        """
        This method loads an image given its filename and returns it as a CTkImage object.
        Ensure that the images are in the same directory as the script or provide the full path.
        """
        try:
            img = Image.open(image_name)  # Open the image file
            img = img.resize((500, 500))  # Resize image to a more manageable size (500x500)
            return ctk.CTkImage(light_image=img, dark_image=img)  # Use CTkImage instead of PhotoImage
        except Exception as e:
            print(f"Error loading image {image_name}: {e}")
            return None  # Return None if the image cannot be loaded

    def on_skill_selected(self, skill):
        """
        This method handles the skill selection.
        After a skill is selected, navigate to the location selection screen.
        """
        self.skill = skill  # Store the selected skill
        print(f"Selected skill: {self.skill}")  # Debug: print the selected skill

        # Move to the location selection screen
        self.screen_stack.append("location_selection_screen")

        for widget in self.root.winfo_children():
            widget.destroy()

        # Create location selection screen
        self.create_location_selection_screen()

    def create_location_selection_screen(self):
        # Save the current screen to stack (this will be the root screen)
        self.screen_stack.append("location_selection_screen")

        # Create the location selection page title
        self.title_label = ctk.CTkLabel(self.root, text=self.get_text("Select Your Location"), font=("Arial", 24))
        self.title_label.pack(pady=20)

        # Load images for each city (resize images to 500x500)
        self.lahore_img = self.load_image("lahore.png")
        self.karachi_img = self.load_image("karachi.png")
        self.islamabad_img = self.load_image("islamabad.png")
        self.faisalabad_img = self.load_image("faisalabad.png")
        self.peshawar_img = self.load_image("peshawar.png")
        self.multan_img = self.load_image("multan.png")

        # Create a frame to arrange the images and buttons
        self.location_frame = ctk.CTkFrame(self.root)
        self.location_frame.pack(pady=20)

        # City selection buttons (arranged in a 2x3 grid)
        self.create_city_button(self.lahore_img, "Lahore", 0, 0)
        self.create_city_button(self.karachi_img, "Karachi", 0, 1)
        self.create_city_button(self.islamabad_img, "Islamabad", 0, 2)
        self.create_city_button(self.faisalabad_img, "Faisalabad", 1, 0)
        self.create_city_button(self.peshawar_img, "Peshawar", 1, 1)
        self.create_city_button(self.multan_img, "Multan", 1, 2)

        # Back button to return to the previous screen
        back_button = ctk.CTkButton(self.root, text=self.get_text("Back"), command=self.go_back)
        back_button.pack(pady=20)

    def create_city_button(self, image, city_name, row, column):
        # Create a button for each city
        city_button = ctk.CTkButton(self.location_frame, image=image, text=city_name, compound="top", command=lambda: self.on_city_selected(city_name))
        city_button.grid(row=row, column=column, padx=20, pady=10)

    def on_city_selected(self, city):
        # After selecting a city, save the location and navigate to the next screen
        self.location = city
        self.screen_stack.append("main_screen_after_location_selection")
        
        for widget in self.root.winfo_children():
            widget.destroy()

        # Now navigate to the main screen (e.g., jobs or profile)
        self.create_labor_main_screen()

    def create_labor_main_screen(self):
        # This will be the main screen after selecting the skill and location
        self.screen_stack.append("main_screen")

        # Remove "My Profile" button as per the updated requirement
        self.jobs_button = ctk.CTkButton(self.root, text=self.get_text("View Jobs"), command=self.view_jobs)
        self.jobs_button.pack(pady=20)

    def view_jobs(self):
        # Display jobs screen (for demo purposes)
        self.title_label = ctk.CTkLabel(self.root, text=self.get_text("Available Jobs"), font=("Arial", 24))
        self.title_label.pack(pady=20)

        # Simulate available jobs based on selected skill and location
        if self.skill and self.location:
            jobs_text = f"Available jobs for {self.skill} in {self.location}:"
            jobs_text += "\n\n1. Job 1 - Details\n2. Job 2 - Details\n3. Job 3 - Details"
        else:
            jobs_text = "No job available. Please select a skill and location."

        self.jobs_label = ctk.CTkLabel(self.root, text=jobs_text, font=("Arial", 16))
        self.jobs_label.pack(pady=20)

        # Back button to return to the main screen
        back_button = ctk.CTkButton(self.root, text=self.get_text("Back"), command=self.go_back)
        back_button.pack(pady=10)

    def go_back(self):
        # Pop the last screen from the stack
        if self.screen_stack:
            last_screen = self.screen_stack.pop()
            for widget in self.root.winfo_children():
                widget.destroy()

            # Navigate to the previous screen
            if last_screen == "skill_selection_screen":
                self.create_skill_selection_screen()
            elif last_screen == "location_selection_screen":
                self.create_skill_selection_screen()
            elif last_screen == "main_screen_after_location_selection":
                self.create_location_selection_screen()
            elif last_screen == "main_screen":
                self.create_labor_main_screen()

    def get_text(self, text):
        # This function returns the translated text based on the selected language
        translations = {
            "Select Your Location": {"English": "Select Your Location", "Urdu": "اپنا شہر منتخب کریں"},
            "Lahore": {"English": "Lahore", "Urdu": "لاہور"},
            "Karachi": {"English": "Karachi", "Urdu": "کراچی"},
            "Islamabad": {"English": "Islamabad", "Urdu": "اسلام آباد"},
            "Faisalabad": {"English": "Faisalabad", "Urdu": "فیصل آباد"},
            "Peshawar": {"English": "Peshawar", "Urdu": "پشاور"},
            "Multan": {"English": "Multan", "Urdu": "ملتان"},
            "Back": {"English": "Back", "Urdu": "پیچھے"},
            "View Jobs": {"English": "View Jobs", "Urdu": "ملازمتیں دیکھیں"},
            "Available Jobs": {"English": "Available Jobs", "Urdu": "دستیاب ملازمتیں"},
        }
        return translations.get(text, {}).get(self.language, text)


if __name__ == "__main__":
    root = ctk.CTk()
    app = LaborEmploymentApp(root)
    root.mainloop()
