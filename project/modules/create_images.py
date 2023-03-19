import customtkinter as ctk
from PIL import Image
import random
import modules.find_path as m_path
import modules.create_app as m_app

list_of_images = ["images/1.jpg", "images/2.jpeg", "images/3.jpeg", "images/4.jpeg", "images/5.jpeg"]

def show_image():
    choice = random.choice(list_of_images)
    # number = random.randint(0,4)
    # print("\n", number, "\n")
    
    image = ctk.CTkImage(
        light_image= Image.open(m_path.find_path_to_file(choice)), 
        size = ((200, 200))
    )
    label = ctk.CTkLabel(
        master = m_app.main_app.IMAGE_WINDOW,
        text = "",
        image = image
    )
    label.place(x = 150, y = 100)