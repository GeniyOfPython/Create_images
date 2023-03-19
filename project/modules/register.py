import customtkinter as ctk
import modules.create_app as m_app

entry_login_text = ctk.StringVar(master = m_app.main_app.REGISTER)
entry_password_text = ctk.StringVar(master = m_app.main_app.REGISTER)
entry_password_repeat_text = ctk.StringVar(master = m_app.main_app.REGISTER)

entry_login = ctk.CTkEntry(
    master= m_app.main_app.REGISTER,
    width = 200,
    height = 50, 
    border_width = 3,
    fg_color = "black",
    text_color = "white",
    textvariable= entry_login_text
)

entry_password = ctk.CTkEntry(
    master= m_app.main_app.REGISTER,
    width = 200,
    height = 50, 
    border_width = 3,
    fg_color = "black",
    text_color = "white",
    textvariable= entry_password_text
)

entry_password_repeat = ctk.CTkEntry(
    master= m_app.main_app.REGISTER,
    width = 200,
    height = 50, 
    border_width = 3,
    fg_color = "black",
    text_color = "white",
    textvariable= entry_password_repeat_text
)



entry_login.place(x = 150, y = 100)
entry_password.place(x = 150, y = 200)
entry_password_repeat.place(x = 150, y = 300)