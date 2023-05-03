import customtkinter, requests, modules.app
from PIL import Image
counter = 0
def picture():
    global counter
    text = customtkinter.StringVar()
    window = customtkinter.CTkEntry(master=modules.app.main_app, width=300, height=150, textvariable=text)
    window.place(x=150, y=150)
    def pressing_button(event):
        global counter
        try:
            a = requests.get(url=text.get(), stream=True).raw
            img = Image.open(a)
            counter += 1
            new_tab = modules.app.main_app.TABVIEW.add(f"Вкладка {counter}")
            b = customtkinter.CTkImage(light_image=img, size=(450, 400))
            yeyy_image = customtkinter.CTkLabel(master=new_tab, text=" ", image=b)
            yeyy_image.place(x=0, y=0)
            window.place_forget()
        # return a
        except:
            print("ахахахахха ти какашка")

    window.bind('<Return>', pressing_button)