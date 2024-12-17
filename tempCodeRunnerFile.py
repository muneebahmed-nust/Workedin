
            self.current_frame.destroy()
        # Create new frame
        self.current_frame = page_func()

    def select_language_page(self):
        frame = ctk.CTkFrame(self.root, width=1000, height=600)
        frame.pack(fill="both", expand=True)
        select_language_heading=ctk.CTkLabel(frame, 
                                    text="Select Language \nزبان منتخب کریں", 