import customtkinter, requests, modules.app
from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont

counter = 0
url_loading = None
point_counter = 0
x1, y1 = None, None
x2, y2 = None, None

def picture():
    if counter < 4:
        def url():
            global url_loading
            url_loading = True
            button_file.place_forget()
            button_url.place_forget()
            window.place(x=100, y=150)
            button_open.place(x = 400, y = 150)



        def local_file():
            global url_loading
            url_loading = False
            button_file.place_forget()
            button_url.place_forget()
            pressing_button_file()
            

        
        def pressing_button_url():
            global counter

            try:
                filename = requests.get(url=text.get(), stream=True).raw
                modules.app.main_app.CURRENT_IMAGE = Image.open(filename)                
                counter += 1
                # new_tab = modules.app.main_app.TABVIEW.add(f"Вкладка {counter}")
                b = customtkinter.CTkImage(light_image=modules.app.main_app.CURRENT_IMAGE, size=(450, 400))
                modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=b, width = 450, height = 400)
                modules.app.main_app.IMAGE_LABEL.place(x=150, y=0)
                window.place_forget()
                button_open.place_forget()
                info_frame = customtkinter.CTkFrame(master=modules.app.main_app, width=140, height=100)
                info_frame.place(x=5, y=260)
                info_dict = {
                    "Size": modules.app.main_app.CURRENT_IMAGE.size, 
                    "Format": modules.app.main_app.CURRENT_IMAGE.format, 
                    "Mode": modules.app.main_app.CURRENT_IMAGE.mode
                }
                label_y = 0
                for info in info_dict.items():
                    label = customtkinter.CTkLabel(master=info_frame, text=info)
                    label.place(x=0, y=label_y)
                    label_y += 20
                # return a
            except:
                print("ахахахахха ти какашка")

        def pressing_button_file():
            global counter

            try:
                filename = customtkinter.filedialog.askopenfilename()
                img = Image.open(filename)
                modules.app.main_app.CURRENT_IMAGE = img
                counter += 1
                # new_tab = modules.app.main_app.TABVIEW.add(f"Вкладка {counter}")
                b = customtkinter.CTkImage(light_image=img, size=(450, 400))
                modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=b)
                modules.app.main_app.IMAGE_LABEL.place(x=150, y=0)
                # window.unbind('<Return>')
                info_frame = customtkinter.CTkFrame(master=modules.app.main_app, width=140, height=70)
                info_frame.place(x=5, y=325)
                info_dict = {
                    "Size": img.size, 
                    "Format": img.format, 
                    "Mode": img.mode
                }
                label_y = 0
                for info in info_dict.items():
                    label = customtkinter.CTkLabel(master=info_frame, text=info)
                    label.place(x=0, y=label_y)
                    label_y += 20
                # return a
            except:
                print("ахахахахха ти какашка")
            # window.bind('<Return>', pressing_button)

        
            

        button_file = customtkinter.CTkButton(
            master=modules.app.main_app, 
            width=150, 
            height=50, 
            text="Обрати файл з комп'ютера",
            fg_color = "#302f2b",
            border_color = "#d36f23",
            hover_color = "#c67538",
            border_width = 3,
            command = local_file
        )

        button_url = customtkinter.CTkButton(
            master=modules.app.main_app, 
            width=150, 
            height=50, 
            text="URL",
            fg_color = "#302f2b",
            border_color = "#d36f23",
            hover_color = "#c67538",
            border_width = 3,
            command = url
        )   

        button_file.place(x = 150, y = 150)
        button_url.place(x = 150, y = 205)
        
        text = customtkinter.StringVar()
        window = customtkinter.CTkEntry(master=modules.app.main_app, width=300, height=50, textvariable=text)
        button_open = customtkinter.CTkButton(
            master=modules.app.main_app, 
            width=150, 
            height=50, 
            text="Відкрити",
            fg_color = "#302f2b",
            border_color = "#d36f23",
            hover_color = "#c67538",
            border_width = 3,
            command = pressing_button_url
        )   

        # Dimka Perdimka

