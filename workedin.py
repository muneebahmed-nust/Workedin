import customtkinter as ctk
import utils  

#This is the app class which navigates between pages

class App:
    def __init__(self, root):
        self.root = root
        self.x_axis=self.root.winfo_screenwidth()/2
        self.y_axis=self.root.winfo_screenheight()/2
        self.current_frame = self.labour_data_entry_page()
        
        
    def show_page(self, page_func):
        # Destroy current frame if it exists
        if self.current_frame:
            self.current_frame.destroy()
        # Create new frame
        self.current_frame = page_func()
    
    def labour_data_entry_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        heading=ctk.CTkLabel(frame,text="Workedin",font=("Arial",24))
        heading.place(relx=0.5, y=20, anchor="center")

        name_label=ctk.CTkLabel(frame,text="Full Name:",font=("Arial",16))
        name_label.place(x=400,y=100,anchor="e")
        name_entry_box=ctk.CTkEntry(frame,width=200,height=30,placeholder_text="e.g Aslam Ahmed")
        name_entry_box.place(x=650,y=100,anchor="w")

        age_label=ctk.CTkLabel(frame,text="Age:",font=("Arial",16))
        age_label.place(x=400,y=150,anchor="e")
        age_entry_box=ctk.CTkEntry(frame,width=200,height=30)
        age_entry_box.place(x=650,y=150,anchor="w")

        phone_label=ctk.CTkLabel(frame,text="Phone:",font=("Arial",16))
        phone_label.place(x=400,y=200,anchor="e")
        phone_entry_box=ctk.CTkEntry(frame,width=200,height=30)
        phone_entry_box.place(x=650,y=200,anchor="w")

        cnic_label=ctk.CTkLabel(frame,text="CNIC:",font=("Arial",16))
        cnic_label.place(x=400,y=250,anchor="e")
        cnic_entry_box=ctk.CTkEntry(frame,width=200,height=30,placeholder_text="e.g 1234567890123")
        cnic_entry_box.place(x=650,y=250,anchor="w")

        experience_label=ctk.CTkLabel(frame,text="Number of years of experience:",font=("Arial",16))
        experience_label.place(x=400,y=300,anchor="e")
        experience_entry_box=ctk.CTkEntry(frame,width=200,height=30,placeholder_text="e.g 10")
        experience_entry_box.place(x=650,y=300,anchor="w")

        city_label=ctk.CTkLabel(frame,text="City:",font=("Arial",16))
        city_label.place(x=400,y=350,anchor="e")
        city_entry_box=ctk.CTkEntry(frame,width=200,height=30)
        city_entry_box.place(x=650,y=350,anchor="w")

        submit_button=ctk.CTkButton(frame,text="Submit",command=lambda:self.show_page(self.job_submission_page))
        submit_button.place(x=400,y=400,anchor="center")
       
        return frame
        
    def job_submission_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        
        heading=ctk.CTkLabel(frame,text="Job Submission",font=("Arial",24))
        heading.place(relx=0.5, y=20, anchor="center")
        
        city_label =ctk.CTkLabel(frame, text="City",font=("Arial",16))
        city_label.place(x=400,y=100,anchor="e")
        city_box= ctk.CTkComboBox(frame, values= [
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
    
        city_box.place(x=650,y=100,anchor="w")

        job_type_label = ctk.CTkLabel(frame, text="Job Type",font=("Arial",16))
        job_type_label.place(x=400,y=150,anchor="e")
        job_type_box= ctk.CTkComboBox(frame, values=["Driver","Labour","Electrician","Plumber","Mason","Carpenter","Painter","Cleaner","Cook","Security Guard","Other"], command=self.on_job_type_change)
        job_type_box.place(x=650,y=150,anchor="w")
        
        self.other_job_entry = ctk.CTkEntry(frame,placeholder_text="Please specify", width=200, height=30)
        self.other_job_entry.place(x=650, y=200, anchor="w")
        self.other_job_entry.configure(state="disabled")
        
        user_name_label = ctk.CTkLabel(frame, text="User Name",font=("Arial",16))
        user_name_label.place(x=400,y=250,anchor="e")
        user_name_entry = ctk.CTkEntry(frame,placeholder_text="e.g Aslam Ahmed", width=200, height=30)
        user_name_entry.place(x=650, y=250, anchor="w")

        job_description_label = ctk.CTkLabel(frame, text="Job Description",font=("Arial",16))
        job_description_label.place(x=400,y=300,anchor="ne")
        job_description_entry = ctk.CTkTextbox(frame, width=250, height=100)
        job_description_entry.insert("0.0", "")  # Add placeholder text
        job_description_entry.place(x=650, y=300, anchor="nw")

        submit_button=ctk.CTkButton(frame,text="Submit",command=lambda:self.show_page(self.job_submission_page))
        return frame

    def on_job_type_change(self, selected_job_type):
        if selected_job_type == "Other":
            # Show the entry
            self.other_job_entry.configure(state="normal")
        else:
            self.other_job_entry.configure(state="disabled")
            



    def caller(self):
        print("hello\n")
    
    def x_value_center(self,widget):
        print("Value" + str(widget.winfo_width()))
        print("anove")
        return self.x_axis-(widget.winfo_width()/2)
    
    


def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    root = ctk.CTk()
    root.state("zoomed")
    print(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.geometry("1000x600")
    root.title("Workedin")
    app = App(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()


