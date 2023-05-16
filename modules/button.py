import customtkinter, modules.app, modules.button_functions

add_picture = customtkinter.CTkButton(
    master = modules.app.main_app, 
    width = 100, 
    height = 30, 
    command = modules.button_functions.picture, 
    border_width= 3,
    text = "Нова картинка",
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538"
)

save_picture = customtkinter.CTkButton(
    master = modules.app.main_app, 
    width = 100, 
    height = 30, 
    command = modules.button_functions.save, 
    border_width= 3,
    text = "Зберегти",
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538"
)

crop = customtkinter.CTkButton(
    master=modules.app.main_app,
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538",
    width=100,
    height=30,
    text="Обрiзати",
    border_width=3,
    command = modules.button_functions.picture_crop
)

filters = customtkinter.CTkButton(
    master=modules.app.main_app,
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538",
    width=100,
    height=30,
    text="Фiльтри",
    border_width=3,
    command = modules.button_functions.filters
)

rotate = customtkinter.CTkButton(
    master=modules.app.main_app,
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538",
    width=100,
    height=30,
    text="Поворот",
    border_width=3,
    command = modules.button_functions.rotate
)

write = customtkinter.CTkButton(
    master=modules.app.main_app,
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538",
    width=100,
    height=30,
    text="Текст",
    border_width=3,
    command = modules.button_functions.text
)

add_picture.place(x=20, y=20)
save_picture.place(x=20, y=60)
crop.place(x=20, y=100)
filters.place(x=20, y=140)
rotate.place(x=20, y=180)
write.place(x=20, y=220)