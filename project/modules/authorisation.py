import customtkinter as ctk
import modules.create_app as m_app

entry_password_text = ctk.StringVar()
entry_login_text = ctk.StringVar()

entry_login = ctk.CTkEntry(
    master= m_app.main_app.AVTORIZATION,
    width = 200,
    height = 50, 
    border_width = 3,
    fg_color = "black",
    text_color = "white",
    textvariable= entry_login_text
)

entry_password = ctk.CTkEntry(
    master= m_app.main_app.AVTORIZATION,
    width = 200,
    height = 50, 
    border_width = 3,
    fg_color = "black",
    text_color = "white",
    textvariable= entry_password_text
)

entry_login.place(x = 150, y = 100)
entry_password.place(x = 150, y = 200)