# def save():
def save():
    if modules.app.main_app.CURRENT_IMAGE:
        def finished():             
            try:
                if filename.get() and width_text.get() and height_text.get():
                    width_int = int(width_text.get())
                    height_int = int(height_text.get())
                    a = modules.app.main_app.CURRENT_IMAGE.resize((width_int, height_int))
                    a.save(filename.get())
                    window.place_forget()
            except:
                print("Казьол неправильно заполнил")

        window = customtkinter.CTkFrame(master = modules.app.main_app, width = 200, height = 400, border_width = 3)
        
        filename = customtkinter.StringVar()
        width_text = customtkinter.StringVar()
        height_text = customtkinter.StringVar()
        
        filename_entry = customtkinter.CTkEntry(master=window, width = 190, height = 100, textvariable=filename)
        width_entry = customtkinter.CTkEntry(master=window, width = 190, height = 100, textvariable=width_text)
        height_entry = customtkinter.CTkEntry(master=window, width = 190, height = 50, textvariable=height_text)


        filename_label = customtkinter.CTkLabel(master = window, text = "Ім'я файлу:")
        width_label = customtkinter.CTkLabel(master = window, text = "Ширина зображення:")
        height_label = customtkinter.CTkLabel(master = window, text = "Висота зображення:")

        finish_button = customtkinter.CTkButton(
            master = window,
            width = 190,
            height = 25, 
            text = "Зберегти",
            fg_color = "#302f2b",
            border_color = "#d36f23",
            hover_color = "#c67538",
            border_width = 3, 
            command = finished
        )

        filename_entry.place(x = 5, y = 40)
        filename_label.place(x = 5, y = 5)
        width_entry.place(x=5, y=170)
        width_label.place(x = 5, y = 140)
        height_entry.place(x=5,y=300)
        height_label.place(x = 5, y = 270)
        finish_button.place(x = 5, y = 375)

        window.place(x = 200, y = 0)


def picture_crop():
    frame = customtkinter.CTkFrame(master = modules.app.main_app, width = 200, height = 400, border_width = 3)

    pointx1 = customtkinter.StringVar()
    pointx2 = customtkinter.StringVar()
    pointy1 = customtkinter.StringVar()
    pointy2 = customtkinter.StringVar()

    entry = customtkinter.CTkEntry(master = frame, width = 190, height = 100, textvariable = pointx1) 
    entry2 = customtkinter.CTkEntry(master = frame, width = 190, height = 100, textvariable = pointy1) 
    entry3 = customtkinter.CTkEntry(master = frame, width = 190, height = 100, textvariable = pointx2) 
    entry4 = customtkinter.CTkEntry(master = frame, width = 190, height = 50, textvariable = pointy2)
    
    def crop_function():
        modules.app.main_app.CURRENT_IMAGE = modules.app.main_app.CURRENT_IMAGE.crop((int(pointx1.get()), int(pointy1.get()), int(pointx2.get()), int(pointy2.get())))
        img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (450, 400))
        modules.app.main_app.IMAGE_LABEL.place_forget()
        modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image = img, width = 450, height = 400)
        modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)
        frame.place_forget()

    confirm = customtkinter.CTkButton(
        master = frame, width = 190, height = 30, text = "Обрізати", command=crop_function,
        fg_color = "#302f2b",
        border_color = "#d36f23",
        hover_color = "#c67538",
        border_width = 3
    )
    
    frame.place(x = 200, y = 0)
    entry.place(x = 5, y = 10)
    entry2.place(x = 5, y = 110)
    entry3.place(x = 5, y = 210) 
    entry4.place(x = 5, y = 310)
    confirm.place(x = 5, y = 360)

