import customtkinter as ctk
import modules.create_app as m_app
import modules.button_functions as m_button_func
import modules.create_images as m_images


def create_button(master, text, width = 200, height = 50, border_width = 2, border_color = "green", func = None):
    button = ctk.CTkButton( master = master,
                            width = width,
                            height = height,
                            border_width = border_width,
                            border_color = border_color,
                            text = text,
                            command = func
    )
    return button

bt1 = create_button(master=m_app.main_app.MAIN, text = "Реєстрація", func = m_button_func.registration)
bt1.place(x = 150, y = 200)
# 
bt2 = create_button(master=m_app.main_app.MAIN, text = "Авторизація", func = m_button_func.authorisation)
bt2.place(x = 150, y = 300)
# 
bt_confirm_registration = create_button(master=m_app.main_app.REGISTER, text = "Підтвердити реєстрацію", func = m_button_func.confirm_registration)
bt_confirm_registration.place(x = 150, y = 400)
# 
bt_confirm_auth = create_button(master=m_app.main_app.AVTORIZATION, text = "Підтвердити авторизацію", func = m_button_func.confirm_auth)
bt_confirm_auth.place(x = 150, y = 300)

bt_create_images = create_button(master=m_app.main_app.IMAGE_WINDOW, text = "Зробити малюнок", func = m_images.show_image)
bt_create_images.place(x=150, y= 400)

