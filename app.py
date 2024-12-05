from tkinter import *
from tkinter import messagebox

class SignupForm:
    def __init__(self, root):
        self.root = root
        self.root.geometry("444x234")  # Width x Height
        self.root.minsize(200, 100)    # Min Width, Height
        self.root.maxsize(1200, 988)   # Max Width, Height
        self.root.title("Workedin")
        
        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Full name field
        self.name_label = Label(self.root, text="Full name:")
        self.name_label.pack(pady=5)
        self.name_entry = Entry(self.root)
        self.name_entry.pack(pady=5)

        # Contact info field
        self.contact_label = Label(self.root, text="Contact info:")
        self.contact_label.pack(pady=5)
        self.contact_entry = Entry(self.root)
        self.contact_entry.pack(pady=5)

        # Skill field (dropdown)
        self.skill_label = Label(self.root, text="Skill:")
        self.skill_label.pack(pady=5)
        self.skills = ["Plumber", "Carpenter", "Electrician", "Painter", "Others"]
        self.skill_var = StringVar(self.root)
        self.skill_var.set("Plumber")  # Default value
        self.skill_menu = OptionMenu(self.root, self.skill_var, *self.skills)
        self.skill_menu.pack(pady=5)

        # Location field
        self.location_label = Label(self.root, text="Location (city):")
        self.location_label.pack(pady=5)
        self.location_entry = Entry(self.root)
        self.location_entry.pack(pady=5)

        # Experience field
        self.experience_label = Label(self.root, text="Experience (years):")
        self.experience_label.pack(pady=5)
        self.experience_entry = Entry(self.root)
        self.experience_entry.pack(pady=5)

        # Sign-up button
        self.sign_up_button = Button(self.root, text="Sign-up", command=self.submit_signup)
        self.sign_up_button.pack(pady=20)

    def validate_input(self):
        # Getting input from user
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        skill = self.skill_var.get()
        location = self.location_entry.get()
        experience = self.experience_entry.get()

        # Checking if all the required fields are filled
        if not name or not contact or not skill or not location:
            messagebox.showwarning("Input error", "Please fill all required fields")
            return False

        # Checking if name contains only alphabets
        if not name.isalpha():
            messagebox.showwarning("Input error", "Name should contain only alphabets")
            return False

        # Checking if contact contains only numbers
        if not contact.isnumeric():
            messagebox.showwarning("Input error", "Contact should contain only numbers")
            return False

        # Checking if skill contains only alphabets
        if not skill.isalpha():
            messagebox.showwarning("Input error", "Skill should contain only alphabets")
            return False

        # Checking if experience contains only numbers
        if not experience.isnumeric():
            messagebox.showwarning("Input error", "Experience should contain only numbers")
            return False

        return True

    def clear_form(self):
        # Clear the form after successful submission
        self.name_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.skill_var.set("Plumber")  # Reset dropdown to default value
        self.location_entry.delete(0, END)
        self.experience_entry.delete(0, END)

    def submit_signup(self):
        # If validation passes, display success message
        if self.validate_input():
            name = self.name_entry.get()
            messagebox.showinfo("Success", f"Sign-up successful for {name}")
            self.clear_form()  # Clear the form after successful sign-up

# Create the main window
root = Tk()
signup_form = SignupForm(root)  # Create an instance of SignupForm
root.mainloop()