def filters():
    frame = customtkinter.CTkFrame(master = modules.app.main_app, width = 200, height = 400)
    def grayscale():
        modules.app.main_app.CURRENT_IMAGE = modules.app.main_app.CURRENT_IMAGE.convert("L")
        img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (450, 400))
        modules.app.main_app.IMAGE_LABEL.place_forget()
        modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=img, width = 450, height = 400)
        modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)
        frame.place_forget()

    def blur():
        modules.app.main_app.CURRENT_IMAGE = modules.app.main_app.CURRENT_IMAGE.filter(ImageFilter.BLUR)
        img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (450, 400))
        modules.app.main_app.IMAGE_LABEL.place_forget()
        modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=img, width = 450, height = 400)
        modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)
        frame.place_forget()

    def sharpen():
        modules.app.main_app.CURRENT_IMAGE = modules.app.main_app.CURRENT_IMAGE.filter(ImageFilter.SHARPEN)
        img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (450, 400))
        modules.app.main_app.IMAGE_LABEL.place_forget()
        modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=img, width = 450, height = 400)
        modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)
        frame.place_forget()
    
    def smooth():
        modules.app.main_app.CURRENT_IMAGE = modules.app.main_app.CURRENT_IMAGE.filter(ImageFilter.SMOOTH)
        img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (450, 400))
        modules.app.main_app.IMAGE_LABEL.place_forget()
        modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=img, width = 450, height = 400)
        modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)
        frame.place_forget()

    def detail():
        modules.app.main_app.CURRENT_IMAGE = modules.app.main_app.CURRENT_IMAGE.filter(ImageFilter.DETAIL)
        img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (450, 400))
        modules.app.main_app.IMAGE_LABEL.place_forget()
        modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=img, width = 450, height = 400)
        modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)
        frame.place_forget()

    grayscale_button = customtkinter.CTkButton(
        master = frame, width = 190, height = 50, text = "Чорно-білий", command=grayscale,
        fg_color = "#302f2b",
        border_color = "#d36f23",
        hover_color = "#c67538",
        border_width = 3
    )
    
    blur_button = customtkinter.CTkButton(
        master = frame, width = 190, height = 50, text = "Розмиття", command=blur,
        fg_color = "#302f2b",
        border_color = "#d36f23",
        hover_color = "#c67538",
        border_width = 3                                   
    )

    sharpen_button = customtkinter.CTkButton(
        master = frame, width = 190, height = 50, text = "Різкість", command=sharpen,
        fg_color = "#302f2b",
        border_color = "#d36f23",
        hover_color = "#c67538",
        border_width = 3
    )
    
    smooth_button = customtkinter.CTkButton(
        master = frame, width = 190, height = 50, text = "Згладжування", command=smooth,
        fg_color = "#302f2b",
        border_color = "#d36f23",
        hover_color = "#c67538",
        border_width = 3,                             
    )
    
    detail_button = customtkinter.CTkButton(
        master = frame, width = 190, height = 50, text = "Деталізація", command=detail,
        fg_color = "#302f2b",
        border_color = "#d36f23",
        hover_color = "#c67538",
        border_width = 3
    )

    grayscale_button.place(x = 5, y = 20)
    blur_button.place(x = 5, y = 80)
    sharpen_button.place(x = 5, y = 140)
    smooth_button.place(x = 5, y = 200)
    detail_button.place(x = 5, y = 260)
    
    frame.place(x = 150, y = 0)
def rotate():
    modules.app.main_app.CURRENT_IMAGE = modules.app.main_app.CURRENT_IMAGE.rotate(90)
    img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (450, 400))
    modules.app.main_app.IMAGE_LABEL.place_forget()
    modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=img, width = 450, height = 400)
    modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)

# snus kriminal papararara

def text():
    mouse_x = None
    mouse_y = None
    text_entry = customtkinter.StringVar()

    def mouse_pressed(event):
        global mouse_x, mouse_y
        mouse_x = modules.app.main_app.winfo_pointerx()
        mouse_y = modules.app.main_app.winfo_pointery()
        print(mouse_x, mouse_y)
        entry.place(x = mouse_x, y = mouse_y)
    
    def entry_pressed(event):
        if text_entry.get():
            modules.app.main_app.CURRENT_IMAGE = modules.app.main_app.CURRENT_IMAGE.text((mouse_x, mouse_y), text_entry.get())
            img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (450, 400))
            modules.app.main_app.IMAGE_LABEL.place_forget()
            modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image = img, width = 450, height = 400)
            modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)
            entry.place_forget()
    # frame = customtkinter.CTkFrame(master = modules.app.main_app, width = 200, height = 400, border_width = 3)
    modules.app.main_app.IMAGE_LABEL.bind("<Button-1>", mouse_pressed)
    
    entry = customtkinter.CTkEntry(master = modules.app.main_app, width = 190, height = 100, textvariable = text_entry) 
    font = ImageFont.truetype("arial.ttf", size=18)
    
    entry.bind("<Return>", entry_pressed)
