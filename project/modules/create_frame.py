import customtkinter as ctk

class MyFrame(ctk.CTkFrame):
    def __init__(self, text, master, width, height, **kwargs):
        super().__init__(master= master, width= width, height= height, **kwargs)
        self.LABEL = ctk.CTkLabel(self, text= text)
        self.LABEL.place(x = 210, y = 10)