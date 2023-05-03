import customtkinter
import PIL

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.WIDTH = 600
        self.HEIGHT = 400
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}+{0}+{100}")
        self.title("TriangleSheep")
        # self.FRAME = customtkinter.CTkFrame(master=self, border_width=3, border_color="orange", width=self.WIDTH-150, height=self.HEIGHT-40)
        # self.FRAME.place(x=150, y=40)
        self.resizable(False, False)
        self.TABVIEW = customtkinter.CTkTabview(master=self, width = 450, height = 400)
        self.TABVIEW.place(x=150, y=-10)


main_app = App()