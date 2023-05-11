import customtkinter
import PIL

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.WIDTH = 600
        self.HEIGHT = 400
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}+{0}+{100}")
        self.title("TriangleSheep")
        self.resizable(False, False)
        # self.TABVIEW = customtkinter.CTkTabview(
        #     master = self,
        #     width = 590,
        #     height = 400,
        #     segmented_button_fg_color = "orange",
        #     segmented_button_selected_color = "#d36f23",
        #     segmented_button_selected_hover_color = "#c67538"
        # )
        # self.TABVIEW.place(x=5, y=-10)
        self.CURRENT_IMAGE = None# eron don don
        self.IMAGE_LABEL = None



main_app = App()