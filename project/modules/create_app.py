import customtkinter as ctk
import modules.create_frame as m_frame
# import modules.button_functions as m_button_func
import modules.scene as m_scene


class App(ctk.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.geometry(f"{app_width}x{app_height}+{0}x{100}")
        self.title("Picture")
        self.resizable(False, False)
        
        self.REGISTER = m_frame.MyFrame("Реєстрація", master= self, width= app_width, height= app_height)
        self.MAIN = m_frame.MyFrame("Головне вікно", master= self, width= app_width, height= app_height)
        self.AVTORIZATION = m_frame.MyFrame("Авторізація", master= self, width= app_width, height= app_height)
        self.IMAGE_WINDOW = m_frame.MyFrame("Генерація малюнків", master= self, width= app_width, height= app_height)
        
        # elif m_scene.scene == "Головне вікно":
        self.MAIN.grid(row = 0, column = 0)
        # elif m_scene.scene == "Авторізація":
        #     self.AVTORIZATION.grid(row = 0, column = 0)
        # elif m_scene.scene == "Генерація малюнків":
        #     self.IMAGE_WINDOW.grid(row = 0, column = 0)
            
            
main_app = App(500, 500)