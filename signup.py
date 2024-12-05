from tkinter import *
from tkinter import messagebox

class SignupForm:
    def __init__(self, root):
        self.root = root
        self.root.geometry("444x450")  # Increased height for additional language support
        self.root.minsize(200, 100)    # Min Width, Height
        self.root.maxsize(1200, 988)   # Max Width, Height
        self.root.title("Workedin")

        # Set background color to light mint green (pastel green)
        self.root.config(bg="#A8E6CF")

        # Add a language toggle variable
        self.language = StringVar(self.root)
        self.language.set("English")  # Default to English

        # Create UI components
        self.create_widgets()

        # Show the pop-up after 3 seconds (3000 milliseconds)
        self.root.after(3000, self.show_popup)

        # Set the interface to the default language (English initially)
        self.change_language(self.language.get())

    def create_widgets(self):
        # Employment App Header
        self.header_label = Label(self.root, text="Workedin: Employment Made Easy", bg="#A8E6CF", fg="black", font=("Arial", 16, "bold"))
        self.header_label.pack(pady=20)

        # Short description label
        self.description_label = Label(self.root, text="Find the best jobs and make connections easily!", bg="#A8E6CF", fg="black", font=("Arial", 10))
        self.description_label.pack(pady=5)

        # Language Selection Dropdown
        self.language_label = Label(self.root, text="Select Language:", bg="#A8E6CF", fg="black", font=("Arial", 10))
        self.language_label.pack(pady=10)
        
        self.language_menu = OptionMenu(self.root, self.language, "English", "Urdu", command=self.change_language)
        self.language_menu.pack(pady=5)

        # Full name field
        self.name_label = Label(self.root, text="Full name:", bg="#A8E6CF", fg="black", font=("Arial", 10))
        self.name_label.pack(pady=5)
        self.name_entry = Entry(self.root, font=("Arial", 10))
        self.name_entry.pack(pady=5)

        # Contact info field
        self.contact_label = Label(self.root, text="Contact info:", bg="#A8E6CF", fg="black", font=("Arial", 10))
        self.contact_label.pack(pady=5)
        self.contact_entry = Entry(self.root, font=("Arial", 10))
        self.contact_entry.pack(pady=5)

        # Skill field (dropdown)
        self.skill_label = Label(self.root, text="Skill:", bg="#A8E6CF", fg="black", font=("Arial", 10))
        self.skill_label.pack(pady=5)
        
        self.skills_english = ["Plumber", "Carpenter", "Electrician", "Painter", "Others"]
        self.skills_urdu = ["پلمبر", "نقاش", "الیکٹریشن", "پینٹر", "دیگر"]
        
        self.skill_var = StringVar(self.root)
        self.skill_var.set(self.skills_english[0])  # Default value in English
        
        self.skill_menu = OptionMenu(self.root, self.skill_var, *self.skills_english)
        self.skill_menu.pack(pady=5)

        # Location field
        self.location_label = Label(self.root, text="Location (city):", bg="#A8E6CF", fg="black", font=("Arial", 10))
        self.location_label.pack(pady=5)
        self.location_entry = Entry(self.root, font=("Arial", 10))
        self.location_entry.pack(pady=5)

        # Sign-up button
        self.sign_up_button = Button(self.root, text="Sign-up", command=self.submit_signup, bg="#4CAF50", fg="white", font=("Arial", 10))
        self.sign_up_button.pack(pady=20)

        # Sign-in button
        self.sign_in_button = Button(self.root, text="Already have an account? Sign In", command=self.show_sign_in, bg="#FF6347", fg="white", font=("Arial", 10))
        self.sign_in_button.pack(pady=5)

    def change_language(self, selected_language):
        """Change all the UI elements based on selected language."""
        if selected_language == "English":
            # Update UI for English
            self.name_label.config(text="Full name:")
            self.contact_label.config(text="Contact info:")
            self.skill_label.config(text="Skill:")
            self.location_label.config(text="Location (city):")
            self.sign_up_button.config(text="Sign-up")
            self.sign_in_button.config(text="Already have an account? Sign In")

            # Set entry fields to Left-to-Right (LTR) for English
            self.name_entry.config(justify=LEFT)
            self.contact_entry.config(justify=LEFT)
            self.location_entry.config(justify=LEFT)

            # Update skill dropdown to English
            self.skill_var.set(self.skills_english[0])
            self.skill_menu['menu'].delete(0, 'end')
            for skill in self.skills_english:
                self.skill_menu['menu'].add_command(label=skill, command=lambda value=skill: self.skill_var.set(value))

        elif selected_language == "Urdu":
            # Update UI for Urdu
            self.name_label.config(text="پورا نام:")
            self.contact_label.config(text="رابطہ کی معلومات:")
            self.skill_label.config(text="مہارت:")
            self.location_label.config(text="مقام (شہر):")
            self.sign_up_button.config(text="سائن اپ کریں")
            self.sign_in_button.config(text="کیا آپ کے پاس اکاؤنٹ ہے؟ سائن ان کریں")

            # Set entry fields to Right-to-Left (RTL) for Urdu input
            self.name_entry.config(justify=RIGHT)
            self.contact_entry.config(justify=RIGHT)
            self.location_entry.config(justify=RIGHT)

            # Update skill dropdown to Urdu
            self.skill_var.set(self.skills_urdu[0])
            self.skill_menu['menu'].delete(0, 'end')
            for skill in self.skills_urdu:
                self.skill_menu['menu'].add_command(label=skill, command=lambda value=skill: self.skill_var.set(value))

    def show_popup(self):
        # Create a custom pop-up window that appears in front of the sign-up page
        popup = Toplevel(self.root)
        popup.geometry("300x150")  # Set size of pop-up window
        popup.title("Workedin")

        # Add label in the pop-up with both English and Urdu text
        popup_label = Label(popup, text="Making employment easy through Workedin\nملازمت کو ورکڈن کے ذریعے آسان بنانا", 
                            font=("Arial", 12), bg="#FFEB3B", fg="black", justify=LEFT)
        popup_label.pack(pady=20)

        # Add a button to close the pop-up
        close_button = Button(popup, text="Close", command=popup.destroy, bg="#FF6347", fg="white")
        close_button.pack(pady=10)

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
        self.name_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.skill_var.set("Plumber")  # Reset dropdown to default value
        self.location_entry.delete(0, END)

    def submit_signup(self):
        # If validation passes, display success message
        if self.validate_input():
            name = self.name_entry.get()
            messagebox.showinfo("Success", f"Sign-up successful for {name}")
            self.clear_form()  # Clear the form after successful sign-up

    def show_sign_in(self):
        # This method can show a sign-in form or a message box indicating a redirect
        messagebox.showinfo("Sign In", "Redirecting to the Sign In Page...")

# Create the main window
root = Tk()
signup_form = SignupForm(root)  # Create an instance of SignupForm
root.mainloop()


