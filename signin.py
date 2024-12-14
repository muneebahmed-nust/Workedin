import customtkinter as ctk

class LaborEmploymentApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x400")
        self.language = "English"  # Default language is English
        self.create_signin_screen()

    def create_signin_screen(self):
        # Create the back button
        back_button = ctk.CTkButton(self.root, text=self.get_text("Back"), command=self.go_back)
        back_button.pack(pady=10, anchor="w", padx=10)

        # Label for sign-in screen
        self.title_label = ctk.CTkLabel(self.root, text=self.get_text("Sign In"), font=("Arial", 24))
        self.title_label.pack(pady=20)

        # Dropdown for selecting user type (Tradesperson or Employer)
        self.user_type_dropdown = ctk.CTkOptionMenu(self.root, values=[self.get_text("Tradesperson"), self.get_text("Employer")])
        self.user_type_dropdown.pack(pady=10)

        # Language selection (English or Urdu)
        language_label = ctk.CTkLabel(self.root, text=self.get_text("Select Language"), font=("Arial", 16))
        language_label.pack(pady=10)

        self.language_dropdown = ctk.CTkOptionMenu(self.root, values=[self.get_text("English"), self.get_text("Urdu")], command=self.change_language)
        self.language_dropdown.pack(pady=10)

        # Label and Entry for username
        self.username_label = ctk.CTkLabel(self.root, text=self.get_text("Username"), font=("Arial", 16))
        self.username_label.pack(pady=5)

        self.username_entry = ctk.CTkEntry(self.root, placeholder_text=self.get_text("Enter your username"))
        self.username_entry.pack(pady=5)

        # Label and Entry for password
        self.password_label = ctk.CTkLabel(self.root, text=self.get_text("Password"), font=("Arial", 16))
        self.password_label.pack(pady=5)

        self.password_entry = ctk.CTkEntry(self.root, placeholder_text=self.get_text("Enter your password"), show="*")
        self.password_entry.pack(pady=5)

        # Sign-in button
        signin_button = ctk.CTkButton(self.root, text=self.get_text("Sign In"), command=self.sign_in)
        signin_button.pack(pady=20)

    def get_text(self, text):
        # This function returns the translated text based on the selected language
        translations = {
            "Sign In": {"English": "Sign In", "Urdu": "سائن ان"},
            "Back": {"English": "Back", "Urdu": "پیچھے"},
            "Tradesperson": {"English": "Tradesperson", "Urdu": "ہنر مند"},
            "Employer": {"English": "Employer", "Urdu": "ملازمت دینے والا"},
            "Select Language": {"English": "Select Language", "Urdu": "زبان منتخب کریں"},
            "English": {"English": "English", "Urdu": "انگریزی"},
            "Urdu": {"English": "Urdu", "Urdu": "اردو"},
            "Username": {"English": "Username", "Urdu": "یوزر نیم"},
            "Enter your username": {"English": "Enter your username", "Urdu": "اپنا یوزر نیم درج کریں"},
            "Password": {"English": "Password", "Urdu": "پاس ورڈ"},
            "Enter your password": {"English": "Enter your password", "Urdu": "اپنا پاس ورڈ درج کریں"},
            "Sign In": {"English": "Sign In", "Urdu": "سائن ان"}
        }
        return translations.get(text, {}).get(self.language, text)

    def change_language(self, selected_language):
        # Change the language without destroying the window
        self.language = selected_language
        self.update_text()

        # Set right-to-left text direction for Urdu
        if selected_language == "Urdu":
            self.set_rtl(True)
        else:
            self.set_rtl(False)

    def set_rtl(self, rtl):
        # Set the widgets to RTL if the language is Urdu
        if rtl:
            self.username_entry.configure(text_alignment="right")
            self.password_entry.configure(text_alignment="right")
            self.username_label.configure(anchor="e")
            self.password_label.configure(anchor="e")
        else:
            self.username_entry.configure(text_alignment="left")
            self.password_entry.configure(text_alignment="left")
            self.username_label.configure(anchor="w")
            self.password_label.configure(anchor="w")

    def update_text(self):
        # Update all the UI texts based on the current language
        self.title_label.configure(text=self.get_text("Sign In"))
        self.username_label.configure(text=self.get_text("Username"))
        self.password_label.configure(text=self.get_text("Password"))
        
        # Update the placeholder text for the entry widgets
        self.username_entry.configure(placeholder_text=self.get_text("Enter your username"))
        self.password_entry.configure(placeholder_text=self.get_text("Enter your password"))
        
        # Update dropdown values
        self.user_type_dropdown.configure(values=[self.get_text("Tradesperson"), self.get_text("Employer")])
        self.language_dropdown.configure(values=[self.get_text("English"), self.get_text("Urdu")])
        
        # Set the selected language
        self.language_dropdown.set(self.get_text(self.language))  # Set the selected language option

    def sign_in(self):
        # Get username and password values from the Entry widgets
        username = self.username_entry.get()
        password = self.password_entry.get()

        # For now, we just print the username and password (in a real app, you'd check these values)
        print(f"Username: {username}")
        print(f"Password: {password}")

        # Implement the logic to verify username and password here
        # For example, you can check against a database or predefined credentials.

        # You can show a message if the sign-in was successful or if it failed
        if username == "testuser" and password == "password123":  # Example credentials
            print("Sign-in successful!")
        else:
            print("Invalid username or password.")

    def go_back(self):
        # When the back button is clicked, you can navigate to the previous screen
        print("Going back to the previous screen.")
        # You can replace this with actual navigation functionality if needed.

if __name__ == "__main__":
    root = ctk.CTk()
    app = LaborEmploymentApp(root)
    root.mainloop()
