import customtkinter as ctk
import modules.register as m_reg
import modules.authorisation as m_auth
import modules.json_operations as m_json_ops
import modules.scene as m_scene
import modules.create_app as m_app



def confirm_registration():
    if m_reg.entry_login_text.get() and m_reg.entry_password_text.get() and m_reg.entry_password_repeat_text.get():
        if m_reg.entry_password_repeat_text.get() == m_reg.entry_password_text.get():
            m_json_ops.base.update({str(m_reg.entry_login_text.get()): str(m_reg.entry_password_text.get())})
            m_json_ops.write_json("json\\data.json")
            m_app.main_app.REGISTER.grid_forget()
            m_app.main_app.IMAGE_WINDOW.grid(row = 0, column = 0)
            
        else:
            label_wrong = ctk.CTkLabel(
                master=m_app.main_app.REGISTER,
                text="Паролі не співпадають!",
                text_color="red"
            )
            label_wrong.place(x= 180, y= 350)

def confirm_auth():
    if m_auth.entry_login_text.get() and m_auth.entry_password_text.get():
        entry_data = {
            m_auth.entry_login_text.get(): m_auth.entry_password_text.get()
        }
        data_auth = m_json_ops.read_json("json\\data.json")
        if entry_data.items() == dict(data_auth).items():
            m_app.main_app.AVTORIZATION.grid_forget()
            m_app.main_app.IMAGE_WINDOW.grid(row = 0, column = 0)
        else:
            label_wrong_2 = ctk.CTkLabel(
                master=m_app.main_app.AVTORIZATION,
                text="Щось не співпадає!",
                text_color="red"
            )
            label_wrong_2.place(x = 180, y = 250)


def registration():
    m_app.main_app.AVTORIZATION.grid_forget()
    m_app.main_app.MAIN.grid_forget()
    m_app.main_app.REGISTER.grid(row = 0, column = 0)

def authorisation():
    m_app.main_app.MAIN.grid_forget()
    m_app.main_app.REGISTER.grid_forget()
    m_app.main_app.AVTORIZATION.grid(row = 0, column = 0)